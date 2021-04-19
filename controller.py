import tkinter as tk
from tkinter import * 
from tkinter import messagebox 
import cv2 
from PIL import ImageTk, Image
from firebase import firebase
import pyrebase



firebaseConfig = {
    "apiKey": "AIzaSyB8PXmbAhCglMcvTQYYEkEg_H0KlUQHgl4",
    "authDomain": "seabin-be632.firebaseapp.com",
    "databaseURL": "https://seabin-be632.firebaseio.com",
    "projectId": "seabin-be632",
    "storageBucket": "seabin-be632.appspot.com",
    "messagingSenderId": "406649588495",
    "appId": "1:406649588495:web:f90ba06ea477d256820c7a",
    "measurementId": "G-VXF85SSYEC"
};


# pyrebase
firebaseConn = pyrebase.initialize_app(firebaseConfig)

# Auth Reference
auth = firebaseConn.auth()

# Database Reference
db = firebaseConn.database()

root = tk.Tk()
root.title("SeaBin Controller")
# root.attributes("-fullscreen", True)

canvas = tk.Canvas(root,  bg="#21374C")
canvas.grid(row=0, column=0, columnspan = 5)

mainFrame = Frame(canvas,width=300, height=300)
mainFrame.grid(row=0, column=1, columnspan=3, rowspan= 3, padx=20,pady=20)              

#Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)

cap = cv2.VideoCapture('1.mp4')


def show_frame():
	ret, frame = cap.read()

	cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	img   = Image.fromarray(cv2image).resize((760, 400))
	imgtk = ImageTk.PhotoImage(image = img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)


show_frame()  #Display


score_lbl = Label(canvas, text="Score : 0",bg="#30FF00", font=("Calibri", 13))
score_lbl.grid(row=0, column=4)


players_online_lbl = Label(canvas, text="Players Online : 0",bg="#30FF00", font=("Calibri", 13))
players_online_lbl.grid(row=0, column=5, padx=20)



def forward_motion():
    db.child("seabin").child("motion").set("f")
    print("Forward")


def backward_motion():
    db.child("seabin").child("motion").set("b")
    print("Backward")


def leftward_motion():
    db.child("seabin").child("motion").set("l")
    print("Leftward")


def rightward_motion():
    db.child("seabin").child("motion").set("r")
    print("Rightward")


def start_motor():
    db.child("seabin").child("ignition").set("1")
    print("Starting...")


def stop_motor():
    db.child("seabin").child("ignition").set("0")
    print("Stopping...")


def login_user():
	global user_info
	email = username.get()
	password_info = password.get()
	user = auth.sign_in_with_email_and_password(email,password_info)
	user_info = auth.get_account_info(user['idToken'])
	if user == None: 
		messagebox.showerror("Error", "Check your credentials")
		
	else :
		response = messagebox.showinfo("Success", "Succesfully logged")
		if response == 'ok':
			login_screen.destroy()
			


def login_screen(): 
	global login_screen
	global login_frame
	login_screen = Toplevel(root)
	login_screen.title("Login")
	login_screen.geometry("500x200")

	global username, username_entry
	global password, password_entry

	username = StringVar()
	password = StringVar()
	
	login_frame = LabelFrame(login_screen, padx=5, pady=5,bg="#21374C")
	login_frame.grid(padx=15,pady=15)

	username_label = Label(login_frame, text = "Username",width="65")
	username_label.grid(row=0,column=1,columnspan=5,pady=5)

	username_entry = Entry(login_frame, textvariable = username,width=40, borderwidth=2)
	username_entry.grid(row=1,column=1,columnspan=5,pady=5)

	password_label = Label(login_frame, text = "Password",width="65")
	password_label.grid(row=2,column=1,columnspan=5,pady=5)

	password_entry = Entry(login_frame, textvariable = password,width=40, borderwidth=2,show="*")
	password_entry.grid(row=3,column=1,columnspan=5,pady=5)

	login_button = Button(login_frame, text = "Login", width=15, command = login_user,bg="#30FF00")
	login_button.grid(row=4,column=1,columnspan=5,pady=8)


forward_btn = Button(canvas, text="^", font="Times 10 italic bold", width=15,bg="#30FF00", command=forward_motion)
forward_btn.grid(row = 4, column = 1, columnspan =2, padx = 5, pady = 5)

backward_btn = Button(canvas, text="v", width=15,bg="#30FF00",command=backward_motion)
backward_btn.grid(row = 6, column = 1,columnspan = 2, padx = 5, pady = 5)

left_btn = Button(canvas, text="<", font="Times 10 italic bold", width=15,bg="#30FF00",command=leftward_motion)
left_btn.grid(row = 5, column = 1, padx = 5, pady = 5)

right_btn = Button(canvas, text=">", font="Times 10 italic bold", width=15,bg="#30FF00",command=rightward_motion)
right_btn.grid(row = 5, column = 2, padx = 5, pady = 5)

start_btn = Button(canvas, text="Start", width=15,bg="#30FF00",command=start_motor)
start_btn.grid(row=5, column = 3 )

stop_btn = Button(canvas, text="Stop", width=15,bg="#30FF00",command=stop_motor)
stop_btn.grid(row=5, column = 4 , padx = 10)

login_btn = Button(canvas, text="Log In", width=10,bg="#30FF00",command=login_screen)
login_btn.grid(row=7, column = 5 , padx = 10, pady=5)


logged_status_lbl = Label(canvas, text="Logged Out",bg="#30FF00")   
logged_status_lbl.grid(row=8, column=5, pady=5)


root.mainloop()
