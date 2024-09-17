EmailSender Using python

Sends your daily status update by storing it in a file in an specific format over email using python script.

Prerequired modules: customkinter, dotenv, smtplib. Install theem using pip install cutomkinter.

First we create a basic GUI(Graphic User Interface) using cutomkinter module. We provide label(title), three entry filed(yourname,date,status) for input from user and a send button also adjust their margin and padding.

  ![GUI Image](https://github.com/user-attachments/assets/22b7b236-9540-4507-9650-3e9feb250909)

Second we define a send function which fetch the data of gui using .get()
method in three varibales yourname, date, status and apply if condition on it that if any of the field is empty it print please filled all the details.

Third if details provide correctly then store the data in a file called status.txt.

Now for sending emails, we use smtlib(simple file mail transfer protocol).
For the structure of email we provide body, subject ,recipient mail, sneder mail and password (it is 16 Character App Password Not your gmail passowrd).

Dotenv is used for environment variable in our file. For storing sensitive information like mail password in .env file and fetch them using os.environ.get() method.


