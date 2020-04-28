import argparse
import time
import os
import requests
import json
import xlsxwriter
from requests_toolbelt.multipart.encoder import MultipartEncoder

parser = argparse.ArgumentParser(description='scan through all apks and produce excel output')
parser.add_argument("-p", required=True, type=str, help="Path to the APK folder")
parser.add_argument("-api", required=True, type=str, help="Mobsf API key")
parser.add_argument("-url", required=True, type=str, help="Mobsf URL e.g. localhost:8000")

args = parser.parse_args()
path = args.p
api_key = args.api
mobsf_server = args.url

# compile list of apk paths
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.apk' in file:
            files.append(os.path.join(r, file))

# create excel file
workbook = xlsxwriter.Workbook("output.xlsx")
result_worksheet = workbook.add_worksheet("result")
cell_format = workbook.add_format({"text_wrap": True, "valign": 'vcenter'})

# for every apk path, send to mobsf
row = 0
col = 0
result_worksheet.write(row, col, "filename")
result_worksheet.write(row, col+1, "Permissions")
result_worksheet.write(row, col+2, "Manifest Analysis")
row+=1

for f in files:
	apk_name = f[f.rfind("/")+1:]
	print("Uploading", apk_name)
	multipart_data = MultipartEncoder(fields={'file': (f, open(f, 'rb'), 'application/octet-stream')})
	headers = {"Content-Type": multipart_data.content_type, "Authorization": api_key}
	response = requests.post(mobsf_server + '/api/v1/upload', data=multipart_data, headers=headers)
	resp_dict = json.loads(response.text)
	print("Uploaded", apk_name)

	# scan apk
	print("Scanning", apk_name)
	resp_dict["re_scan"] = 1 # enable rescan of apk
	headers = {'Authorization': api_key}
	response = requests.post(mobsf_server + '/api/v1/scan', data=resp_dict, headers=headers)
	print("Scanned", apk_name)
	scan_dict = json.loads(response.text)

	if "file_name" in scan_dict.keys():
		# if scan passes, write to excel
		result_worksheet.write(row, col, scan_dict["file_name"])

		permissions_output = ""
		for key, val in scan_dict["permissions"].items():
			permissions_output += key + " \n"
			for title, content in val.items():
				permissions_output += title + ": " + content + " \n"
			permissions_output += "\n"
		result_worksheet.write(row, col+1, permissions_output, cell_format)

		manifest_analysis = ""
		for item in scan_dict["manifest_analysis"]:
			manifest_analysis += "name: " + item["name"] + "\n"
			manifest_analysis += "stat: " + item["stat"] + "\n"
			manifest_analysis += "desc: " + item["desc"] + "\n"
			manifest_analysis += "\n"
		result_worksheet.write(row, col+2, manifest_analysis, cell_format)
		result_worksheet.set_row(row, 20+(len(scan_dict["manifest_analysis"])*5))
	else:
		# fail output name and that it failed
		result_worksheet.write(row, col, apk_name)
		result_worksheet.write(row, col+1, "scan failed")

	row += 1
	time.sleep(1) # needed to prevent connection reset by peer 

result_worksheet.set_column(col+1, col+1, 40)
result_worksheet.set_column(col+2, col+2, 100)
workbook.close()