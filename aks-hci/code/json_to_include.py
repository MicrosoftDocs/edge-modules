'''
Script to create a table from a JSON configuration file.

2022.3.7

'''

import json
from datetime import datetime

THISDATE = str(datetime.now().strftime("%m/%d/%Y"))

outpath = r"C:\git\ms\azure-stack-docs-pr\azure-stack\includes\hci-connectivity-reqs.md"

def write_text(outbody, path):
    '''Write text file to the path.'''
    out_file = open(path, "w")
    for line in outbody:
        out_file.write(line)
    out_file.close()



metadata_slug = '''---
author: mattbriggs
ms.author: mabrigg
ms.service: azure-stack
ms.topic: include
ms.date: {}
ms.reviewer: abha
ms.lastreviewed: {}

# Created from build at the repo: edge modules

---

'''.format(THISDATE, THISDATE)

def main():
    '''
    '''
    tables = json.load(open('./json_to_include_config.json', 'r'))
    for i in tables["tables"]:
        print("Building: {}".format(i["source"]))
        try:
            table_json = json.load(open(i["source"], 'r'))
            headings = table_json[0].keys()
            header = "| "
            table_def = "| "
            for h in headings:
                header += " {} |".format(h)
                table_def += " :---|"
            header += "\n"
            table_def += "\n"
            rows = ""
            for r in table_json:
                row_string = "| "
                for s in headings:
                    row_string += " {} |".format(r[s])
                row_string += "\n"
                rows += row_string
            out_table = metadata_slug + header + table_def + rows
            write_text(out_table, i["target"])
        except Exception as e:
            print("An error occurred when generating {}. Error: {}".format(i["source"], e))

if __name__ == "__main__":
    main()