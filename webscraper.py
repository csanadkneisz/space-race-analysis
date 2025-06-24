import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

BASE_URL = "https://nextspaceflight.com/launches/past/?search="

res = requests.get(BASE_URL)
html_content = res.text
parser = BeautifulSoup(html_content, "html.parser")

# Find the last page number
last_page_btn = parser.select_one('.mdc-button--raised:-soup-contains("last »")')
total_pages = int(last_page_btn.get('href').split('=')[1].split('&')[0])

missions_list = []

for pg in range(1, total_pages + 1):
    page_res = requests.get(f"https://nextspaceflight.com/launches/past/?page={pg}&search=")
    page_html = page_res.text
    page_soup = BeautifulSoup(page_html, "html.parser")

    titles = page_soup.select('h5')
    info_blocks = page_soup.select('.mdl-card__supporting-text')
    detail_links = page_soup.select('.mdc-button:-soup-contains("Details")')

    for idx in range(len(detail_links)):
        detail_href = detail_links[idx].get('href')
        detail_res = requests.get(f"https://nextspaceflight.com{detail_href}")
        detail_html = detail_res.text
        detail_soup = BeautifulSoup(detail_html, "html.parser")

        mission_result = detail_soup.select_one('h6')
        agency = detail_soup.select_one('.a:first-child .mdl-cell:first-child')
        rocket_state = detail_soup.select_one('.a:first-child .mdl-cell:nth-of-type(2)')
        cost_info = detail_soup.select_one('.a:first-child .mdl-cell:nth-of-type(3)')

        date_and_place = info_blocks[idx].get_text(strip=True, separator="#").split('#')

        if cost_info and "$" in cost_info.get_text():
            try:
                cost_amount = float(cost_info.get_text(strip=True).split('$')[1].split(' ')[0])
            except ValueError:
                cost_amount = ""
        else:
            cost_amount = ""

        entry = {
            "Organisation": agency.get_text(strip=True),
            "Location": date_and_place[1],
            "Date": date_and_place[0],
            "Detail": titles[idx].get_text(strip=True),
            "Rocket_Status": rocket_state.get_text(strip=True).split(': ')[1],
            "Price": cost_amount,
            "Mission_Status": mission_result.get_text(strip=True)
        }

        missions_list.append(entry)

df = pd.DataFrame(missions_list)
df.to_csv(f"mission_launches_updated_{date.today()}.csv", index=False)