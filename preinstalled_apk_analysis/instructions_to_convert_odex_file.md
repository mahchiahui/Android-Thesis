# Converting odex files to classes.dex

ODEX files are the optimized versions of .DEX files, which contain the executable code for an Android app. Android creates ODEX files for apps before they are run, and they contain the same filename prefix as their corresponding APK file (e.g., MyApp.apk and MyApp.odex). The data in ODEX files replaces data used in the equivalent DEX file (classes.dex) stored inside the APK file. When analyzing preinstalled apks, the actual apk does not contain the typical classes.dex that is found in user-installed apk. The analyst has to convert the odex file to smali, convert that to dex code and then put that classes.dex into the apk.

## Instructions
ADB pull /system/framework and /system/app

<img src="/images/adb_pull.png" width="1000"/>

Download [baksmali-2.4.0.jar](https://bitbucket.org/JesusFreke/smali/downloads/) and use it to convert odex to smali code

<img src="/images/baksmali_decode.png" width="1000"/>

Convert the smali code to a dex file using [smali-2.4.0.jar](https://bitbucket.org/JesusFreke/smali/downloads/)

<img src="/images/convert_to_dex.png" width="1000"/>

Use [Apktool](https://ibotpeaches.github.io/Apktool/install/) to unzip the apk file

<img src="/images/apktool_decode.png" width="1000"/>

Copy the classes.dex file into the decoded apk folder and build the apk with Apktool

<img src="/images/apktool_build.png" width="800"/>
