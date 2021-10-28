'''Unit Tests for Build FAQS
2021.10.28'''

import build_faqs as FQ
import yaml

config = FQ.get_config()

def test_assert_make_faq_dict():
    '''Check that the right number of files are generated.'''
    faq_dict = FQ.make_faq_dict(config["testfile"])
    list_of_file = faq_dict.keys()
    assert len(list_of_file) == 2

def test_generate_faqs():
    '''Check a valid yml file is generated with the correct title.'''
    faq_dict = FQ.make_faq_dict(config["testfile"])
    FQ.generate_faqs(faq_dict, config["testout"])
    with open(r"C:\git\ms\edge-modules\aks-hci\code\testdata\one.yml", "r") as read_file:
        yaml_content = yaml.load(read_file, Loader=yaml.FullLoader)
    assert yaml_content["title"] == "Microsoft commercial marketplace publisher FAQ"