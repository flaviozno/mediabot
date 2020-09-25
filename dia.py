from selenium import webdriver
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyautogui as pg

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
time.sleep(5)
contatos = ['']#nome da pessoa TEM QUE SER IDENTICO AO CONTATO

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"DP7CM")]')
    campo_pesquisa.click()
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"_3mR1z")]')
    campo_pesquisa.click()
    #campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"_3HPyS _1e77x")]')
    #campo_pesquisa.click()
    pg.moveTo(1000,300)#vai variar de acordo com a resolução 1360x768
    time.sleep(5)
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"_1Rzv6")]')
    campo_pesquisa.click()
    time.sleep(7)
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@title,"Download")]')#baixou primeria
    campo_pesquisa.click()
    for fotos in range(10): #quantas fotos quer baixar
        campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"_2UGa7 djOrh _3y5oW")]') #foi para o lado
        campo_pesquisa.click()
        time.sleep(1)
        campo_pesquisa = driver.find_element_by_xpath('//div[contains(@title,"Download")]')
        campo_pesquisa.click()


for contato in contatos:
    buscar_contato(contato)

driver.close()