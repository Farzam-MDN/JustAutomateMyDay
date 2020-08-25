import os
import webbrowser
import time
import smtplib, ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import random

global chrome_path
chrome_path  = "commands/SuggestMovie/chromedriver/chromedriver.exe"
global  driver




page = random.randint(1, 500)
url = 'https://www.besteveralbums.com/overall.php?o=&f=&fv=&orderby=-InfoRankScore&sortdir=asc&page=' + str(page)

try:
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)

except:
    chrome_path = "chromedriver/chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)

driver.implicitly_wait(3)


#click on accept privacy
driver.find_element_by_xpath("""//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]""").click

albumnames = [driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[2]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[7]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[12]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[17]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[22]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[27]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[32]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[37]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[42]/div[3]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[47]/div[3]/a""").text]
artists = [driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[2]/div[4]/a""").text, driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[7]/div[4]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[12]/div[4]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[17]/div[4]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[22]/div[4]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[27]/div[4]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[32]/div[4]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[37]/div[4]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[42]/div[4]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[47]/div[4]/a""").text]
ranks = [driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[5]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[10]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[15]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[20]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[25]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[30]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[35]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[40]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[45]/div/div[10]/a""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[50]/div/div[10]/a""").text]
yearofreleases = [driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[5]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[10]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[15]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[20]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[25]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[30]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[35]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[40]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[45]/div/div[2]""").text,driver.find_element_by_xpath("""//*[@id="div_chart"]/div[1]/div[50]/div/div[2]""").text]



##print(albumnames)
##print(ranks)
##print(yearofreleases)





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
    msg = 'ALBUM SUGGESTION ' + '\n'  + albumnames[albumnum] + '\n' + 'Artist - ' + artists[albumnum] + '\n' + 'Rank - ' + ranks[albumnum] + '\n' + 'Released in - ' + yearofreleases[albumnum]
    mailServer = smtplib.SMTP(smtp_server , port)
    mailServer.starttls()
    mailServer.login(sender , password)
    mailServer.sendmail(sender, mailto , msg)
    print(" \n The email was sent!")
    mailServer.quit()

except:
    print('Connect the pc to internet to receive an email')


