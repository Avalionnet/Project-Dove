from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

launcher = webdriver.Chrome()
launcher.get('https://web.whatsapp.com/')
input('Please scan the QR code on the browser. Press enter here after you\'ve successfully loggin in')

# This method sends a document from your computer to the selected recipient indicated by [name]
def sendDocument(name, messageBody, filepath):
    searchBox = launcher.find_element_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir = "ltr"]')
    time.sleep(2)
    searchBox.send_keys(name + Keys.ENTER)

    recipient = launcher.find_element_by_xpath(f'//span[@title = "{name}"]')
    recipient.click()

    attachmentIcon =  launcher.find_element_by_xpath(f'//span[@data-testid = "clip"][@data-icon="clip"]')
    attachmentIcon.click()

    documentIcon =  launcher.find_element_by_xpath(f'//input[@accept="*"][@type="file"]')
    documentIcon.send_keys(filepath)

    time.sleep(2)
    sendButton =  launcher.find_element_by_xpath(f'//span[@data-testid="send"]')
    sendButton.click()

# This method sends a message to the intended recipient
def sendMessage(name, message):
    searchBox = launcher.find_element_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"][@dir = "ltr"]')
    time.sleep(1)
    searchBox.send_keys(name + Keys.ENTER)

    recipient = launcher.find_element_by_xpath(f'//span[@title = "{name}"]')
    recipient.click()
    time.sleep(1)
    inputBox = launcher.find_element_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"][@spellcheck="true"]')
    inputBox.send_keys(message + Keys.ENTER)

# Enter the whatsapp username of the recipient here
name = "[Replace this with UserName]"
# Example filepath
filepath = "C:\\Your\\Document\\Directory\\sample.pdf"
message = "[Message Content Here]"

# Sends this message to the selected user 20 times
for i in range(0, 20):
    sendMessage(name, message)
    
# sendDocument(n, message, filepath)



