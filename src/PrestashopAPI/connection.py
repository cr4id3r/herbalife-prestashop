import requests as requests
import xml.etree.ElementTree as ET

import xmltodict as xmltodict


class PrestaShopConnection:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.session = requests.Session()

    def perform_request(self, method, url, data=None):
        target_endpoint = self.url + '/api/' + url
        print(target_endpoint)
        response = self.session.request(method, target_endpoint, data=data, auth=(self.key, ''))
        xml_parsed = xmltodict.parse(response.content)

        return xml_parsed

    def get_all_products(self):
        response = self.perform_request('GET', 'products')
        if response.get('prestashop'):
            for product_element in response['prestashop']['products']['product']:
                product_info = self.get_product_info(product_element['@id'])
                print(product_info)

    def get_product_info(self, product_id):
        response = self.perform_request('GET', 'products/' + product_id)
        return response['prestashop']['product']

    def get_product_schema(self):
        schema = self.perform_request('GET', 'products?schema=blank')
        print(schema)

        print(xmltodict.unparse(schema))

    def add_product(self, product):
        self.get_product_schema()



if __name__ == '__main__':
    connection = PrestaShopConnection('http://localhost:8080', 'DMEVDCHDY1F7BGPBM7IQNJ7XFMZJCPIJ').get_product_schema()