from bs4 import BeautifulSoup
from urllib.request import *
import time
import csv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException

url = 'https://ok.ru/positow'
host = 'https://otkritkiok.ru/'
def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html
def parse():
    driver = webdriver.Chrome(executable_path='C:\Python\chromedriver.exe')
    driver.get('https://ok.ru/positow')
    SCROLL_PAUSE_TIME = 0.5
    i = 0
    while i < 10:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        try:
            more = driver.find_element_by_xpath('//*[@id="feed_feedsPanelGroupSingle"]/div/div/div[2]')
            more.click()
        except ElementClickInterceptedException:
            pass
        except ElementNotInteractableException:
            pass
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        i = i +1
    data = driver.page_source
    driver.save_screenshot('C:\\Drivers\\testing.png')
    #driver.close()
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    soup = BeautifulSoup(data, "html.parser")
    days = []
    list = soup.find_all(class_='feed-w')
    counter = 0
    for a in list:
        counter1 = 0
        try:
            a.find(class_='feed_label').get_text()
        except AttributeError:
            try:
                a.find(class_='media-link_c va_target').get_text()
            except AttributeError:
                try:
                    name = a.find('img',loading='lazy').get('src')
                    name1 = 'https:' + name
                    try:
                        #posts_text.append(
                        text = a.find(class_='media-text_cnt_tx emoji-tx textWrap').get_text().replace(u'\xa0', '').replace(u'\n', '').replace('Продолжение ниже...', '')
                        if len(text) < 120 :
                            posts_text.append(text)
                            counter1 = 1
                        else:
                            counter1 = 2
                    except AttributeError:
                        posts_text.append('null')
                    if counter1 != 2:
                        urlretrieve(name1, 'C:\\Users\\Rachu\\FilesforBot\\parser2\\' + str(counter) + '.jpg')
                        days.append(counter)
                        counter = counter + 1
                except AttributeError:
                    pass

    print("Количество постов:" + str(days[-1]))
    print(posts_text)
def main():
    with open('max.txt', 'w') as max:
        max.write(str(len(posts_text)))
    with open('file1.txt', 'w') as file:
        for i in posts_text:
            file.write(i)
            file.write('\n')
def reader():
    path = 'C:\\Users\\Rachu\\PycharmProjects\\pythonProject4\\'
    with open(path+'max.txt', 'r') as max:
        intmax = int(max.readline())
    with open(path + 'file1.txt', 'r') as f:  # opens file for reading
        for a in range(0,intmax):
            line = f.readline().replace('\n', '').replace('null', '')
            output_text.append(line)
#posts_text = ['null', 'null', 'В мире просто не существует такой коробки, в которую не поместился бы кот', 'null', 'null', 'null', 'Погулял по настоящему!', 'null', 'Это правда!', 'null', 'null', 'Муж поздравил ', 'null', 'null', 'null', 'null']
posts_text = []
output_text = []
print(len(posts_text))
parse()
main()
reader()
print(output_text)

