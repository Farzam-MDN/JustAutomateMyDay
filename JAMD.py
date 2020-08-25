import time
from datetime import datetime
import os
import smtplib, ssl
import random
import wget

global lastcommand #saves the last command in the config file here to then write it in log in 2 locations. log of JAMD and config of the command
global currentline
currentline = 0
#lastcommand = ''

global showonlineschedulemsg
showonlineschedulemsg = True

def Hello():
    print('Hi there. Welcome to JustAutomateMyDay (JAMD).')
    print('The scheduled commands will run in time..')
    time.sleep(3)
    #print('The config file will be loaded soon..')


def Config(command):
    global lastcommand
    #print(command)


    command = command.replace('\n', '')
    commandinfo = command.split(',')
    #print(commandinfo)  #this was on

    now = datetime.now()
    date_year = now.strftime("%Y")
    date_month = now.strftime("%m")
    date_day = now.strftime("%d")
    time_hour = now.strftime("%H")
    time_minute = now.strftime("%M")
    #time_second = now.strftime("%S")

    #if the exact command not already in log file
    #compare

    donebefore = False

    with open('log.txt') as f:
        if command in f.read():
            #print("true")
            donebefore = True
            f.close()

    if donebefore == False:
        #print('Not done before')

        thecommanddate = commandinfo[0]
        thecommandtime = commandinfo[1]
        thecommandname = commandinfo[2].replace('/', '')
        thecommandparameters = commandinfo[3]
        thecommandmode = commandinfo[4]

        if date_year == thecommanddate.split('-')[2]:
            #print('same year')
            if date_month == thecommanddate.split('-')[1]:
                #print('same month')
                if date_day == thecommanddate.split('-')[0]:
                    #print('same day')
                    if time_hour == thecommandtime.split(':')[0]:
                        #print('same hour')
                        if time_minute == thecommandtime.split(':')[1]:
                            #print('same minute')

                            #print('now run the command')

                            #first check if the command is in the list
                            validcommand = False
                            with open('commandslist.txt') as f:
                                    if thecommandname in f.read():
                                            #print("Valid command")
                                            validcommand = True
                                            pyfileaddress = 'Commands/'+thecommandname+'/'+thecommandname+'.py'
                                            logfileaddress = 'Commands/'+thecommandname+'/'+ 'log.txt'
                                            #os.system(fileaddress)
                                            #print(fileaddress)
                                            exec(open(pyfileaddress).read())
                                            f.close()
                                            print('The following command was run: ' + thecommandname)

                                            #randnum = random.randint(1, 250)
                                            lastcommand = thecommandname + ' ' + thecommandparameters

                                            with open("log.txt","a") as f:
                                                f.write(command + '\n')
                                                f.close()

                                            with open(logfileaddress,"a") as f:
                                                f.write(command + '\n')
                                                f.close()

                                            if thecommandmode == 'loud':
                                                #sendemail
                                                #check the config for the recepient email and sender credentials

                                                SendEmail()
                                                #f.close()



                                    else:
                                        print('/' + thecommandname + ' is an invalid command. Please add it to commandslist')
                                        f.close()
                                        with open("log.txt","a") as f:
                                                f.write('ERROR in:' +  command + '\n')
                                                f.close()






def SendEmail():
    try:
        global lastcommand


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

        msg = 'JAMD MSG ' + lastcommand
        mailServer = smtplib.SMTP(smtp_server , port)
        mailServer.starttls()
        mailServer.login(sender , password)
        mailServer.sendmail(sender, mailto , msg)
        print(" \n The email was sent!")
        mailServer.quit()

    except:
        print('Please connect to internet to send email')



def GetNumberofLines():
    num_lines = sum(1 for line in open('schedule.txt'))
    return num_lines

def StartApp():
    global currentline
    global showonlineschedulemsg
    #url of online schedule
    f=open('config.txt')
    lines=f.readlines()
    lineonlineschedule = lines[5]
    lineonlineschedule = lineonlineschedule.replace("OnlineSchedule:","")
    lineonlineschedule = lineonlineschedule.replace("\n","")
    f.close()

    Addressoflogfileonserver = lineonlineschedule




    #for each line in config file     #does this on a loop

    while True:

        #taking care of onlineschedule
        #onlineschedulelines = ['']
        try:
            downloadedfilepath = wget.download(Addressoflogfileonserver)
            f = open(downloadedfilepath, "r")
            onlineschedulelines = f.readlines()
            f.close()
            os.remove(downloadedfilepath)

            f = open("schedule.txt", "r")
            schedulelines = f.readlines()
            f.close()

            f = open("schedule.txt", "a")
            for aline in onlineschedulelines:
                #aline = aline.replace('\n','')
                if aline in schedulelines:
                    pass
                elif aline not in schedulelines:
                    f.write('\n' + aline)

            f.close()
        except:
            if showonlineschedulemsg == True:
                print('Connect to internet to use the online schedule.')
                showonlineschedulemsg = False


        numoflines = GetNumberofLines()
        if currentline == numoflines:
                currentline = 0

        while currentline < numoflines:
            f=open('schedule.txt')
            lines=f.readlines()
            #print(lines[currentline])
##            if(lines[currentline] == ''):
##                print('it was empty line')

            Config(lines[currentline])
            f.close()
            currentline = currentline + 1




            f.close()




#program
Hello()
StartApp()



