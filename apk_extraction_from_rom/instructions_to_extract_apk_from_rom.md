# Extracting Apk from Android ROM
First download the firmware from the OEM (original equipment manufacturer)

Here is what is inside the zip file

<img src="/images/unzip_rom.png" width="400"/>

Using [sdat2img.py](https://github.com/xpirt/sdat2img/blob/master/sdat2img.py), you can unzip the system.new.dat file into a system.img file

<img src="/images/convert_to_system_img.png" width="400"/>

After, you have to mount the newly created system.img file into an output folder

<img src="/images/mount_system_img.png" width="400"/>


You have successfully unzipped an android rom

<img src="/images/rom_apk_files.png" width="400"/>
