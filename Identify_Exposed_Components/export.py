import xml.etree.ElementTree as ET
import argparse
import time
import os
import shutil

parser = argparse.ArgumentParser(description="Integrate system app's odex file into apk")
parser.add_argument("-p", required=True, type=str, help="Path to the System APKs folder")

args = parser.parse_args()
sys_path = args.p

# create txt file
result_file = open("result.txt","w+")

# populate file with exported activities, receivers, providers, services
temp_folder = "temp/"
for r, d, f in os.walk(sys_path):
	for file in f:
		apk_path = os.path.join(r, file)
		result_file.write(file + ":\n")
		apktools_disassemble = "java -jar ../Tools/apktool_2.4.1.jar d " + apk_path + " -o " + temp_folder
		os.system(apktools_disassemble)
		tree = ET.parse(temp_folder + "AndroidManifest.xml")
		root = tree.getroot()

		# get exported activities
		act_result = []
		for child in root.iter("activity"):
			if child.get("{http://schemas.android.com/apk/res/android}exported") == "true":
				act_result.append(child.get("{http://schemas.android.com/apk/res/android}name"))
			elif child.get("{http://schemas.android.com/apk/res/android}exported") == None:
				# check if it has filters
				if len(child.findall("intent-filter")) > 0:
					act_result.append(child.get("{http://schemas.android.com/apk/res/android}name"))

		# get exported receivers
		rec_result = []
		for child in root.iter("receiver"):
			if child.get("{http://schemas.android.com/apk/res/android}exported") == "true":
				rec_result.append(child.get("{http://schemas.android.com/apk/res/android}name"))
			elif child.get("{http://schemas.android.com/apk/res/android}exported") == None:
				# check if it has filters
				if len(child.findall("intent-filter")) > 0:
					rec_result.append(child.get("{http://schemas.android.com/apk/res/android}name"))

		# get exported services
		svc_result = []
		for child in root.iter("service"):
			if child.get("{http://schemas.android.com/apk/res/android}exported") == "true":
				svc_result.append(child.get("{http://schemas.android.com/apk/res/android}name"))
			elif child.get("{http://schemas.android.com/apk/res/android}exported") == None:
				# check if it has filters
				if len(child.findall("intent-filter")) > 0:
					svc_result.append(child.get("{http://schemas.android.com/apk/res/android}name"))

		# get exported providers
		prv_result = []
		for child in root.iter("provider"):
			if child.get("{http://schemas.android.com/apk/res/android}exported") == "true":
				prv_result.append(child.get("{http://schemas.android.com/apk/res/android}name"))
			elif child.get("{http://schemas.android.com/apk/res/android}exported") == None:
				# check if it has filters
				if len(child.findall("intent-filter")) > 0:
					prv_result.append(child.get("{http://schemas.android.com/apk/res/android}name"))

		result_file.write("activities: " + ", ".join(act_result) + "\n")
		result_file.write("receivers: " + ", ".join(rec_result) + "\n")
		result_file.write("services: " + ", ".join(svc_result) + "\n")
		result_file.write("providers: " + ", ".join(prv_result) + "\n\n")
		shutil.rmtree(temp_folder)
result_file.close() 
