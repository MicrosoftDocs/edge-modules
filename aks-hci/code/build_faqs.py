'''
Build FAQ for AKS HCI
2021.10.28

'''

import json
import pandas as pd
import mod_utilities as MU

def get_config():
  '''Get the config file and return config dict'''
  with open("config.json", "r") as read_file:
    config = json.load(read_file)
  return config

def make_faq_dict(data_csv):
  '''With the path to a CSV file, return a dictionary with the yaml files.'''
  data = pd.read_csv(data_csv)
  active_items = data.loc[(data['status'] == 'Active')]
  active_items.sort_values(by=['document'])
  docs = set(active_items['document'].tolist())

  yaml_faqs = {}
  for d in docs:
      file_name = "{}.yml".format(d)
      print("===\n{}\n".format(file_name))
      file_body = ""
      doc_rows = active_items.loc[(data['document'] == d)]
      doc_rows.sort_values(by=['section'])
      sections = set(active_items['section'].tolist())
      for s in sections:
          file_body += "  - name: {}\n    questions:\n".format(s)
          lines = doc_rows.loc[(data['section'] == s)]
          for idx, row in lines.iterrows():
              file_body += "    - question: {}\n".format(row["question"])
              file_body += "      answer: | \n        {}\n".format(row["answer"])
              topic_title = row["title"]
              topic_description = row["description"]
              topic_summary = row['summary']
      header = '''
### YamlMime:FAQ
metadata:
  title: {} 
  description: "{}"

title: {} 
summary: |
  {}

sections:
'''.format(topic_title, topic_description, topic_title, topic_summary)
      footer = '''

additionalContent: |
  ## In Conclusion 
  Here's some optional text that can be placed at the end of the document.'''
      full_body = header + file_body + footer
      yaml_faqs[file_name] = full_body
  return yaml_faqs


def generate_faqs(yml_dict, outputpath):
  ''''''
  list_of_file = yml_dict.keys()
  for i in list_of_file:
    full_path = str(outputpath) + i
    MU.write_text(yml_dict[i], full_path)


def main():
    ''' Parse the include modules and create a report.'''

    config = get_config()
    faq_dict = make_faq_dict(config["datafile"])
    generate_faqs(faq_dict, config["output"])


if __name__ == "__main__":
    main()