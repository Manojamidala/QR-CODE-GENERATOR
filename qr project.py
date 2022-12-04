from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class Qr:
    def __init__(self, root):
        pass
        self.root=root
        self.root.geometry("1200x600+200+50") 
        self.root.title("QR Code Generator")
        self.root.resizable(True, True)

        self.var_regno=StringVar() 
        self.var_name=StringVar() 
        self.var_phone=StringVar()
        self.var_dept=StringVar() 
        self.var_year=StringVar()
        self.download_Path = StringVar()

        title=Label(self.root,text="QR Code Generator",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)

        entryFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white') 
        entryFrame.place(x=50,y=100,width=500,height=450)

        title1=Label(entryFrame,text="Details", font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        lbl_code=Label(entryFrame,text="ID. Number",font=("times newroman",18,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(entryFrame,text="Name",font=("times new roman",18,'bold'),bg='white').place(x=20,y=110)
        lbl_dept=Label(entryFrame,text="Department",font=("times new roman",18,'bold'),bg='white').place(x=20,y=160)

        lbl_phno=Label(entryFrame,text="Phone number",font=("times new roman",18,'bold'),bg='white').place(x=20,y=210) 
        lbl_year=Label(entryFrame,text="year of study",font=("times new roman",18,'bold'),bg='white').place(x=20,y=260)

        txt_code=Entry(entryFrame,textvariable=self.var_regno,font=("times new roman",18),bg='white').place(x=200,y=60)

        txt_name=Entry(entryFrame,textvariable=self.var_name,font=("times new roman", 18),bg='white').place(x=200,y=110)

        txt_dept=ttk.Combobox(entryFrame,values=['CSE', 'ECE', 'MEC','CIV','EEE'],textvariable=self.var_dept,font=("times new roman",15,'bold')).place(x=200,y=160)

        txt_phno=Entry(entryFrame,textvariable=self.var_phone,font=("times new roman",18),bg='white').place(x=200,y=210) 
        txt_year=ttk.Combobox(entryFrame,values = ['1st Year','2nd Year','3rd Year', '4th Year'],textvariable=self.var_year,font=("times new roman",15)).place(x=200,y=260)
        btn_gen=Button(entryFrame,text='Generate QR',command=self.gen,font=("times new roman",18,'bold'),bg='green',fg='white').place(x=70,y=380,width=180,height=30) 
        btn_clr=Button(entryFrame,text='Clear',command=self.clr,font=("times new roman",18,'bold'),bg='red',fg='white').place(x=300,y=380,width=120,height=30)

        self.msg=""

        self.msg_label =Label(entryFrame,text=self.msg,font=("times new roman",20),bg='white',fg='green') 
        self.msg_label .place(x=0,y=320,relwidth=1)

        qrFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')

        qrFrame.place(x=600,y=100,width=550,height=450) 
        title2=Label(qrFrame,text="QR Code",font=("goudy old style", 20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        self.qrc=Label(qrFrame,text='No QR Code \nAvailable', font=('times new roman', 15),bg='#60bbf0',fg='white',bd=1,relief=RIDGE)

        self.qrc.place(x=140,y=100, width=180,height=180)
        lbl_folder=Label(qrFrame, text="Pick Location:",font=("times new roman", 18, 'bold'), bg='orange').place(x=20,y=330)

        txt_path=Entry(qrFrame,textvariable=self.download_Path,font=("times new roman", 18),bg='white').place(x=200,y=330, width=295) 
        btn_dir = Button(qrFrame,text='Choose folder', command=self.Browse, font=("times new roman", 13,'bold'), bg='purple',fg='white').place(x=200, y=380, width=180, height=20)
    
    def Browse(self):
        download_Directory=filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
        self.download_Path.set(download_Directory)
        
    def gen(self):
        if(self.var_regno.get() == '' or self.var_name.get()== '' or self.var_dept.get()=='' or self.var_phone.get()== '' or self.var_year.get()=='' ):
            self.msg = "All feilds are required!"
            self.msg_label.config(text=self.msg, fg="red")
        else:
            # updating notifications
            qr_data = (
                f"Reg No: {self.var_regno.get()}\nName:{self.var_name.get()}\nDepartment:{self.var_dept.get()}\nPhone No: {self.var_phone.get()}\nYear:{self.var_year.get()}\n")
            qr_code = qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code, [180,180])
            qr_code.save(self.download_Path.get() + ".png")
            # image adding

            self.im = ImageTk.PhotoImage(qr_code)
            self.qrc.config(image=self.im)
            self.msg = "QR Generated Successfully!"
            messagebox.showinfo("QR Code is saved successfully!")
            self.msg_label.config(text=self.msg, fg="green")

    def clr(self):
        self.var_regno.set('')
        self.var_name.set('')
        self.var_dept.set('')
        self.var_phone.set('') 
        self.var_year.set('')
        self.msg = ""
        self.msg_label.config(text=self.msg)
        self.qrc.config(image='')
        self.download_Path.set('')


root = Tk()
def about_menu():

        """About program."""

        messagebox.showinfo("Program info",'A QR code is a type of matrix barcode invented in 1994 by the Japanese automotive company Denso Wave.')

def exit_app():

    """Don't go.I love you and want to have your children, I'm rich too!.""" 
    ask_yn=messagebox.askyesno('Question', 'confirm Quit?')

    if not ask_yn:

        return

    root.destroy()

    

menu_bar = Menu(root)

file_menu=Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label='Tools', menu=file_menu)

file_menu.add_command(label='About', compound='left',  command=about_menu)
file_menu.add_separator()

file_menu.add_command(label='Exit', compound='left', command=exit_app)

root.config(menu=menu_bar)

obj = Qr(root)


root.mainloop()