import argparse
import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_write_year(year):
    count = year % 100
    text = 'лет'
    if count >= 5 and count <= 20:
        return text
    count = count % 10
    text = 'год'
    if count == 1:
        return text
    text = 'года'
    return text


def get_sorted_products(products, categories):
    sorted_products = collections.defaultdict(list)
    for num in range(len(products)):
        sorted_products[categories[num]].append(products[num])
    return sorted_products


def create_parser():
    parser = argparse.ArgumentParser(description='Run Web-server')
    parser.add_argument(
        '-p', '--path',
        default='catalog.xlsx', help='Path to ".xlsx"'
    )
    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    excel_data_df = pandas.read_excel(
        namespace.path,
        sheet_name='Лист1',
        na_values=['None'], keep_default_na=False
    )
    products = excel_data_df.to_dict(orient='record')
    columns = excel_data_df.columns.ravel()
    categories = excel_data_df[columns[0]].tolist()
    sorted_products = get_sorted_products(products, categories)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    now = datetime.datetime.now()
    foundation_year = 1920
    winery_age = now.year - foundation_year
    years_text = get_write_year(winery_age)
    rendered_page = template.render(
        products=sorted_products,
        passed_years=winery_age,
        years_text=years_text)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
