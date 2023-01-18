from __future__ import print_function
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_cursor():
    cnx = mysql.connector.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME')
    )

    cursor = cnx.cursor()
    return cnx, cursor


def save_product(name, description, price, reference, image_url, language, product_url):
    cnx, cursor = get_cursor()
    add_product = ("INSERT INTO products "
                   "(title, description, price, reference, lang_code, image_url, product_url) "
                   "VALUES (%(name)s, %(description)s, %(price)s, %(reference)s, %(language)s, %(image_url)s, %(product_url)s)")

    product_info = {
        'name': name,
        'description': description,
        'price': price,
        'reference': reference,
        'language': language,
        'image_url': image_url,
        'product_url': product_url
    }

    cursor.execute(add_product, product_info)
    cnx.commit()
    print("Product saved")


def save_category(category_name, category_description, html_lang, page_url, category_image_url):
    cnx, cursor = get_cursor()

    add_category = ("INSERT INTO category "
                    "(name, description, language, category_url) "
                    "VALUES (%(name)s, %(description)s, %(language)s, %(category_url)s)")

    category_info = {
        'name': category_name,
        'description': category_description,
        'language': html_lang,
        'category_url': page_url
    }

    cursor.execute(add_category, category_info)
    cnx.commit()
    print("Category saved")


def get_all_products():
    cnx, cursor = get_cursor()
    query = ("SELECT * FROM products")
    cursor.execute(query)

    field_names = [i[0] for i in cursor.description]
    all_products = []
    for row in cursor:
        all_products.append(dict(zip(field_names, row)))

    return all_products


if __name__ == '__main__':
    all_products = get_all_products()
    print(all_products)