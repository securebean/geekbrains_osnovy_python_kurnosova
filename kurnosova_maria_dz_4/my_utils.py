import requests
from xmltodict3 import XmlTextToDict


def currency_rates(text):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    doc_dict = XmlTextToDict(response.content, ignore_namespace=True).get_dict()
    course = None
    for i in range(0, len(doc_dict['ValCurs']['Valute'])):
        if text.upper() in doc_dict['ValCurs']['Valute'][i]['CharCode']:
            course = float(doc_dict['ValCurs']['Valute'][i]['Value'].replace(',', '.'))
    return course