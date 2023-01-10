from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
site = "https://www.google.com/flights?hl=pt-BR"
navegador.get(site)
#cidade_ida = navegador.find_element('xpath', "//*[@class='II2One j0Ppje zmMKJ LbIaRd']")
#cidade_ida.send_keys("Foz do Iguaçu")
navegador.find_element('xpath', "//*[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc nCP5yc AjY5Oe LQeN7 TUT4y']").click()
cidade_destino = navegador.find_element('xpath', "//*[@class='II2One j0Ppje zmMKJ LbIaRd']/[2]")
sleep(2)
