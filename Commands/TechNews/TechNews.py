import os
import webbrowser
import time
import smtplib, ssl
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import random

global chrome_path
chrome_path  = "commands/SuggestMovie/chromedriver/chromedriver.exe"
global  driver




page = random.randint(1, 500)
url = 'https://technology.slashdot.org'

try:
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)

except:
    chrome_path = "chromedriver/chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)




driver.implicitly_wait(3)


#click on accept privacy




elem = driver.find_element_by_xpath("""//*[@id="cmpwelcomebtnyes"]/a""")
actions = ActionChains(driver)
actions.click(elem).perform()

time.sleep(3)


headlines = [driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[1]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[2]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[4]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[5]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[6]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[7]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[8]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[9]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[10]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[11]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[12]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[13]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[14]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[15]/header/h2""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[16]/header/h2""").text]
news = [driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[1]/div/div""").text, driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[2]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[4]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[5]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[6]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[7]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[8]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[9]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[10]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[11]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[12]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[13]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[14]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[15]/div/div""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[16]/div/div""").text]
dates = [driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[1]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[2]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[4]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[5]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[6]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[7]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[8]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[9]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[10]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[11]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[12]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[13]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[14]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[15]/header/div/span[2]""").text,driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[16]/header/div/span[2]""").text]
links = [driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[1]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[2]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[4]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[5]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[6]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[7]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[8]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[9]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[10]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[11]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[12]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[13]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[14]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[15]/header/h2/span[1]/a""").get_attribute('href'),driver.find_element_by_xpath("""/html/body/section[1]/div[4]/div/div/div/div[1]/article[16]/header/h2/span[1]/a""").get_attribute('href')]


##print(str(headlines))
##print(str(news))
##print(str(dates))
##print(str(links))


driver.close()


#sends email

try:
    f = open("config.txt", "r")
    lines = f.readlines()
    linesmtpserver = lines[0]
    linesmtpserver = linesmtpserver.replace("SMTPServer:","")
    linesmtpserver = linesmtpserver.replace("\n","")

    lineport = lines[1]
    lineport = lineport.replace("Port:","")
    lineport = lineport.replace("\n","")

    linesenderemail = lines[2]
    linesenderemail = linesenderemail.replace("SenderEmailAddress:","")
    linesenderemail = linesenderemail.replace("\n","")

    linesenderpass = lines[3]
    linesenderpass = linesenderpass.replace("SenderEmailPassword:","")
    linesenderpass = linesenderpass.replace("\n","")

    linerecipientemail = lines[4]
    linerecipientemail = linerecipientemail.replace("RecipientEmailAddress:","")
    linerecipientemail = linerecipientemail.replace("\n","")

    context = ssl.create_default_context()




    smtp_server = str(linesmtpserver)
    port = int(lineport)

    sender = linesenderemail
    password = linesenderpass

    mailto = linerecipientemail

    albumnum = random.randint(0, 9)

    msg = 'TECH NEWS ' + '\n' + '\n' + '\n'

    for headline in headlines:
            msg = msg + str(headlines[headlines.index(headline)]) + '\n' + '\n' +  str(dates[headlines.index(headline)]) + '\n' + '\n' +  str(news[headlines.index(headline)]) + '\n' + str(links[headlines.index(headline)]) + '\n' + '\n' + '***************************************************' + '\n'




    mailServer = smtplib.SMTP(smtp_server , port)
    mailServer.starttls()
    mailServer.login(sender , password)
    mailServer.sendmail(sender, mailto , msg)
    print(" \n The email was sent!")
    mailServer.quit()

except:
    print('Connect the pc to internet to receive an email')


