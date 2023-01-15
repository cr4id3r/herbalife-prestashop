from prestapyt import PrestaShopWebService

KEY = 'CETCXX3BI33HZTB7AK27NM9YYG5WZPH9' #Insert your API Key here
SHOP_API_ENDPOINT = 'http://localhost:8080/api/'

prestashop = PrestaShopWebService(SHOP_API_ENDPOINT, KEY)

def add_product(product_model):
    product = prestashop.add('products', product_model)
    print(product)

def get_all_products():
    products = prestashop.get('products')
    print(products)


if __name__ == '__main__':
    get_all_products()
