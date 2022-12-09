from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from numpy import append
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import os 


global spisok_slov
spisok_slov = ['Доступ ограничен', 'Ресурс заблокирован', 'МТС']
global spisok_adresovzaglushek
spisok_adresovzaglushek = ['http://warning.rt.ru/',
                           'http://t2-blocked.com/', 'http://blocked.mts.ru/']
global search_text
search_text = ["Доступ к", "ресурсу ограничен", "решению суда", "Единый Реестр",
               "на основании Федерального закона",
               "Об информации, информационных технологиях и о защите информации", "149-ФЗ"]


def nothing():
    pass


def connection_possibility(links, size):
    count1 = 0
    count2 = 0
    list = [[], [], []]
    for j in range(size):
        url = "http://" + links[j]
        req = Request(url)

        try:
            response = urlopen(req)
        except HTTPError as e:
            list[1].append(links[j])
            count1 += 1
        except URLError as e:
            list[1].append(links[j])
            count1 += 1
        else:
            list[2].append(links[j])
            count2 += 1
            filePath = __file__
            dir = os.path.abspath(os.curdir)
            less_filePath = dir + '\telehack\scr\geckodriver.exe'
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(options=options,
                                        executable_path=less_filePath)
            browser.maximize_window()
            browser.get(url)
            sleep(2)
            url1 = url.lstrip(r"https://")
            less_filePath = dir.rstrip('\scr\geckodriver.exe')
            url1 = less_filePath+r'\img'+r'\\' + url1 + r'.png'

            browser.save_screenshot(url1)

            if (url+'\\' != browser.current_url):
                i = 0
                flag1 = 0
                flag2 = 0
                while i < len(spisok_adresovzaglushek):
                    if (browser.current_url == spisok_adresovzaglushek[i]):
                        flag1 = 1
                        break
                    i += 1
                i = 0
                while i < len(spisok_slov):
                    if (browser.title == spisok_slov[i]):
                        flag2 = 1
                        break
                    i += 1
                if (flag1 and flag2):
                    list[1].append(links[j])
                    list[2].pop()
                    count1 += 1
                    count2 -= 1
                else:
                    get_source = browser.page_source
                    get_source = get_source.replace('&nbsp;', ' ')
                    i = 0
                    counter = 0
                    for i in range(0, len(search_text)-1):
                        if (search_text[i] in get_source):
                            counter += 1
                    if (counter >= 2):
                        list[1].append(links[j])
                        list[2].pop()
                        count1 += 1
                        count2 -= 1
        browser.quit()
    list[0].append(count1)
    list[0].append(count2)

    out_list =[[],[],[]]
    out_list[0].append(count1)
    out_list[0].append(count2)
    for i2 in range(0, len(list[2])):
        out_list[1].append(list[2][i2])
    for i2 in range(0, len(list[1])):
        out_list[1].append(list[1][i2])
    
    return out_list
