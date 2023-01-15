from pymongo import MongoClient

client = MongoClient()
db = client.herba4life


def save_product(name, description, price, reference, image_url, language, product_url):
    product_info = {
        'name': name,
        'description': description,
        'price': price,
        'reference': reference,
        'language': language,
        'image_url': image_url,
        'product_url': product_url
    }
    collection = db.products
    collection.insert_one(product_info)


def save_category(name, description, language, category_url):
    category_info = {
        'name': name,
        'description': description,
        'language': language,
        'category_url': category_url
    }
    collection = db.categories
    collection.insert_one(category_info)


def get_all_products():
    collection = db.products
    return list(collection.find())


def remove_all_products():
    collection = db.products
    collection.delete_many({})


def get_all_categories():
    collection = db.categories
    return list(collection.find())


def remove_all_categories():
    collection = db.categories
    collection.delete_many({})
