import argparse
import os

parser = argparse.ArgumentParser(description='scan through all apks and produce excel output')
parser.add_argument("-p", default=1, required=True, type=str, help="Path to the APK folder")

args = parser.parse_args()
path = args.p

# compile list of apk paths
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.apk' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)

# for every apk path, send to mobsf
# get result from mobsf
# output to excel