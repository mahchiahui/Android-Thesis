import argparse
import time
import os
import shutil

parser = argparse.ArgumentParser(description="Integrate system app's odex file into apk")
parser.add_argument("-p", required=True, type=str, help="Path to the System APK folder")
parser.add_argument("-o", required=True, type=str, help="output folder")
parser.add_argument("-f", required=True, type=str, help="framework")

args = parser.parse_args()
sys_path = args.p
output = args.o
framework_path = args.f

def odex_integration(odex_path, framework_path, apk_name, apk_path, output_path):
	
	# convert odex to smali
	temp_folder = "temp"
	baksmali_command = "java -jar ../Tools/baksmali-2.4.0.jar deodex " + odex_path + " -d " + framework_path + " -o " + temp_folder
	os.system(baksmali_command)

	# convert smali to dex
	smali_command = "java -jar ../Tools/smali-2.4.0.jar assemble -o classes.dex " + temp_folder
	os.system(smali_command)
	shutil.rmtree(temp_folder)

	# use apktools to unzip apk
	apktools_disassemble = "java -jar ../Tools/apktool_2.4.1.jar d -s -r " + apk_path + " -o " + temp_folder
	os.system(apktools_disassemble)

	# put classes.dex into apk folder
	os.rename("classes.dex", temp_folder + "/classes.dex")

	# zip up
	apktools_assemble = "java -jar ../Tools/apktool_2.4.1.jar b -o " + apk_name + " " + temp_folder + "/"
	os.system(apktools_assemble)
	shutil.rmtree(temp_folder)

	# output to apk folder
	if not os.path.exists(output_path):
		os.makedirs(output_path)
	os.rename(apk_name, output_path + apk_name)


# compile list of apk paths

# r=root, d=directories, f = files
for r, d, f in os.walk(sys_path):
    for file in f:
        if '.apk' in file:
        	apk_path = os.path.join(r, file)
        	odex_path = ""
        	for rt, dr, fi in os.walk(r):
        		for name in fi:
        			if '.odex' in name:
        				odex_path = os.path.join(rt,name)
        	if not odex_path:
        		print("no odex file")
        		os.rename(apk_path, output + file)
        	else:
        		odex_integration(odex_path, framework_path, file, apk_path, output)
