import requests as requests
import xml.etree.ElementTree as ET

import xmltodict as xmltodict

from src.PrestashopAPI.models import Product


class PrestaShopConnection:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.session = requests.Session()

    def perform_request(self, method, url, data=None, is_xml=False):
        target_endpoint = self.url + '/api/' + url
        headers = {}
        if is_xml:
            headers['Content-Type'] = 'application/xml'

        response = self.session.request(method, target_endpoint, data=data, auth=(self.key, ''), headers=headers)
        xml_parsed = xmltodict.parse(response.content)

        return xml_parsed

    def get_all_products(self):
        all_products = []
        response = self.perform_request('GET', 'products')
        if response.get('prestashop'):
            for product_element in response['prestashop']['products']['product']:
                product_info = self.get_product_info(product_element['@id'])
                all_products.append(product_info)

        return all_products

    def get_product_info(self, product_id):
        response = self.perform_request('GET', 'products/' + product_id)
        return response['prestashop']['product']

    def get_product_schema(self, to_dict=True):
        schema = self.perform_request('GET', 'products?schema=blank')
        if to_dict:
            return schema

        return xmltodict.unparse(schema)

    def add_product(self, product_model):
        xml_data = product_model.get_xml(self)
        xml_string = xmltodict.unparse(xml_data)
        response = self.perform_request('POST', 'products', data=xml_string)
        print(response)


if __name__ == '__main__':
    connection = PrestaShopConnection('http://localhost:8080', 'DMEVDCHDY1F7BGPBM7IQNJ7XFMZJCPIJ')
    t = Product()
    t.set_name('nombre test', 1)
    t.set_description('description test', 1)
    connection.add_product(t)
