from datetime import datetime

# 1 год
# 2-4 года
# 5-20 лет


def year_with_article(year: int) -> str:

    if year in range(5, 20) or \
            year % 10 == 0 or \
            year % 10 in range(5, 20) or \
            year % 100 in range(5, 20):
        return f'{year} лет'
    if year % 10 in range(2, 5):
        return f'{year} года'
    return f'{year} год'


YEAR_OF_CREATION_WINERY: int = 1910

current_year: int = datetime.now().year
winery_age = current_year - YEAR_OF_CREATION_WINERY
current_year_winery = year_with_article(year=winery_age)
print(current_year_winery)
