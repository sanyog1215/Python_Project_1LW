#function to send email
def send_email():
        import smtplib
        import getpass
        import geocoder

        #user input email
        fromaddr = input("From: ")
        toaddrs = input("To: ").split()

        # email subject
        subject = input("Subject: ")

        #  email message
        print("Enter message:3")
        msg = ""
        while True:
            try:
                line = input()
            except EOFError:
                break
            if not line:
                break
            msg += line + "\n"

       
        email_message = f"From: {fromaddr}\nTo: {', '.join(toaddrs)}\nSubject: {subject}\n\n{msg}"

        app_password = getpass.getpass("Enter your Gmail app-specific password: ")

        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Using TLS on port 587
            server.starttls()
            server.login(fromaddr, app_password)  # Use the app-specific password

            # Send the email
            server.sendmail(fromaddr, toaddrs, email_message)
# Close the SMTP server connection
            server.quit()
            print("Email sent successfully!")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            

            
#function to send sms
def send_sms():
     from twilio.rest import Client
     account_sid="AC898946107af3ee2f7f77e21feb3d3c18"
     auth_token="bf6cc9dff76c9bf17dd0b9fced0c929d"
     client=Client(account_sid,auth_token)
     message = client.messages \
    .create(       
            from_= "+12053031065 ",
            to=input("receiver no.:"),
            body=input("Enter your message:")
            )

     print(message.sid)
    #funtion to send whatsapp message

def send_whatsapp_message():
        import pywhatkit as kit

        phone_number = input("Enter the recipient's phone number: ")

        message = input("Enter the message you want to send: ")

        hour = int(input("Enter the hour to send the message (24-hour format): "))
        minute = int(input("Enter the minute to send the message: "))

        kit.sendwhatmsg(phone_number, message, hour, minute)

  

#function to open chrome
def open_chrome():
    import os
    os.system("chrome")
    
#function to open notepad
def open_notepad():
    import os
    os.system("notepad")
    
#function to speak text   
def speak_text(text):
    import pyttsx3
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    #function to open webpage   
def open_webpage():
    import webbrowser
    url = input("Enter the URL: ")
    webbrowser.open(url)
    
    
#function to get wikipedia data    
def get_wikipedia_data(topic):
    import requests
    from bs4 import BeautifulSoup
    wikipedia_url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(wikipedia_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.text
        paragraphs = soup.find_all('p')

        print(f"Title: {title}\n")

        for paragraph in paragraphs:
            print(paragraph.text)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        

#funtion to get geolocation
def get_geolocation(address):
    try:
        location = geocoder.osm(address)
        latitude, longitude = location.latlng
        return latitude, longitude
    except Exception as e:
        print(f"Error getting geolocation: {e}")
        return None

def geolocation_interaction():
    print("-------------Geolocation Interaction-------------------------------")
    address = input("Enter an address for geolocation: ")
    coordinates = get_geolocation(address)

    if coordinates:
        print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
    else:
        print("Geolocation not available.")

    
 



while True:
    print("\t\t\t\t\tWelocme to  MENU ")

    print(""" 
        press 1:  send a mail
        press 2:  send sms
        press 3:  send Whatsap message
        press 4:  open chrome
        press 5:  open notepad
        press 6:  to convert text to speech
        press 7:  for geolocation
        press 8:  open web page
        press 9:  to get wikipedia data
        press 10: To exit 
        """
        )
    
    choice=int(input("Enter Your Choice:"))
    
    if(choice==1):
        send_email()

    elif(choice==2):
        send_sms()

    elif(choice==3):
        send_whatsapp_message()

    
    elif(choice==4):
        open_chrome()

    elif(choice==5):
        open_notepad()
        
    elif(choice==6):
        text_speak=input("Enter text  to speak:")
        speak_text(text_speak)
        
    elif(choice==7):
        geolocation_interaction()
        
    elif(choice==8):
        open_webpage()
        
    elif(choice==9):
        topic = input("Enter the topic for Wikipedia data: ")
        get_wikipedia_data(topic)
        
    elif(choice==10):
        break
    else:
        print("Incorrect choice")
