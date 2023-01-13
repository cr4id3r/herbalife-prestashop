from bs4 import BeautifulSoup


def process_page(page_url, page_html):
    # Open html string with bs4
    soup = BeautifulSoup(page_html, 'html.parser')

    # Check if exists class product-detail
    if soup.find_all(class_='product-detail'):

        # Get product name
        product_name = soup.select_one('.information.product-container h1').text

        # Get product reference
        product_reference = soup.select_one('.information.product-container .sku').text
        product_reference = product_reference.replace('Ref ', '').replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')

        # Get product price
        product_price = soup.select_one('.information.product-container .price').text
        product_price = ''.join([i for i in product_price if i.isdigit() or i == '.' or i == ','])

        # Get product description
        product_description = soup.select_one('#product-overview').text

        # Print product info
        print('Product name: ', product_name)
        print('Product price: ', product_price)
        print('Product reference: ', product_reference)
        #print('Product description: ', product_description)
        #print('Product image: ', product_image)
        print('Product url: ', page_url)
