# Identifying Third-Party Library(TPL) in APK

2 tools that has the capabilities to detect third park libraries in APKs have been identified. It is recommended to use LibScout as it provides a more comprehensive identification of TPL.

## LibScout

LibScout is a light-weight and effective static analysis tool to detect third-party libraries in Android/Java apps. The detection is resilient against common bytecode obfuscation techniques such as identifier renaming or code-based obfuscations such as reflection-based API hiding or control-flow randomization. Further, LibScout is capable of pinpointing exact library versions including versions that contain severe bugs or security issues.

LibScout requires the original library SDKs (compiled .jar/.aar files) to extract library profiles that can be used for detection on Android apps. Pre-generated library profiles are hosted at the repository [LibScout-Profiles](https://github.com/reddr/LibScout-Profiles).

### Setup

Download the latest [release](https://github.com/reddr/LibScout/releases) 

Build the tool.

```bash
./gradlew build
```

move the newly build LibScout.jar to base folder

```bash
mv ~/Downloads/LibScout-2.3.2/build/LibScout-2.3.2.jar ~/Downloads/LibScout-2.3.2/
```

Download the latest [LibScout-Profiles](https://github.com/reddr/LibScout-Profiles/archive/master.zip) and place it in the base folder

Lastly, download the [android sdk jar](https://androidsdkmanager.azurewebsites.net/SDKPlatform) that is used by the the android device. E.g. if the android device uses android version 9, download android sdk 28 jar (android version 9 => API Level 28). Place the android.jar in the lib folder.

Your repo structure should look something like this

<pre><code>
|_ gradlew / gradlew.bat (gradle wrappers to generate runnable LibScout.jar)
|_ assets
|    |_ library.xml (Library meta-data template)
|_ config
|    |_ LibScout.toml (LibScout's config file)
|    |_ logback.xml (log4j configuration file)
|_ data
|    |_ app-version-codes.csv (Google Play app packages with valid version codes)
|_ lib
|    Android.jar
|_ scripts
|    |_ library-specs (pre-defined library specs)
|    |_ library-scraper.py   (scraper for mvn-central, jcenter, custom mvn)
|    |_ library-profile-generator.sh (convenience profile generator)
|_ src
|    source directory of LibScout (de/infsec/tpl). Includes some open-source,
|    third-party code to parse AXML resources / app manifests etc.
|_ LibScout.jar
|
|_ LibScout-Profiles (ready-to-use library profiles for TPL detection)
</code></pre>

### Usage

Use LibScout's match function to identify TPLs used in the APK

```bash
java -jar LibScout-2.3.2.jar -o match -p LibScout-Profiles-master/ -a lib/android.jar <path to APK>
```

This should result in the following output

<img src="/images/LibScout_usage.png" width="1000"/>

## LibRadar

An automatic tool for Android library detection. Its suppose to be fast, accurate and obfuscation-resilient.

### Setup

Download the [latest release](https://github.com/pkumza/LibRadar/releases).

### Usage

Run the following command to start analyzing an APK

```bash
python LibRadar/main/main.py <path to apk>
```

It should produce output that looks something like this

<img src="/images/libradar.png" width="1000"/>