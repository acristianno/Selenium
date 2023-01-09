import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.youtube.com/watch?v=gx-VVwXB128&ab_channel=CanaldoUcla")
navegador.find_element('xpath', '//*[@id="movie_player"]/div[32]/div[2]/div[1]/button').click()
time.sleep(2)