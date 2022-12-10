import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from read_data_from_excel import get_assortment_wines

from exceptions import ToManyXlsxFilesException
from year_word_declension import get_year_with_article


def parsing_console_arguments():
    parser = argparse.ArgumentParser(
        description=(
            """
                Заупск программы:
                `python main.py --file <file.xlsx>`    
            """
        )
    )
    parser.add_argument(
        "--file",
        help="Введите название файла",
    )

    return parser.parse_args()


def main():
    args = parsing_console_arguments()
    xlsx_file = args.file
    try:
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('template.html')
        rendered_page = template.render(
            year_with_article=get_year_with_article(),
            wines_assortment=get_assortment_wines(xlsx_file),
        )
        with open('index.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

        server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
        server.serve_forever()
    except ToManyXlsxFilesException:
        print('Файл формата ".xlsx" должен быть равен одному')


if __name__ == '__main__':
    main()
