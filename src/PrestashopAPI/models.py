


class Product:
    id = None
    reference = None
    name = None
    description = None

    def set_description(self, description, language_id):
        description_dict = self.description or {}
        description_dict[language_id] = description
        self.description = description_dict

    def set_name(self, name, language_id):
        name_dict = self.name or {}
        name_dict[language_id] = name
        self.name = name_dict

    def get_next_id(self, connection):
        all_products = connection.get_all_products()
        next_id = max([int(product['id']) for product in all_products]) + 1
        return next_id

    def get_xml(self, connection):
        schema = connection.get_product_schema(to_dict=True)
        # schema['prestashop']['product']['id'] = self.id or self.get_next_id(connection)

        # schema['prestashop']['product']['name'] = self.reference or 'test'
        connection.get_all_products()
        if self.name:
            for language_id, text in self.name.items():
                translate_info = {
                    '@id': str(language_id),
                    '@xlink:href': connection.url + '/api/languages/' + str(language_id),
                    '#text': text
                }
                schema['prestashop']['product']['name']['language'] = list(filter(lambda x: x.get('@id') != str(language_id), schema['prestashop']['product']['name']['language']))
                schema['prestashop']['product']['name']['language'].append(translate_info)

        if self.description:
            for language_id, text in self.description.items():
                translate_info = {
                    '@id': str(language_id),
                    '@xlink:href': connection.url + '/api/languages/' + str(language_id),
                    '#text': text
                }

                schema['prestashop']['product']['description']['language'] = list(filter(lambda x: x.get('@id') != str(language_id), schema['prestashop']['product']['description']['language']))
                schema['prestashop']['product']['description']['language'].append(translate_info)

        schema['prestashop']['product']['position_in_category'] = '1'

        return schema
