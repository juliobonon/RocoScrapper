import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import difflib


def WhatsAppBot(result):
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=D:\Python\Memory\WebWhatsAppBot")
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)

    driver.find_element_by_xpath('//*[@title="N lembro minha conta bfo"]').click()
    time.sleep(3)
    chat = driver.find_element_by_class_name('_1Plpp')
    chat.send_keys(result)
    time.sleep(3)
    driver.find_elements_by_xpath("//span[@data-icon='send']")

    time.sleep(10)
    driver.quit()


def swapFiles(result_text):
    arquivo_atual = open('notes.txt', 'w')
    arquivo_atual.write(result_text)
    arquivo_atual.close()

def difFiles():
    text1 = open("sample1.txt").readlines()
    text2 = open("sample2.txt").readlines()
    result = ''

    for line in difflib.unified_diff(text1, text2):
        result = result + line
    
    return result

url = 'https://twitter.com/RogueCompany'
 
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]

result = []
result2 = []
result_text = ''

for twit in tweets:
    if ("key" in twit):
        result.append(twit)
        result_text = result_text + twit


arquivo_novo = open("notes_novo.txt", "w")
arquivo_novo.write(result_text)
arquivo_novo.close()

arquivo_novo = open("notes_novo.txt", "r")
compare = arquivo_novo.read()
arquivo_novo.close()


arquivo_atual = open('notes.txt', 'r')
compare2 = arquivo_atual.read()
arquivo_atual.close()


if compare == compare2:
    print("Arquivos iguais")
else:
    result = difFiles()
    WhatsAppBot(result)
    swapFiles(result_text)

    