# Import necessary packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import re

warnings.simplefilter("ignore")
url = "https://chat.chatgptdemo.net/"
chrome_driver_path = 'C:\\Users\\hp\\Desktop\\DEVELOPER\\Projects\\Project 1\\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument('--log-level=3')
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(5)


File = open("C:\\Users\\hp\\Desktop\\DEVELOPER\\Projects\\Project 1\\Chatnumber.txt","w")
File.write("3")
File.close()

while True:
    Inputtttt = input("Enter Your Query : ")
    try:
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/div[3]/div[3]/div[3]/textarea").send_keys(Inputtttt)
    except:
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/div[3]/div[3]/div[3]/textarea").send_keys(Inputtttt)

    sleep(1)
    try:
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/div[3]/div[3]/div[4]").click()
    except:
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/div[3]/div[3]/div[4]").click()

    sleep(5)
    File = open("C:\\Users\\hp\\Desktop\\DEVELOPER\\Projects\\Project 1\\Chatnumber.txt","r")
    Data = File.read()
    Data = str(Data)
    File.close()
    try:
        XpathValue = f'/html/body/div[1]/div[1]/div[3]/div[2]/div[{Data}]/div[1]/div[2]/pre'
        Text = driver.find_element(by=By.XPATH,value=XpathValue).text
        NewText = re.sub(r'\d+\s*','',Text)
        print(NewText)
        File = open("C:\\Users\\hp\\Desktop\\DEVELOPER\\Projects\\Project 1\\Chatnumber.txt","w")
        NewData = int(Data) + 2
        File.write(str(NewData))
        File.close()
    except Exception as e:
        print(e)
