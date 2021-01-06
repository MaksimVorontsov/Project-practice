from bs4 import BeautifulSoup
from urllib.request import *
import csv
def create_csv(path):
    url = 'https://otkritkiok.ru/prazdniki/'
    host = 'https://otkritkiok.ru/'
    def get_html(url):
        req = Request(url)
        html = urlopen(req).read()
        return html
    def main():
        cnt = 0
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
            counter = 0
            list = soup.find_all(class_='timeline__one-day timeline__one-day_margin')

            for a  in list:
                #print(a)
                days.append(a.find('div', class_='timeline__number').get_text())
                if m < 10:
                    if int(days[counter]) < 10:
                        date = '0'+ str(m) + '-' + '0' + days[counter]
                    else:
                        date = '0' + str(m) + '-' + days[counter]
                else:
                    if int(days[counter]) < 10:
                        date = str(m) + '-' + '0' + days[counter]
                    else:
                        date = str(m) + '-' + days[counter]
                name = a.find('a', class_="timeline__holidays-name").get_text().replace('\u0306', '')
                counter = counter + 1
                cnt = cnt + 1
                celebration.append({
                    'number': str(cnt - 1),
                    'date': '+' + date + '+',
                    'name': name,
                    'group': 'all_users'
                })
        print(celebration)
    celebration = []
    group = []
    dates = []
    main()
    print(celebration)
    with open(path + 'celebrations.csv', "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['number','date', 'name', 'group'] )
        for line in celebration:
            writer.writerow([line['number'], line['date'], line['name'], line['group']])
    def read_csv(name):#parserchek
        with open(path + name,'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            count = 0
            for row in reader:
                if count == 0:
                    count = count +1
                else:
                    print(row[2])
                    group.append({
                        'date': row[1].replace('+', ''),
                        'list': row[3]
                    })
                    #dates.append(row[1].replace('+', ''))
    read_csv('celebrations.csv')
