import tkinter as tk
import re
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

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
    error.config(text=f"PDF generated successfully : {pdf_name}",fg="blue")
    clear_entry()
    
    
def submit():
    Name = Name_entry.get()
    AICTE_id = aicte_entry.get()
    Email = email_entry.get()
    Phone_No = no_entry.get()
    Collage_Name = clg_entry.get()
    
    error.config(text="")
    if not Name or Name.strip() == '':
        error.config(text="Please enter your name.")
        return
    if not re.match(r'^[a-zA-Z\s]+$', Name):
        error.config(text="Name can only contain alphabetic characters.")
        return
    if not AICTE_id:
        error.config(text="Please enter your AICTE ID.")  
        return  
    if not Email:
        error.config(text="Please enter your email address.")
        return
    if not re.match(r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', Email):
        error.config(text="Please enter a valid email address.")
        return
    if not Phone_No:
        error.config(text="Please enter your phone number.") 
        return   
    if not Phone_No.isdigit():
        error.config(text="Phone number must contain only digits.")
        return
    if len(Phone_No) != 10:
        error.config(text="Phone number must be 10 digits long.")
        return
    if not Collage_Name:
        error.config(text="Please enter your college name.") 
        return  
    pdf_generate(Name,AICTE_id,Email,Phone_No,Collage_Name)  

root = tk.Tk()
root.title("Registration Form")
title_label = tk.Label(root, text="Student Registration Form", font=("Helvetica", 20, "bold"), bg="sky blue", fg="white")
title_label.grid(row=0, columnspan=2, pady=10, sticky="ew")

labels = ["Name               :", "AICTE Id         :", "Email                :", "Phone No        :", "College Name :"]
for i, label_text in enumerate(labels, start=1):
    label = tk.Label(root, text=label_text, width=12, anchor="e",font=("Helvetica", 14))
    label.grid(row=i, column=0, padx=(10, 5), pady=5)
    entry = tk.Entry(root, width=30,font=("Helvetica", 14))
    entry.grid(row=i, column=1, padx=(0, 10), pady=5)
    if i == 1:
        Name_entry = entry
    elif i == 2:
        aicte_entry = entry
    elif i == 3:
        email_entry = entry
    elif i == 4:
        no_entry = entry
    elif i == 5:
        clg_entry = entry
        
error = tk.Label(root, text="", fg="red") 
error.grid(row=len(labels)+1, columnspan=2, padx=5, pady=5)     

submit_button = tk.Button(root, text="Submit", command=submit, bg="blue", fg="white", font=("Helvetica", 14, "bold"))
submit_button.grid(row=len(labels)+2, columnspan=2, pady=10, sticky="ew")
root.mainloop()