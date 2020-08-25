import os
import webbrowser
import time
import smtplib, ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

global chrome_path
chrome_path  = "commands/SuggestMovie/chromedriver/chromedriver.exe"
global  driver




try:
    driver = webdriver.Chrome(chrome_path)
    driver.get('https://www.suggestmemovie.com')

except:
    chrome_path = "chromedriver/chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get('https://www.suggestmemovie.com')
#driver.implicitly_wait(5)
time.sleep(3)


moviename = driver.find_element_by_xpath("""/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/h1""").text
rating = driver.find_element_by_xpath("""/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div""").text
story = driver.find_element_by_xpath("""/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div/div[1]/div[2]/p""").text
genre = driver.find_element_by_xpath("""/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div/div[1]/div[2]/dl/dd[1]""").text
movieinfo = [moviename,rating,story,genre]
#getcompanywebsite(' ',' ',' ')
#findstartingxpath()

elementlink = driver.find_element_by_xpath("""/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div/div[1]/ul/li/a[2]""")
filmurl = elementlink.get_attribute('href')

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

    msg = 'MOVIE SUGGESTION ' + '\n'  + moviename + '\n' + 'IMDB Rating - ' + rating + '\n' + story + '\n' + 'Genre - ' + genre + '\n' + 'Link - ' + filmurl
    mailServer = smtplib.SMTP(smtp_server , port)
    mailServer.starttls()
    mailServer.login(sender , password)
    mailServer.sendmail(sender, mailto , msg)
    print(" \n The email was sent!")
    mailServer.quit()

except:
    print('Connect the pc to internet to receive an email')


