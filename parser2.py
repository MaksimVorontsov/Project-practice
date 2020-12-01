from bs4 import BeautifulSoup
from urllib.request import *

url = 'https://otkritkiok.ru/prazdniki/'
host = 'https://otkritkiok.ru/'
def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html
def main():
    for m in range(1,13):
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
        celebration = []
        list = soup.find_all(class_='timeline__one-day timeline__one-day_margin')
        counter = 0
        for a  in list:
            #print(a)
            days.append(a.find('div', class_='timeline__number').get_text())
            if m < 10:
                if int(days[counter]) < 10:
                    celebration.append('0'+ str(m) + '-' + '0' + days[counter])
                else:
                    celebration.append('0' + str(m) + '-' + days[counter])
            else:
                if int(days[counter]) < 10:
                    celebration.append(str(m) + '-' + '0' + days[counter])
                else:
                    celebration.append(str(m) + '-' + days[counter])
            counter = counter + 1

        print(month_name+'=')
        print(celebration)
        #print(box_list)
        #print(name)
        #print(days)
main()