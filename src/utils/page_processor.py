from bs4 import BeautifulSoup

from src.mysql_connection.mysql_utils import save_category, save_product


def process_page(page_url, page_html):
    # Open html string with bs4
    soup = BeautifulSoup(page_html, 'html.parser')

    # Check if its a category
    found_elements = soup.find_all('a', {'class': 'cmp-teaser__title-link'})
    if len(found_elements) == 1:
        process_category(page_url, soup)
        return

    # Check if exists class product-detail
    if soup.find_all(class_='product-detail'):
        process_product(page_url, soup)
        return


def process_category(page_url, soup):
    category_name = soup.select_one('.cmp-teaser__title-link').text
    category_description = soup.select_one('.cmp-teaser__description').text
    category_image_url = soup.select_one('.cmp-image .cmp-image__image').get('src')
    html_lang = soup.html.get('lang')

    save_category(category_name, category_description, html_lang, page_url, category_image_url)


def process_product(page_url, soup):
    # Get product name
    product_name = soup.select_one('.information.product-container h1').text

    # Get product reference
    product_reference = soup.select_one('.information.product-container .sku').text
    product_reference = product_reference.replace('\n', '').replace('\r', '').strip()
    product_reference = product_reference.split(" ")[1]

    # Get product price
    product_price = soup.select_one('.information.product-container .price')
    if product_price:
        product_price = product_price.text
        product_price = ''.join([i for i in product_price if i.isdigit() or i == '.' or i == ','])
    else:
        product_price = '-'

    # Get product description
    product_description = str(soup.select_one('#product-overview'))

    #Product image url
    product_image_url = soup.select_one('.product-detail .information .image img').get('src')

    # Print product info
    save_product(product_name,
                 product_description,
                 product_price,
                 product_reference,
                 product_image_url,
                 soup.html.get('lang'),
                 page_url
                 )
