from datetime import datetime


YEAR_OF_CREATION_WINERY: int = 1920


def year_with_article(year: int) -> str:
    """
    Возвращает слово "год" в зависимости от количества лет
    Пример:
        1 год
        5 лет
        103 года
    """
    if year in range(5, 20) or \
            year % 10 == 0 or \
            year % 10 in range(5, 20) or \
            year % 100 in range(5, 20):
        return f'{year} лет'
    if year % 10 in range(2, 5):
        return f'{year} года'
    return f'{year} год'


current_year: int = datetime.now().year
winery_age = current_year - YEAR_OF_CREATION_WINERY
current_year_winery = year_with_article(year=winery_age)
