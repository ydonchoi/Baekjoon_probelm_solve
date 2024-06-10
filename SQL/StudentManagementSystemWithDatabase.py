# Practice (date: 2023.12.31) (band.us@ydonchoi)
# Project: Student Management System with Database
# From. (GUI) https://youtu.be/287lnVXph6o?si=YFB5l_kBs4sCaY01
# From. (mySQL) https://youtu.be/tUc6FMPSZDg?si=lA1vCLdYqyhcUi-C

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management Sysyem")
        self.root.geometry("1350x700+0+0")
        
        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=("times new roman",40,"bold"),bg="navy",fg="white")
        title.pack(side=TOP,fill=X)

        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.Dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
                
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)
        
        m_title = Label(Manage_Frame, text="Manage Student", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        m_title.grid(row=0, columnspan=2, pady=20)
        
        lbl_roll = Label(Manage_Frame, text="Roll NO.", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        lbl_roll.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        
        txt_roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font = ('times new roman', 15, 'bold'), relief=GROOVE)
        txt_roll.grid(row=1, column=1, padx=20, pady=10, sticky='w')
        
        lbl_name = Label(Manage_Frame, text="Name", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        
        txt_name = Entry(Manage_Frame, textvariable=self.Name_var,font = ('times new roman', 15, 'bold'), relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=20, pady=10, sticky='w')

        lbl_Email = Label(Manage_Frame, text="Email", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        lbl_Email.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        
        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var,font = ('times new roman', 15, 'bold'), relief=GROOVE)
        txt_Email.grid(row=3, column=1, padx=20, pady=10, sticky='w')
        
        lbl_Gender = Label(Manage_Frame, text="Gender", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        lbl_Gender.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        
        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var,font = ('times new roman', 13, 'bold'), state='randomly')
        combo_Gender['value'] = ('male','female','others')
        combo_Gender.grid(row=4, column=1, padx=20, pady=10)     
        
        lbl_Contanct = Label(Manage_Frame, text="Contanct", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        lbl_Contanct.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        
        txt_Contact = Entry(Manage_Frame, textvariable=self.Contact_var,font = ('times new roman', 15, 'bold'), relief=GROOVE)
        txt_Contact.grid(row=5, column=1, padx=20, pady=10, sticky='w')

        lbl_Dob = Label(Manage_Frame, text="D.O.B", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        lbl_Dob.grid(row=6, column=0, padx=20, pady=10, sticky='w')
        
        txt_Dob = Entry(Manage_Frame, textvariable=self.Dob_var, font = ('times new roman', 15, 'bold'), relief=GROOVE)
        txt_Dob.grid(row=6, column=1, padx=20, pady=10, sticky='w')

        lbl_Address = Label(Manage_Frame, text="Address", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        lbl_Address.grid(row=7, column=0, padx=20, pady=10, sticky='w')

        self.txt_Address = Text(Manage_Frame, width=29, height=4, font = ('', 10), relief=GROOVE)
        self.txt_Address.grid(row=7, column=1, padx=20, pady=10, sticky='w')

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg='crimson')
        btn_Frame.place(x=15, y=515, width=410, height=55)
        
        Addbtn = Button(btn_Frame, text='Add',width=10,command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text='Update',width=10,command=self.update).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text='Delete',width=10,command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text='Clear',width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)
        
        Detail_Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Manage_Frame.place(x=500,y=100,width=800,height=580)
        
        lbl_search = Label(Detail_Manage_Frame, text="Search By", bg='crimson', fg='white', font = ('times new roman', 20, 'bold'))
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        combo_Search_By = ttk.Combobox(Detail_Manage_Frame, width=10, font = ('times new roman', 13, 'bold'), state='randomly')
        combo_Search_By['value'] = ('Roll_No','Name','Contact')
        combo_Search_By.grid(row=0, column=1, padx=20, pady=10)     
        
        txt_Search = Entry(Detail_Manage_Frame, textvariable=self.search_txt, width=20, font = ('times new roman', 15, 'bold'), relief=GROOVE)
        txt_Search.grid(row=0, column=2, padx=20, pady=10, sticky='w')

        searchbtn = Button(Detail_Manage_Frame, text='Search',width=10, height=1, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Manage_Frame, text='Show All',width=10, height=1, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
        
        Table_Frame = Frame(Detail_Manage_Frame,bd=4,relief=RIDGE,bg='crimson')
        Table_Frame.place(x=10, y=70, width=760, height=500)
                
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=('roll','name','email','gender','contact','dob','address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading('roll',text='Roll No.')        
        self.Student_table.heading('name',text='Name')        
        self.Student_table.heading('email',text='Email')        
        self.Student_table.heading('gender',text='Gender')                
        self.Student_table.heading('contact',text='Contact')        
        self.Student_table.heading('dob',text='D.O.B')        
        self.Student_table.heading('address',text='Address')        
        self.Student_table['show'] = 'headings'
        self.Student_table.column('roll',width=100)
        self.Student_table.column('name',width=100)
        self.Student_table.column('email',width=100)
        self.Student_table.column('gender',width=100)
        self.Student_table.column('contact',width=100)
        self.Student_table.column('dob',width=100)
        self.Student_table.column('address',width=100)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=='' or self.Name_var.get()=='' or self.Contact_var.get()=='' or self.Dob_var.get()=='':
            messagebox.showerror('Error','All fields are required to insert.')
        else:
            con=pymysql.connect(host='localhost', user='root',password='12345',database='stm')
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.Name_var.get(),
                                                                            self.Email_var.get(),
                                                                            self.Gender_var.get(),
                                                                            self.Contact_var.get(),
                                                                            self.Dob_var.get(),
                                                                            self.txt_Address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo('Insert Success', 'Necessary Fields are inserted.')
        
    def fetch_data(self):
        con=pymysql.connect(host='localhost', user='root',password='12345',database='stm')
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set('')
        self.Name_var.set('')
        self.Email_var.set('')
        self.Gender_var.set('')
        self.Contact_var.set('')
        self.Dob_var.set('')
        self.txt_Address.delete('1.0',END)

    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.Dob_var.set(row[5])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[6])
        
    def update(self):
        con=pymysql.connect(host='localhost', user='root',password='12345',database='stm')
        cur = con.cursor()
        cur.execute("update students set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll_no=%s",(self.Name_var.get(),self.Email_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.Dob_var.get(),self.txt_Address.get('1.0',END),self.Roll_No_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    def delete(self):
        con=pymysql.connect(host='localhost', user='root',password='12345',database='stm')
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        
    def search_data(self):
        con=pymysql.connect(host='localhost', user='root',password='12345',database='stm')
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    
        
root = Tk()
ob = Student(root)
root.mainloop()
                
        
