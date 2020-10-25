import os, sys, time, smtplib, webbrowser


# Start #
def program():
    userOS = input("\n\n\nEnter your Operating System [Windows/Linux]: ")
    if userOS == 'windows' or userOS == 'Windows' or userOS == 'WINDOWS':
        os.system("Color D")
    #Loading Screen:
    def logoLoad():
        print('''
    
    ╭━━━━╮╱╱╱╱╭╮╱╭╮╭━╮╭╮
    ┃╭╮╭╮┃╱╱╱╱┃┃╱┃┃┃╭╋╯╰╮
    ╰╯┃┃┣┻━┳━━┫┃╱┃╰╯╯┣╮╭╯
    ╱╱┃┃┃╭╮┃╭╮┃┃╱┃╭╮┃┣┫┃
    ╱╱┃┃┃╰╯┃╰╯┃╰╮┃┃┃╰┫┃╰╮
    ╱╱╰╯╰━━┻━━┻━╯╰╯╰━┻┻━╯
        By dean0
    ---------------   
        Loading...
        ''')
        time.sleep(1)


    #Menu:
    def menu():
        print('''
        Tools:
        1) Pinger
        2) Email Bomber
        3) Website Spammer
        4) Muffin
        5) Patch Notes
        6) Color Settings (Windows ONLY!)
        7) Feedback (Suggestions)
        ''')


    #Email Bomber
    def emailBomber():

        def loadingScreen():
            print('''
      ▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███      
        ▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒   
        ▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒    
        ▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄     
        ░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒    
        ░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
        ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
        ░   ░      ░     ░   ▒    ▒ ░  ░ ░       ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
        ░  ░       ░         ░  ░ ░      ░  ░    ░          ░ ░         ░    ░         ░  ░   ░      

            ''')

            print("Loading...")
            time.sleep(1)
            print("\n")

        if userOS == "Windows" or userOS == "windows" or userOS == "WINDOWS":
            os.system("Color B")
        time.sleep(0.15)
        loadingScreen()
        senderEmail = input("Enter Email for Sender (Gmail): ")
        senderPassword = input("Enter Password for Sender: ")
        recEmail = input("Enter your Victim (Person Recieving Email): ")
        emailMsg = input("Enter the message you want to send:\n")
        emailAmount = int(input("Enter how many emails you want to send: "))

        def emailSend():
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(senderEmail, senderPassword)
                server.sendmail(senderEmail, recEmail, emailMsg)
                print("Sent Email!")
            except:
                print("Error: Email Couldn't be Sent.")

        for i in range(emailAmount):
            emailSend()
        print("Done! Sent", emailAmount, "emails")

    def pinger():
        pingTarget = input("Enter IP/Website URL: ")
        pingAmount = input("Enter how many times you want to ping the target: ")
        if userOS == 'windows' or userOS == 'Windows' or userOS == 'WINDOWS':
            wincmd = "ping {} -n {}".format(pingTarget, pingAmount)
            os.system(wincmd)
        elif userOS == 'linux' or userOS == 'Linux' or userOS == 'LINUX':
            lincmd = "ping {} -c {}".format(pingTarget, pingAmount)
            os.system(lincmd)

    def webSpam():
        spamSite = input("Enter the website: ")
        spamAmount = int(input("Enter how many times you want the site opened: "))
        for i in range(spamAmount):
            webbrowser.open(spamSite)
            print("Opened!")
            #Finish
        print("Done! Opened", spamAmount, "tabs")

    def colorSettings():
        print('''
        1) Red
        2) Green
        3) Blue
        4) Yellow
        5) White (Bright)
        6) Standard (White; Non-Bright)
        ''')
        colorSet = input("Enter the Number Correlating to the Color you Want: ")
        if colorSet == '1':
            os.system("Color 4")
        elif colorSet == '2':
            os.system("Color A")
        elif colorSet == '3':
            os.system("Color 3")
        elif colorSet == '4':
            os.system("Color E")
        elif colorSet == '5':
            os.system("Color F")
        elif colorSet == '6':
            os.system("Color 7")

    def muffinPic():
        print('''
                                                                                            
                                ██████                                                
                                ██▒▒▒▒▒▒██                                              
                             ██▒▒  ▒▒▒▒▒▒██                                            
                              ██▒▒  ▒▒▒▒▒▒████████                                      
                              ██▒▒▒▒▒▒▒▒▒▒██░░░░░░████                                  
                                ██▒▒▒▒▒▒██░░░░▓▓░░░░░░████                              
                              ██░░██████░░░░░░░░░░░░  ░░░░██                            
                              ██░░░░░░▒▒░░░░░░░░▒▒░░░░░░░░██                            
                            ██░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██                          
                            ██░░░░▓▓░░░░░░  ░░░░░░░░░░░░░░░░██                          
                          ██░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░██                        
                          ██░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░██                        
                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                        
                            ████████░░░░░░░░██░░░░░░░░░░░░████                          
                              ██▓▓▓▓██░░░░██▓▓██░░░░░░░░████                            
                              ██▓▓▓▓▓▓████▓▓▓▓▓▓██░░░░██  ██                            
                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██                              
                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                              
                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                              
                                  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                
                                    ██████████████████                                  
                                                                                        
    
        ''')


    def patchnotes():
        print('''
        Tool Kit by dean0coin
      -------------------------
        BETA v0.2 Patch Notes
        
        1) Added Patch Notes Section.
        2) Added Feedback Section.
        3) Added 'Go Back' Function so you can restart the program after using a tool.
        4) For Email Sending (Feedback + Email Bomber) error messages have been added. (ie. 'try + except' in Python)
        5) Reduced Loading time for program and for Email Bomber. (1.75s to 1s)
        ''')


    def goBack():
        backSel = input("\nType 1 to go back: ")
        if backSel == '1':
            program()
        else:
            print("\nError; Exiting Program.")
            time.sleep(0.95)
            sys.exit()


    def feedback():
        fbSenderML = "toolkitfeedback123@gmail.com"
        fbSenderPW = "123feedback123"
        fbRecML = "toolkitfeedback123@gmail.com"
        feedbackMsg = input("Give Feedback!:\n")

        #Send Feedback
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fbSenderML, fbSenderPW)
            server.sendmail(fbSenderML, fbRecML, feedbackMsg)
            print("Sent Feedback!")
        except:
            print("Error: Feedback Couldn't be Sent.")
            goBack()

    #UI Start
    logoLoad()
    menu()
    userNum = input("Enter Number: ")
    if userNum == '1':
        pinger()
        goBack()
    if userNum == '2':
        emailBomber()
        goBack()
    if userNum == '3':
        webSpam()
        goBack()
    if userNum == '4':
        muffinPic()
        goBack()
    if userNum == '5':
        patchnotes()
        goBack()
    if userNum == '6':
        colorSettings()
        goBack()
    if userNum == '7':
        feedback()
        goBack()

program()




