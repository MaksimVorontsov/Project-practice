import time
import sys
import threading
import random
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidArgumentException as IAE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
##########################################
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\Rachu\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='C:\Python\chromedriver.exe', options=options)
driver.get("https://web.whatsapp.com/")
##########################################
PICPATH = 'C:\\Users\\Rachu\\FilesforBot\\parser2\\'
##########################################(изменяющиеся объекты)
user_name_list = ['110110', 'Миша А']
all_users = ['110110', 'Миша А']
men = ['Миша А']
women = ['110110']
##########################################(Счетчики)
sendmsgcount = []
meme = []
setup_counter = []
randomcount = []
main_counter = []
chek_list = ['']
message_name_1 = ['']
mesflag =[]
current_time_list = []
clock_counter = ['00:10']
##########################################
def read_csv(name, group):#parserchek
    with open('C:\\Users\\Rachu\\PycharmProjects\\BotWhatsApp\\' + name,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        count = 0
        for row in reader:
            if count == 0:
                count = count +1
            else:
                group.append({
                    'date': row[1].replace('+', ''),
                    'list': row[3]
                })
holidays = []
read_csv('celebrations.csv', holidays)
print(holidays)
##########################################
def new_chat(user_name, list = user_name_list):
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_3qx7_"]')))
    new_chat = driver.find_element_by_xpath('//div[@class="_3qx7_"]')
    new_chat.click()

    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="_3FRCZ copyable-text selectable-text"]')))
    new_user = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    new_user.send_keys(user_name)
    time.sleep(1)
    try:
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
        list.remove("{}".format(user_name))
        ###sendpic_count.append('1')
        sendmsgcount.append(1)

    except Exception as e:
        driver.close()
        print(e)
        sys.exit()

def send_message_all(list, mesname): #1-список в котором содежаться имена, 2-сообщение
    for user_name in list:
        send_message(user_name, mesname=mesname, list= list)
def send_message(user_name_arg, mesname, list = user_name_list):
    try:
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name_arg))
        user.click()
    except NoSuchElementException:
        new_chat(user_name_arg, list=list)
        time.sleep(1)
    i = 0
    if len(sendmsgcount) == 0:
        while i < 20:
            try:
                message_box = driver.find_element_by_xpath('//div[@class="_3uMse"]')
                message_box.send_keys(mesname)
                send_button = driver.find_element_by_xpath('//button[@class="_2Ujuu"]')
                send_button.click()
                time.sleep(1)
                i = 40
            except NoSuchElementException:
                pass
                time.sleep(1)
    sendmsgcount.clear()
    user_default = driver.find_element_by_xpath('//span[@title="Waiting_room_for_bot"]')
    user_default.click()
def send_pic_all(list, picname, text = ''):
    for user_name in list:
        send_pic(user_name, picname=picname, text=text)
def send_pic(user_name_arg, picname, text = ''): #без jpg
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(user_name_arg))
    user.click()

    attachment_box = driver.find_element_by_xpath('//div[@title = "Прикрепить"]')
    attachment_box.click()

    path = str(picname)

    imgvid_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    imgvid_box.send_keys(path)
    time.sleep(2)
    if text != '':
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH,
             '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]')))
        comment = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]')
        comment.send_keys(text)
    send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
    send_button.click()
def setup():
    print("Выберите действие: ")
    print("0 - продолжить выполнять работу")
    print("1 - редактирование списка")
    print("2 - изменить время рассылки")
    print("3 - закрыть вкладку и завершить работу программы")
    try:
        start_command = int(input())
        if start_command == 0:
            setup_counter.append('')
        if start_command == 1:
            edit_list()
        if start_command == 2:
            edit_time()
        if start_command == 3:
            setup_counter.append('')
            main_counter.append('')
            driver.close()
        if (start_command > 3) or (start_command < 0):
            print("Нужно ввести число из предложенных")
    except ValueError:
        print("Пожалуйста введите число из списка")
    print("Цикл завершен успешно")
    time.sleep(1)
def edit_list():
    print("0 - Вернуться")
    print("1 - Ввести имя пользователя")
    print("2 - Очистить список")
    print("3 - Удалить пользователя из списка")
    print("4 - Посмотреть список")
    command = int(input())
    try:
        if command == 0:
            print("Возвращаюсь")
        if command == 1:
            print("Введите имя пользователя")
            adduser = input()
            user_name_list.append(adduser)
            if user_name_list.count(adduser) > 1:
                user_name_list.remove(adduser)
                print("Пользователь уже находится в списке")
            print("Пользователь добавлен в список")
        if command == 2:
            user_name_list.clear()
            print("Список очищен")
        if command == 3:
            print("Введите имя пользователя, которого хотите удалить")
            try:
                user_name_list.remove(input())
                print("Пользователь удален")
            except ValueError:
                print("Такого пользователя не было, но это не важно ")
        if command == 4:
            print(user_name_list)
        if (command > 4) or (command < 0):
            print("Нужно написать число из списка")
    except ValueError:
        print("Пожалуйста введите число из списка")
