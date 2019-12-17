import logging
import requests


def get_xml():
    logging.basicConfig(filename='.log', format='%(asctime)s - %(levelname)s - %(message)s')
    # URL of Europen Central Bank , XML of rates to Euro, updated every day around 16:00 CET
    URL = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'
    # Get response
    try:
        xml_from_page = requests.get(URL, stream=True)
    except requests.ConnectionError:
        logging.error('Connection error')
        raise ConnectionError('Cannot connect to server')
    except requests.Timeout:
        logging.error('Timeout error')
        raise TimeoutError('No response from server')
    # Check response code from server
    if xml_from_page.status_code != 200:
        logging.error('Not successful response from ECB. Status code: %s', xml_from_page.status_code)
        raise ResourceWarning('Not successful response from server with code {}'.format(xml_from_page.status_code))

    return xml_from_page
