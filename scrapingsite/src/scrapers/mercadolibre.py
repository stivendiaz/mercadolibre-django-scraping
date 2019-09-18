import re

from requests import get
from bs4 import BeautifulSoup as soup


class ProductsParser:
    def __init__(self, tree, schema):
        self.tree = tree
        self.schema = schema

    def parse(self):
        return { 'title': self.getTitle(),'price':self.getPrice(),'selling_number':self.getSellingNumber(),'shipment':self.getShipment()}

    def getTitle(self):

        try:
            title = self.tree.select_one(self.schema['title'])
            return title.string
        except:
            return None


    def getShipment(self):
        try:
            img = self.tree.select_one(self.schema['shipment'])
            return img.string
        except:
            return None

    def getSellingNumber(self):
        try:
            selling = self.tree.select_one(self.schema['selling_number'])
            return selling.string
        except:
            return None

    def getPrice(self):
        try:
            price = self.tree.select_one(self.schema['price'])
            return re.sub('\\.','',price.string)
        except:
            return None


def getHtml(url):
    response = get(url)
    return response.text


def getParser(html):
    return soup(html, 'html.parser')

def getProducts(parser, schema):
    return parser.select(schema['discriminator'])

def scrap(schema):
    product_list = []
    html = getHtml(schema['url'])
    # Limitate pagination
    parser = getParser(html)
    for tree in getProducts(parser, schema):
        productsParser = ProductsParser(tree, schema)
        product_list.append(productsParser.parse())
    return product_list


def callScrap(search_value):
    schema = {
        'url': 'https://listado.mercadolibre.com.co/' + re.sub(' ','-',search_value),
        'discriminator': 'li.results-item',
        'title': 'div > h2 > a > span',
        'price' : 'span.price__fraction ',
        'selling_number': 'div.stack_column_item.status > div > div',
        'shipment': 'div.item__info-container.highlighted > div > div.item__stack_column.highlighted > div > div.stack_column_item.shipping.highlighted > div > p',
    }
    print(schema['url'])
    return(scrap(schema))
