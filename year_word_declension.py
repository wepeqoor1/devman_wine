from datetime import datetime


YEAR_OF_CREATION_WINERY: int = 1920


def get_year_with_article() -> str:
    current_year: int = datetime.now().year
    winery_age = current_year - YEAR_OF_CREATION_WINERY
    """
    Возвращает слово "год" в зависимости от количества лет
    Пример:
        1 год
        5 лет
        103 года
    """
    if winery_age in range(5, 20) or \
            winery_age % 10 == 0 or \
            winery_age % 10 in range(5, 20) or \
            winery_age % 100 in range(5, 20):
        return f'{winery_age} лет'
    if winery_age % 10 in range(2, 5):
        return f'{winery_age} года'
    return f'{winery_age} год'
