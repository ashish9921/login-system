from tkinter import*
from PIL import  Image ,ImageTk
from tkinter import messagebox
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        self.bg_icon=ImageTk.PhotoImage(Image.open("bg.jpeg"))
        self.logo_icon=ImageTk.PhotoImage(Image.open("logo.jpeg"))
        self.lock_icon=PhotoImage(file="lock.png")
        self.user_icon=ImageTk.PhotoImage(file="user.png")
        
        self.Uname=StringVar()
        self.pass_=StringVar()

        
        
        
        bg_lbl=Label(image=self.bg_icon).pack()
        
        
        

        title=Label(self.root,text="login System",font=("times new roman",40,"bold"),bg="yellow",bd=10,fg="red",relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        
        loging_frame=Frame(bg="white")
        
        loging_frame.place(x=400,y=150)
        
        logolable=Label(loging_frame,image=self.logo_icon,bd=0,bg="white").grid(row=0,columnspan=2,pady=20)
        
        lbluser=Label(loging_frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,pady=10)
        txtuse=Entry(loging_frame,bd=5,textvariable=self.Uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,pady=20)
        
        lblpass=Label(loging_frame,text="PassWord",image=self.lock_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,pady=10)
        txtpass=Entry(loging_frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("",15)).grid(row=2,column=1,pady=20)
        
        btn_lof=Button(loging_frame,text="login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)


    def login(self):
        if self.Uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("error","All the filds requird!!")
        elif self.Uname.get()=="Ashish" and self.pass_.get()=="123":
            messagebox.showinfo("successfull",f"Welcome{self.Uname.get()}")
        else:
            messagebox.showerror("error","Invalid Username or password")
        
root=Tk()
obj=Login_System(root)
root.mainloop()