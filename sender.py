"""Send a message automatically"""
# Tested in Python 3.7.7 64 Bit
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

USERNAME = "Alby7503"
MESSAGE = "Hi!"
TIME = 3
LANGUAGE = "EN"
WORDS = {
    "EN": ["All", "Please log in your account and press enter when ready..."],
    "IT": ["Tutti", "Per favore accedi al tuo account e premi invio quando sei pronto..."],
    "FR": ["Tous", "Veuillez vous connecter à votre compte et appuyez sur Entrée lorsque vous êtes prêt..."],
    "DE": ["Alle", "Bitte melden Sie sich in Ihrem Konto an und drücken Sie die Eingabetaste, wenn Sie bereit sind..."]
}
#Create Chrome Options
OPTIONS = Options()
OPTIONS.add_argument(
    "--user-data-dir=./UserData")
#Create Chrome Driver
DRIVER = Chrome(options=OPTIONS)
#Get page and await login
DRIVER.get("https://discordapp.com/login")
input(WORDS[LANGUAGE][1])
#Find username in all friends list
ELEMENT = DRIVER.find_elements_by_xpath(
    f"//*[contains(text(), {WORDS[LANGUAGE][0]})]")[0]
ELEMENT.click()
sleep(1)
ELEMENT = DRIVER.find_elements_by_xpath(
    f"//*[contains(text(), {USERNAME})]")[0]
ELEMENT.click()
sleep(1)
#Send the message
while 1:
    ACTIONS = ActionChains(DRIVER)
    ACTIONS.send_keys(MESSAGE)
    ACTIONS.send_keys(Keys.ENTER)
    ACTIONS.perform()
    sleep(TIME)
