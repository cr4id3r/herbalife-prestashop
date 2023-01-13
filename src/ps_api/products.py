from prestapyt import PrestaShopWebService

KEY = 'RTPXKUQGENJFV8XL1EJX1Y41DUICVMYK' #Insert your API Key here
SHOP_API_ENDPOINT = 'http://localhost:8080/api'

connection = PrestaShopWebService(SHOP_API_ENDPOINT, KEY)

def add_product():
    prestashop = PrestaShopWebService(SHOP_API_ENDPOINT, KEY)


def get_all_products():
    prestashop = connection.get('products')
    print(prestashop)


if __name__ == '__main__':
    get_all_products()
