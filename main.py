import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk() #root variable for main class to access all its feature
root.title("Email Sender")
root.geometry("500x350") #GUI Window Size

def send():
    yourname= entry1.get()
    date= entry2.get()
    status=entry3.get()
    with open('status.txt', 'wt') as f:
        print(yourname, file =f)
        print(date, file=f)
        print(status, file=f)
   
    exit

    if (yourname=='' or date=='' or status==''): print("Please filled all the required fields")
    exit

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Status Update", font=("roboto",24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="YourName")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Date")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Status" )
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Send", command=send)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12,padx=10)

root.mainloop() #To keep you gui on screen if we dont write it then it will disappera immeditely




