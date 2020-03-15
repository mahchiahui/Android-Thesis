# Scan.py

Scan is a python script that analyzes the extracted apks with MobSF's API. It creates an excel file with the filename, permissions requested and the manifest analysis. The goal of this script is to assist an analyst in identifying suspicious apks.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies for Scan.py.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scan.py -p <path to extracted apks> -api <mobsf api key> -url <url mobsf is hosted on E.g. http://127.0.0.1:8000>
```

## Example

Mount the ROM
<img src="/images/extract_rom.png" width="400"/>

Identify the System app folders
<img src="/images/preinstalled_apps.png" width="400"/>

Run scan.py
<img src="/images/scan_usage.png" width="400"/>

Get output
<img src="/images/output.png" width="400"/>

excel file
<img src="/images/output_results.png" width="400"/>
