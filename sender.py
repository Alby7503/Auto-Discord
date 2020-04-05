"""Send a message automatically"""
# Tested in Python 3.7.7 64 Bit
from sys import argv
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

if len(argv) < 2:
    print("Usage: python sender.py (Username) [Message] {Interval} {(Language)}")
    exit(1)

USERNAME = argv[1]
MESSAGE = argv[2] if len(argv) > 2 else "Hi!"
try:
    TIME = int(argv[3]) if len(argv) > 3 else 3
except ValueError:
    print(argv[3] + " is not a valid number")
    exit(1)
LANGUAGE = argv[4] if len(argv) > 4 else "EN"
WORDS = {
    "EN": ["All", "Please log in your account and press enter when ready..."],
    "IT": ["Tutti", "Per favore accedi al tuo account e premi invio quando sei pronto..."],
    "FR": ["Tous", "Veuillez vous connecter à votre compte et appuyez sur Entrée lorsque vous êtes prêt..."],
    "DE": ["Alle", "Bitte melden Sie sich in Ihrem Konto an und drücken Sie die Eingabetaste, wenn Sie bereit sind..."]
}
# Create Chrome Options
OPTIONS = Options()
OPTIONS.add_argument(
    "--user-data-dir=./UserData")
# Create Chrome Driver
DRIVER = Chrome("chromedriver.exe", options=OPTIONS)
# Get page and await login
DRIVER.get("https://discordapp.com/login")
input(WORDS[LANGUAGE][1])
# Find username in all friends list
ELEMENT = DRIVER.find_element_by_xpath(
    """//*[@id="app-mount"]/div[1]/div/div[2]/div/div/div/div/div[2]/section/div[1]/div[3]/div[2]""")
ELEMENT.click()
sleep(1)
#Search User
ELEMENT = DRIVER.find_element_by_class_name("searchBarComponent-32dTOx")
ELEMENT.click()
sleep(1)
ELEMENT = DRIVER.find_element_by_class_name("input-2VB9rf")
ELEMENT.click()
sleep(0.5)
ELEMENT.send_keys(USERNAME)
sleep(0.2)
ELEMENT.send_keys(Keys.ENTER)
sleep(1)
# Send the message
try:
    while 1:
        ACTIONS = ActionChains(DRIVER)
        ACTIONS.send_keys(MESSAGE)
        ACTIONS.send_keys(Keys.ENTER)
        ACTIONS.perform()
        sleep(TIME)
except KeyboardInterrupt:
    pass
