# Identify exported activities

By identifying exported activities, analysts can identify possible interfaces that can be exploited by malicious android applications. A script has been written to assist the idenfication of exported activities, services, providers and receivers. The script will output a text file with the exported activities for each apk.

## Usage

To run the script, enter the following

```bash
python export.py -p <path to extracted apks>
```

an example of the script being used

```bash
python export.py -p output/
```

