from xml.etree import ElementTree as ET
import argparse


def parse_xml(xml_from_page):
    # Create ElementTree object
    xml_tree = ET.parse(xml_from_page.raw)
    # Get root of XML tree
    xml_root = xml_tree.getroot()
    currencies = {}
    # Find in tree rates
    for item in xml_root:
        for subitem in item:
            for subsubitem in subitem:
                currencies[subsubitem.attrib['currency']] = subsubitem.attrib['rate']
    currencies['EUR'] = float(1)

    return currencies


def parse_arg():
    arg_parser = argparse.ArgumentParser(description='Currency converter')
    arg_parser.add_argument('--amount', required=True, help='Amount of money to convert', type=float)
    arg_parser.add_argument('--input_currency', required=True, help='Currency you have, 3 letters name or symbol')
    arg_parser.add_argument('--output_currency', help='Currency you want, 3 letters name or symbol', default='all')

    args = arg_parser.parse_args()

    return vars(args)

