from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.kabum.com.br/")
navegador.find_element('xpath', '//*[@id="input-busca"]')\
    .send_keys("Placa De Vídeo Palit Geforce RTX 3070 Gamerock, 8GB, GDDR6")
navegador.find_element('xpath', '//*[@id="barraBuscaKabum"]/div/form/button').click()
navegador.find_element('xpath', '//*[@id="listing"]/div[3]/div/div[2]/div/main/div/div[2]/div[2]/button').click()
sleep(2)
preco = navegador.find_element('xpath', "//*[@class='discountPrice']")
print(preco.text)
