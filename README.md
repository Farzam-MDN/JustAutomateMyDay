# JustAutomateMyDay



<!---
![JustAutomateMyDay Logo](https://i.imgur.com/6a0G8wz.png)
-->


JustAutomateMyDay (abbreviated as JAMD) is a python app that can run other python programs based on a specific schedule. Using this tool you can schedule any task such as webscraping or sending emails on a specific date and a specific time. You can even provide your own python applications and make them run based on your schedule!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need the following in order to run the application as it is intended on your machine:

```
Python 3 or above
Pip package installer for python
An FTP server if you want to add scheduled tasks over internet 
```

### Installing and Running the application

First clone this repository or download it manually to a working directory on your computer.
Thereafter, open terminal/cmd inside the JustAutomateMyDay directory on your computer.
Now Run the following command in your terminal/cmd:

```
pip install -r requirements.txt
```
After all the requirements are installed, open config.txt file in JustAutomateMyDay directory.
Also open config-example.txt and help.txt file in the same directory. Now try to set up your config.txt file by reading the guide in help.txt file (See 'explanation on config.txt' section) and looking at config-example.txt file.
As a result your config.txt file should look similar to this:

```
SMTPServer:smtp.gmail.com
Port:587
SenderEmailAddress:somethingsomething42@gmail.com
SenderEmailPassword:password1234
RecipientEmailAddress:receiver24124@gmail.com
OnlineSchedule:https://example.com/JustAutomateMyDay/onlineschedule.txt
```
After the config file is set up we need to set up the Chrome WebDriver. Go to this link https://chromedriver.chromium.org/downloads and download the last version of Chrome WebDriver.
After downloading the chrome webdriver, extract the zip file and copy the extracted file. Now go to JustAutomateMyDay/Commands/SuggestAlbum/chromedriver  and paste the copied file there. Afterwards, go to JustAutomateMyDay/Commands/SuggestMovie/chromedriver and also paste the same copied file there. Lastly, paste the paste the copied file in JustAutomateMyDay/Commands/TechNews/chromedriver.  Now the Chrome WebDriver is set up. Since you will be using the latest version of the chrome driver it is highly suggested to update the chrome browser on your machine to the latest version to have the best performance.

Now the application is configured. We now need to add some scheduled tasks for the application to perform. In JustAutomateMyDay directory open the following files schedule.txt, schedule-example.txt and help.txt.
inside help.txt file read the section about schedule.txt (See 'explanation on schedule.txt' section) and set up some tasks for yourself in schedule.txt file based on the guide.

(Optional): Login to your FTP server and input some tasks in onlineschedule.txt by editing that text file (Inout the tasks just like the way you did for schedule.txt. For explanation on how to set up FTP, Open help.txt and read 'explanation on config.txt' section). 


Now let's run the application. Open cmd/terminal in JustAutomateMyDay directory and run the command below: 
```
py JAMD.py
```
This will run the JustAutomateMyDay application. The application regularly checks the 'schedule.txt' file and performs a task if it is the time to do so. You add more tasks either by editing the 'schedule.txt' file or by editing 'onlineschedule.txt' file on your FTP server. You do not need to close JAMD.py to update your schedules. 

## Making your own commands
Create a Folder in JustAutomateMyDay/Commands and name that folder to something that is not already in commandslist.txt . Now make the following files inside folder you created for your command:  config.txt, launchinfo.txt, log.txt. Now inside the folder create a python file with exactly the same name as the folder. for instance if the folder was named 'ExampleApp' the python file inside ExampleApp folder should be named 'ExampleApp.py' . Now write your python code in the python file without using any functions (JAMD.py currently cannot run functions located in other .py files) . Inside the python file whenever you are referencing a directory be sure to calculate it from JustAutomateMyDay folder (since JAMD.py will try to run your command inside JustAutomateMyDay folder.). In case you used any external libraries for your custom command, install those libraries via pip or other possible ways. Lastly go to commandslist.txt inside JustAutomateMyDay folder and inside a new line write the name of the folder your command is located in (which should be the same as the name of the python file without the .py).
Now to be able to run your command on a schedule, go to schedule.txt in JustAutomateMyDay folder and create a task for running your command. For instance if the command python file was named ExampleApp.py a task to run that file can be like this: 25-08-2020,16:30,/ExampleApp,Whatever you want,loud  

## Contributing

Feel free to fork and expand this project! Send a pull request if you would like to add your code to the project.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Farzam-MDN/JustShareKeys/releases). 

## Authors

* **Farzam Madani** - *Creation of the core application* - [Farzam-MDN](https://github.com/Farzam-MDN)

See also the list of [contributors](https://github.com/Farzam-MDN/JustShareKeys/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Farzam-MDN/JustShareKeys/blob/master/LICENSE) file for details

## Acknowledgments

* Big thanks to anyone whose library is used for this project 



