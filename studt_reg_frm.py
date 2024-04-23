import tkinter as tk
import re
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

def clear_entry():
    Name_entry.delete(0, tk.END)
    aicte_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    no_entry.delete(0, tk.END)
    clg_entry.delete(0, tk.END)

def pdf_generate(Name,AICTE_id,Email,Phone_No,Collage_Name):
    pdf_name=Name+".pdf"
    pdf = canvas.Canvas(pdf_name,pagesize=A4)
    info={
        "Name": Name,
        "AICTE id": AICTE_id,
        "Email" : Email,
        "Phone No": Phone_No,
        "Collage Name" : Collage_Name  
    }
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100,800,"Student Information")
    y=750
    for key,value in info.items():
        pdf.setFont("Helvetica", 12)
        pdf.drawString(100,y,key)
        pdf.drawString(180,y,f": {value}")
        y-=20
    pdf.save()
    error.configure(text=f"PDF generated successfully : {pdf_name}",text_color="blue")
    error.place(x=10, y=300)
    clear_entry()
    
def submit():
    Name = Name_entry.get()
    AICTE_id = aicte_entry.get()
    Email = email_entry.get()
    Phone_No = no_entry.get()
    Collage_Name = clg_entry.get()
    
    error.configure(text="")
    if not Name or Name.strip() == '':
        error.configure(text="Please enter your name.")
        error.place(x=115, y=300)
        return
    if not re.match(r'^[a-zA-Z\s]+$', Name):
        error.configure(text="Name can only contain alphabetic characters.")
        error.place(x=15, y=300)
        return
    if not AICTE_id:
        error.configure(text="Please enter your AICTE ID.") 
        error.place(x=115, y=300) 
        return  
    if not Email:
        error.configure(text="Please enter your email address.")
        error.place(x=115, y=300)
        return
    if not re.match(r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', Email):
        error.configure(text="Please enter a valid email address.")
        error.place(x=115, y=300)
        return
    if not Phone_No:
        error.configure(text="Please enter your phone number.") 
        error.place(x=115, y=300)
        return   
    if not Phone_No.isdigit():
        error.configure(text="Phone number must contain only digits.")
        error.place(x=20, y=300)
        return
    if len(Phone_No) != 10:
        error.configure(text="Phone number must be 10 digits long.")
        error.place(x=20, y=300)
        return
    if not Collage_Name:
        error.configure(text="Please enter your college name.") 
        error.place(x=115, y=300)
        return  
    pdf_generate(Name,AICTE_id,Email,Phone_No,Collage_Name) 


app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("600x440")
app.title('Registration Form')

img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=340, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Student Registration Form", font=('Century Gothic', 25))
l2.place(x=20, y=20)

# Label and Entry for Name
l3 = customtkinter.CTkLabel(master=frame, text="Name                :", font=('Century Gothic', 12))
l3.place(x=10, y=80)
Name_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Enter your name')
Name_entry.place(x=105, y=80)

# Label and Entry for AICTE ID
l4 = customtkinter.CTkLabel(master=frame, text="AICTE ID            :", font=('Century Gothic', 12))
l4.place(x=10, y=115)
aicte_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Enter your AICTE ID')
aicte_entry.place(x=105, y=115)

# Label and Entry for Phone No
l5 = customtkinter.CTkLabel(master=frame, text="Email                  :", font=('Century Gothic', 12))
l5.place(x=10, y=150)
email_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Enter your email')
email_entry.place(x=105, y=150)

# Label and Entry for Email
l6 = customtkinter.CTkLabel(master=frame, text="Phone No         ", font=('Century Gothic', 12))
l6.place(x=10, y=185)
no_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Enter your phone number')
no_entry.place(x=105, y=185)

# Label and Entry for College Name
l7 = customtkinter.CTkLabel(master=frame, text="College Name :", font=('Century Gothic', 12))
l7.place(x=10, y=220)
clg_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Enter your college name')
clg_entry.place(x=105, y=220)

# Create custom button
button1 = customtkinter.CTkButton(master=frame, width=215, text="Save", command=submit, corner_radius=6)
button1.place(x=110, y=270)
button2 = customtkinter.CTkButton(master=frame, width=90, text="Clear", command=clear_entry, corner_radius=6)
button2.place(x=10, y=270)

error = customtkinter.CTkLabel(master=frame, text="", font=('Century Gothic', 13),text_color="red")
error.place(x=115, y=300)

# You can easily integrate authentication system

app.mainloop()
