from bs4 import BeautifulSoup
from urllib.request import *
import os
def download_celebrations(path):
    os.mkdir(path + 'dates')
    path_new = path + 'dates\\'
    url = 'https://otkritkiok.ru/prazdniki/'
    host = 'https://otkritkiok.ru/'
    def get_html(url):
        req = Request(url)
        html = urlopen(req).read()
        return html
    def main():
        for m in range(1, 13):
            if m == 1:
                month_name = 'january'
            if m == 2:
                month_name = 'february'
            if m == 3:
                month_name = 'march'
            if m == 4:
                month_name = 'april'
            if m == 5:
                month_name = 'may'
            if m == 6:
                month_name = 'june'
            if m == 7:
                month_name = 'july'
            if m == 8:
                month_name = 'august'
            if m == 9:
                month_name = 'september'
            if m == 10:
                month_name = 'october'
            if m == 11:
                month_name = 'november'
            if m == 12:
                month_name = 'december'
            opener = build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            install_opener(opener)
            html = get_html(url + month_name)
            soup = BeautifulSoup(html, 'html.parser')
            days = []
            list = soup.find_all(class_='timeline__one-day timeline__one-day_margin')
            counter = 0
            for a  in list:
                days.append(a.find('div', class_='timeline__number').get_text())
                name = a.find('a').get('href')
                secondary_html = get_html(host+name)
                secondary_soup = BeautifulSoup(secondary_html, 'html.parser')
                try:
                    box = secondary_soup.find(class_='grid grid_col_2 grid_col_sm_3 grid_col_md_3 grid_col_lg_4 grid_gap_medium inner-box inner-box_position').find(class_='postcard-snippet__link').get('href')
                except AttributeError:
                    box = secondary_soup.find(class_='grid grid_col_1 grid_col_sm_2 grid_col_md_3 grid_col_lg_3 grid_gap_medium inner-box inner-box_position').find(class_='postcard-snippet__link').get('href')

                tertiary_html = get_html(host+box)
                tertiary_soup = BeautifulSoup(tertiary_html, 'html.parser')
                pic = tertiary_soup.find(class_='image__preloader loaded').find(class_='image__postcard').get('src')
                print(pic)
                chars = len(pic) - 4
                if m < 10:
                    if int(days[counter]) < 10:
                        urlretrieve(pic, path_new +'0'+ str(m) + '-' + '0' + days[counter] + pic[chars:])
                    else:
                        urlretrieve(pic, path_new + '0' + str(m) + '-' + days[counter] + pic[chars:])
                else:
                    if int(days[counter]) < 10:
                        urlretrieve(pic,
                                    path_new + str(m) + '-' + '0' + days[counter] + pic[chars:])
                    else:
                        urlretrieve(pic,
                                    path_new + str(m) + '-' + days[counter] + pic[chars:])
                counter = counter + 1

                print(days)
                print('\n')
    main()
