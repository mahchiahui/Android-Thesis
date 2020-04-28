# Export APK from data without root

Without root, an analyst is not able to list the folder in /data/data which is where most user apps reside in. However, as the permissions on that directory are rwxrwx--x, an analyst can access it, however lack the read permission, which means the analyst is not able to get a listing of its contents. An analyst is able to retrieve the apk by doing the following steps.

## Steps

Download [android platform tools](https://developer.android.com/studio/releases/platform-tools)


Use adb in the platform tools to list the packages in the android device

```bash
./adb shell pm list packages -f
```

A result similar to this should appear

<img src="/images/pm_list_packages.png" width="1000"/>

the package path is appended after "package:". To pull the package use the following command:

```bash
./adb pull <package path>
```

It should look something like this

```bash
./adb pull /data/app/com.huawei.android.thememanager-H6fstsWIRDXXVzwQ-IAGWw==/
```

Rinse and repeat for any other apk