def edit_time():
    print("Введите время рассылки в формате hh:mm:")
    timer= input()
    clock_counter.clear()
    mesflag.clear()
    clock_counter.append(timer)
def sleeper():
    try:
        chek_list.clear()
        chek_list.append('')
        chek = input()
        chek_list.clear()
        chek_list.append(chek)
    except ValueError:
        pass
def clock():
    i = 1
    while i > 0:
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        current_time_list.clear()
        if current_time == clock_counter[0]:
            if len(mesflag) == 0:
                mesflag.append(1)
        elif current_time == "00:00":
            mesflag.clear()
        else:
            current_time_list.append(current_time)
        time.sleep(10)
def chek_for_unseen():
    try:
        unseen = driver.find_element_by_xpath('//div[@class="_2Q3SY"]')
        unseen.click()
        chek_last_message()
        if message_name_1[0].replace('!','') =='Доброе утро' or message_name_1[0] =='доброе утро':
            i = 0
            while i <20:
                message_box1 = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
                message_box1.send_keys("Доброе утрo")
                send_button = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
                send_button.click()
                user_default1 = driver.find_element_by_xpath('//span[@title="Waiting_room_for_bot"]')
                user_default1.click()
                i = 40
        elif message_name_1[0] =='мем' or message_name_1[0] == 'Мем':
            r = 1
            while (r != 0):
                r = 0
                k = random.randint(0, meme[0] - 1)
                for a in randomcount:
                    if a == k:
                        r = 1
            randomcount.append(k)
            print(k)
            print("значение: "+comments[k])
            attachment_box = driver.find_element_by_xpath('//div[@title = "Прикрепить"]')
            attachment_box.click()

            path = str(k) + '.jpg'
            imgvid_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            imgvid_box.send_keys(PICPATH + path)

            if comments[k] != '':
                print("chek2")
                try:
                    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]')))
                    comment = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]')
                    j = 0
                    while j == 0:
                        try:
                            comment.send_keys(comments[k])
                            cross = driver.find_element_by_xpath('//div[@class="_3Jrq3"]')
                            j = j + 1
                        except NoSuchElementException:
                            print('fff')
                            pass
                    print("chek3")
                except TimeoutException:
                    print("TimeoutException")
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')))
            add_files_box2 = driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
            add_files_box2.click()
        else:
            i = 0
            user_default1 = driver.find_element_by_xpath('//span[@title="Waiting_room_for_bot"]')
            user_default1.click()
        user_default = driver.find_element_by_xpath('//span[@title="Waiting_room_for_bot"]')
        user_default.click()
    except NoSuchElementException:
        pass
    except IAE:
        print("No file")
def chek_last_message():
    last_message = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in last_message]
    message_name_1.clear()
    message_name_1.append(msg[-1])
def reader():
    path = 'C:\\Users\\Rachu\\PycharmProjects\\pythonProject4\\'
    with open(path + 'max.txt', 'r') as max:
        intmax = int(max.readline())
        meme.append(intmax)
    with open(path + 'file1.txt', 'r') as f:  # opens file for reading
        for a in range(0,intmax):
            line = f.readline().replace('\n', '').replace('null', '')
            comments.append(line)
def chek_day():
    today = date.today()
    d1 = today.strftime("%m-%d")
    print(d1)
    for element in holidays:
        if element['date'] == d1:
            print(element['list'])
            if element['list'] == 'all_users':
                try:
                    send_pic_all(all_users, PICPATH + d1+'.gif')
                except IAE:
                    try:
                        send_pic_all(all_users, PICPATH + d1 + '.jpg')
                    except IAE:
                        print("Can't find the file, chek if it exists")
            elif element['list'] == 'men':
                try:
                    send_pic_all(men, PICPATH + d1+'.gif')
                except IAE:
                    try:
                        send_pic_all(men, PICPATH + d1 + '.jpg')
                    except IAE:
                        print("Can't find the file, chek if it exists")
            elif element['list'] == 'women':
                try:
                    send_pic_all(women, PICPATH + d1+'.gif')
                except IAE:
                    try:
                        send_pic_all(women, PICPATH + d1 + '.jpg')
                    except IAE:
                        print("Can't find the file, chek if it exists")
            else:
                print("Where is no group with name like that")

WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.XPATH, '//span[@title="Waiting_room_for_bot"]')))
user_default0 = driver.find_element_by_xpath('//span[@title="Waiting_room_for_bot"]')
user_default0.click()

comments = []#reads the file and paste the data
reader()     #

h = threading.Thread(target=clock, daemon=True)###
h.start()                                      ###запускаем часы

print("I'm working(command = setup) :")
while len(main_counter) == 0:
    if threading.active_count() == 2:
        t = threading.Thread(target=sleeper, daemon=True)
        t.start()

    chek_for_unseen()
    if len(mesflag) == 1: ###chek time
        mesflag.append(1)
        chek_day()
    time.sleep(5)
    if chek_list[0] == 'setup':
        print("Переброс на настройки")
        while len(setup_counter) == 0:
            setup()
        chek_list.clear()
        chek_list.append('')
    setup_counter.clear()



