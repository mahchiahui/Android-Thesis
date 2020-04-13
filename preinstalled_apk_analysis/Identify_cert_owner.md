# Identify certificate owner

By identifying exported activities, analysts can identify possible interfaces that can be exploited by malicious android applications. A script has been written to assist the idenfication of exported activities, services, providers and receivers. The script will output a text file with the exported activities for each apk.

## Usage

Use apktool to decode apk file into a folder

```bash
apktool d -r -s <path to system apk>
```

use keytool to read and print the cert

```bash
keytool -printcert -file <path to system apk folder>/original/META-INF/CERT.RSA
```

you will get an output like this

<img src="/images/keytool.png" width="1000"/>