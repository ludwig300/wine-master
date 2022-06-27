from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import collections


def get_write_year(year):
    count = year % 100
    if count >= 5 and count <= 20:
        text = 'лет'
    else:
        count = count % 10
        if count == 1:
            text = 'год'
        elif count >= 2 and count <= 4:
            text = 'года'
        else:
            text = 'лет'
    return text


def get_sorted_products(products, category_list):
    product_dict = collections.defaultdict(list)
    for num in range(len(category_list)):
        product_dict[category_list[num]].append(products[num])
    return product_dict


def main():
    excel_data_df = pandas.read_excel(
        'wine3.xlsx',
        sheet_name='Лист1',
        na_values=['None'], keep_default_na=False
    )
    products = excel_data_df.to_dict(orient='record')
    columns_list = excel_data_df.columns.ravel()
    category_list = excel_data_df[columns_list[0]].tolist()
    product_dict = get_sorted_products(products, category_list)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    now = datetime.datetime.now()
    date_since = datetime.datetime(year=1920, month=1, day=1, hour=0)
    passed_years = now.year - date_since.year
    text_years = get_write_year(passed_years)
    rendered_page = template.render(
        product_dict=product_dict,
        passed_years=passed_years,
        text_years=text_years)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
