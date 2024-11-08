from tkinter import*
#from PIL import ImageTk 
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root= root
        self.root.title("Heart Desease Prediction")
        root.geometry('1200x600')
        root.iconbitmap('heartIcon.ico')
        self.root.resizable(False,False)

        #--------------Image---------------
        #self.bg=ImageTk.PhotoImage(file="Images/25531.jpg")
        #self.bg=PhotoImage(file="Images\heart1.png")
        #self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=10)


        #---------------Login-----------------
        Frame_login=Frame(self.root,bg="white").place(x=150,y=150,height=340,width=500)

        title = Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=160,y=160)
        lbl_user = Label(Frame_login,text="User Name",font=("times new roman",15),fg="black",bg="white").place(x=165,y=280)
        self.txt_user=Entry(Frame_login,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_user.place(x=280,y=280,width=350,height=35)

        #----------------Password----------------
        lbl_pass = Label(Frame_login,text="Password",font=("times new roman",15),fg="black",bg="white").place(x=165,y=340)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15,"bold"),bg="lightgray",show="*")
        self.txt_pass.place(x=280,y=340,width=350,height=35)

        #--------------Forgot Password Button-----------
        forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=162,y=390)

        #-----------------Login Button-------------------
        Login_btn=Button(self.root,command=self.login_fun,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=330,y=450)
    
    def login_fun(self):
        
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.txt_user.get()!= "Suraj" :
            messagebox.showerror("Error","Invalid Username",parent=self.root)
        if self.txt_pass.get()!="123456":
            messagebox.showerror("Error","Invalid Password",parent=self.root)
         
        else:
            messagebox.showinfo("Welcome",f"Welcome{self.txt_user.get()}",parent=self.root)

    

       
    
root = Tk()
obj=Login(root)
root.mainloop()