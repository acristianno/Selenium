import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.hackthissite.org/")
login = navegador.find_element('xpath', '//*[@id="innerlogin"]/p[1]/input')
login.send_keys("Ratatouli")
senha = navegador.find_element('xpath', '//*[@id="innerlogin"]/p[2]/input')
senha.send_keys("cocofresco@123")
navegador.find_element('xpath', '//*[@id="innerlogin"]/p[3]/input').click()
time.sleep(2)
