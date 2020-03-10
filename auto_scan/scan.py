import argparse
import os
import requests
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

# for every apk path, send to mobsf
# for f in files:
filepath = files[0]
print(filepath)
print(api_key)
print(mobsf_server)
print("Uploading file")
multipart_data = MultipartEncoder(fields={'file': (filepath, open(filepath, 'rb'), 'application/octet-stream')})
headers = {'Content-Type': multipart_data.content_type, 'Authorization': api_key}
response = requests.post(mobsf_server + '/api/v1/upload', data=multipart_data, headers=headers)
print("Uploaded file")
print(response.text)

# get result from mobsf
# output to excel