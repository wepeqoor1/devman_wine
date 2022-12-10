from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from year_word_declension import current_year_winery
from read_data_from_excel import get_assortment_wines

from exceptions import ToManyXlsxFilesException


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        current_year_winery=current_year_winery,
        wines_assortment=get_assortment_wines(),
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
# 127.0.0.1:8000/index.html


if __name__ == '__main__':
    try:
        main()
    except ToManyXlsxFilesException:
        print('Файл формата ".xlsx" должен быть равен одному')
