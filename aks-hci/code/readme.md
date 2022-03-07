# AKS on Azure Stack Hub Docs Scripts

These scripts are used to generate docs for AkS on HCI.

2022.3.7

## set up the repo
1. Add a `config.json` file based on the example: `config_example.json`. This file has the following attributes:
    1. **datafile**: \<pathto>\\aks-hci-faq.csv
    1. **output**: \<pathtotheoutput>
2. Install Python 3 and then install the requirements:
    ```
    pip install -r requirements.txt
    ```

## Create the known issues

Run the builder script.
```
python build_faqs.py
```

The script will output yaml files using the Google microformat to the target directory.

### Test the script

The test script will use test data and place files in the testdata folder. A validation report will display.

```
pytest --verbose
``

### References

You can find information about the FAQ format which is being used for the known issues at:
https://review.docs.microsoft.com/en-us/help/contribute/contribute-how-to-faq-guide?branch=master

You can find information about Microformats at:
http://microformats.org/

## Create JSON config files to tables

This script will create tables from JSON arrays stored in the config folder.

## Provide feedback

If you find an issue, you can provide feedback at:
https://github.com/MicrosoftDocs/edge-modules/issues
