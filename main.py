import customtkinter
import os
from dotenv import load_dotenv

import smtplib #Simple Mail Transfer Protocol
from email.mime.multipart import MIMEMultipart
# MIMEText for creating body of the email message.
from email.mime.text import MIMEText
# MIMEApplication attaching files to email messages.
from email.mime.application import MIMEApplication


subject = "Status Update"
body = "Today's Status: "

#To load environment variable
load_dotenv()

#Creates the container for an email message to hold
message = MIMEMultipart()
message['Subject'] = subject
message['From'] =  os.environ.get('sender_email')
message['To'] = os.environ.get('recipient_email')
body_part = MIMEText(body) 
message.attach(body_part)
smtp_server = 'smtp.gmail.com'
smtp_port = 465
path_to_file = 'status.txt'

#Setting Gui Themes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk() #root variable for main class to access all its feature
root.title("Email Sender")
root.geometry("500x350") #GUI Window Size

#send Function
def send():
    yourname= entry1.get() #Making variables to fetch the data of these fields 
    date= entry2.get()
    status=entry3.get()

      #if any filed is empty
    if (yourname=='' or date=='' or status==''):{ print("Please filled all the required fields")}
    else:
        with open('status.txt', 'wt') as f: #copying the output file into another file
            print(yourname," : ",date," : ",status, file =f)
    #Attaching the file with mail   
        with open('status.txt', 'rb') as f:   
            message.attach(MIMEApplication(f.read(), Name="status.txt"))
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(os.environ.get('sender_email') ,os.environ.get('sender_password'))
            server.sendmail(os.environ.get('sender_email'), os.environ.get('recipient_email') ,message.as_string())

    
    root.destroy() #To close the Gui after sending email

#GUI For User input
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#Heading
label = customtkinter.CTkLabel(master=frame, text="Status Update", font=("roboto",24))
label.pack(pady=12, padx=10)

#For Name
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="YourName")
entry1.pack(pady=12, padx=10)

#Foe Email
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Date")
entry2.pack(pady=12, padx=10)

#For Status
entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Status" )
entry3.pack(pady=12, padx=10)

#Send Button
button = customtkinter.CTkButton(master=frame, text="Send", command=send)
button.pack(pady=12, padx=10)

root.mainloop() #To keep you gui on screen if we dont write it then it will disapperad immeditely




