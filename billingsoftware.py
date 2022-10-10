from tkinter import*
import math,random,os
from tkinter import messagebox
root= Tk()
class Bill_App:
    def __init__(self,root):

        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        label1 = "gold"
        label2 = "white"
        label3 = "white"

        title = Label(self.root,text="BILLING SOFTWARE",fg="white",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #======= variables==================================
        
        
        #=========cosmetics==========================
        self.soap = IntVar()
        self.sunscreen = IntVar()
        self.facewash= IntVar()
        self.h_cond= IntVar()
        self.h_oil= IntVar()
        self.lotion= IntVar()

        #=======grocery===============
        self.rice= IntVar()
        self.wheat= IntVar()
        self.daal= IntVar()
        self.f_oil= IntVar()
        self.sugar= IntVar()
        self.tea= IntVar()
        #=======beverage===============
        self.pepsi= IntVar()
        self.coke= IntVar()
        self.maza= IntVar()
        self.mirinda= IntVar()
        self.sprite= IntVar()
        self.fanta= IntVar()
        #=========total price======================
        self.cosemtics_price= StringVar()
        self.grocery_price= StringVar()
        self.beverage_price= StringVar()

        self.cosemtics_tax= StringVar()
        self.grocery_tax= StringVar()
        self.beverage_tax= StringVar()
        #========Customer=======================
        self.c_name= StringVar()
        self.c_phone= StringVar()
        x = random.randint(1000,9999)
        self.bill_no= StringVar()
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        F1 = LabelFrame(self.root,text="Customer Details",bd=10,font=("times new roman",15,"bold"),fg=label1,bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        #============= customer detail frame=================
        cname = Label(F1,text="Customer Name",bg=bg_color,fg=label2,font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_input = Entry(F1,width=15,textvariable= self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphone = Label(F1,text="Phone Number",bg=bg_color,fg=label2,font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_input = Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        cbill = Label(F1,text="Bill No",bg=bg_color,fg=label2,font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_input = Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn = Button(F1,text="Search",command=self.find_bill,bg="cadetblue",fg="white",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

       #============= Cosmetic Frame ====================================
        F2 = LabelFrame(self.root,text="Cosmetics",bd=10,font=("times new roman",15,"bold"),fg=label1,bg=bg_color)
        F2.place(x=0,y=180,width=325,height=380)

        bath_lb = Label(F2,text="Bath Soap",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        sunscreen_lb = Label(F2,text="Sun Screen",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        sunscreen_txt = Entry(F2,width=10,textvariable=self.sunscreen,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_wash_lb = Label(F2,text="Face Wash",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash_txt = Entry(F2,width=10,textvariable=self.facewash,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
 
        h_cond_lb = Label(F2,text="Hair Conditioner",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        h_cond_txt = Entry(F2,width=10,textvariable=self.h_cond,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        h_oil_lb = Label(F2,text="Hair Oil",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        h_oil_txt = Entry(F2,width=10,textvariable=self.h_oil,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        b_loct_lb = Label(F2,text="Body Loction",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        b_loct_txt = Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
       #============= Food Grain Frame ====================================
        F3 = LabelFrame(self.root,text="Food Grain Per Kg",bd=10,font=("times new roman",15,"bold"),fg=label1,bg=bg_color)
        F3.place(x=330,y=180,width=325,height=380)

        rice_lb = Label(F3,text="Rice",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt = Entry(F3,width=10,textvariable=self.rice,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        wheat_lb = Label(F3,text="Wheat",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        wheat_txt = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        daal_lb = Label(F3,text="Daal",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_txt = Entry(F3,width=10,textvariable=self.daal,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
 
        food_oil_lb = Label(F3,text="Food Oil",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        food_oil_txt = Entry(F3,width=10,textvariable=self.f_oil,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        sugar_lb = Label(F3,text="Sugar",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_txt = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_lb = Label(F3,text="Tea",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        tea_txt = Entry(F3,width=10,textvariable=self.tea,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
       #============= Beverage Frame ====================================
        F4 = LabelFrame(self.root,text="Beverage Per Litre",bd=10,font=("times new roman",15,"bold"),fg=label1,bg=bg_color)
        F4.place(x=660,y=180,width=325,height=380)

        pepsi_lb = Label(F4,text="Pepsi",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        pepsi_txt = Entry(F4,width=10,textvariable=self.pepsi,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        coke_lb = Label(F4,text="Coka Cola",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coke_txt = Entry(F4,width=10,textvariable=self.coke,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        maza_lb = Label(F4,text="Maza",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        maza_txt = Entry(F4,width=10,textvariable=self.maza,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
 
        sprite_lb = Label(F4,text="Sprite",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sprite_txt = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        fanta_lb = Label(F4,text="Fanta",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        fanta_txt = Entry(F4,width=10,textvariable=self.fanta,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        mirinda_lb = Label(F4,text="Mirinda",bg=bg_color,fg=label3,font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        mirinda_txt = Entry(F4,width=10,textvariable=self.mirinda,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
    
        #===================== Bill area ===========================
        F5 = Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=995,y=180,width=350,height=380)
        
        bill_lbl = Label(F5,text="BILL SECTION",font="arail 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #==================== Button Frame ==========================

        F6 = LabelFrame(self.root,text="Bill Menu",bd=10,font=("times new roman",15,"bold"),fg=label1,bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text='Total Cosmetic Price',bg=bg_color,fg=label2,font=('times new roman',14,'bold')).grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt=Entry(F6,width=15,font='arial 11 bold',textvariable=self.cosemtics_price,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text='Total Food Grain  Price',bg=bg_color,fg=label2,font=('times new roman',14,'bold')).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        m2_txt=Entry(F6,width=15,font='arial 11 bold', textvariable=self.grocery_price,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text='Total Beverage Price',bg=bg_color,fg=label2,font=('times new roman',14,'bold')).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        m3_txt=Entry(F6,width=15,font='arial 11 bold',textvariable=self.beverage_price ,bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)



        c1_lbl=Label(F6,text=' Cosmetic Tax',bg=bg_color,fg=label2,font=('times new roman',14,'bold')).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        c1_txt=Entry(F6,width=15,font='arial 11 bold',textvariable=self.cosemtics_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text=' Food Grain  Tax',bg=bg_color,fg=label2,font=('times new roman',14,'bold')).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        c2_txt=Entry(F6,width=15,font='arial 11 bold',textvariable=self.grocery_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text=' Beverage Tax',bg=bg_color,fg=label2,font=('times new roman',14,'bold')).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        c3_txt=Entry(F6,width=15,textvariable=self.beverage_tax,font='arial 11 bold',bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)

        total_btn=Button(btn_f,command =self.total,text='Total',bg='cadetblue',fg='White',bd=2,pady=15,width=10,font='arial 15 bold').grid(row=0,column=0,padx=5,pady=5)

        GBill_btn=Button(btn_f,text='Generate Bill',command=self.bill_area,bg='cadetblue',fg='White',bd=2,pady=15,width=10,font='arial 15 bold').grid(row=0,column=1,padx=5,pady=5)

        Clear_btn=Button(btn_f,text='Clear',command=self.clear_data,bg='cadetblue',fg='White',bd=2,pady=15,width=10,font='arial 15 bold').grid(row=0,column=2,padx=5,pady=5)

        Exit_btn=Button(btn_f,text='Exit',command=self.Exit_app,bg='cadetblue',fg='White',bd=2,pady=15,width=10,font='arial 15 bold').grid(row=0,column=3,padx=5,pady=5)

        self.welcome_bill()
    
    
        
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_ss_p=self.sunscreen.get()*120
        self.c_fw_p=self.facewash.get()*60
        self.c_hc_p=self.h_cond.get()*180
        self.c_ho_p=self.h_oil.get()*140
        self.c_l_p=self.lotion.get()*180
        self.total_cosemtics_price=float(
                                   self.c_s_p+
                                   self.c_ss_p+
                                   self.c_fw_p+
                                   self.c_hc_p+
                                   self.c_ho_p+
                                   self.c_l_p
                                )
        self.cosemtics_price.set("Rs. " +str(self.total_cosemtics_price))
        self.c_tax=round((self.total_cosemtics_price*0.05),2)
        self.cosemtics_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.f_oil.get()*180
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price=float(
                                   self.g_r_p+
                                   self.g_fo_p+
                                   self.g_d_p+
                                   self.g_w_p+
                                   self.g_s_p+
                                   self.g_t_p                                   
                               )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.b_m_p=self.maza.get()*60
        self.b_c_p=self.coke.get()*60
        self.b_f_p=self.fanta.get()*40
        self.b_p_p=self.pepsi.get()*45
        self.b_mi_p=self.mirinda.get()*40
        self.b_s_p=self.sprite.get()*60
        self.total_beverage_price=float(
                                   self.b_m_p+
                                   self.b_c_p+
                                   self.b_f_p+
                                   self.b_p_p+
                                   self.b_mi_p+
                                   self.b_s_p
                                   )
        self.beverage_price.set("Rs. " + str(self.total_beverage_price))
        self.b_tax=round((self.total_beverage_price*0.05),2)
        self.beverage_tax.set("Rs. "+str(self.b_tax))

        self.Total_bill=float(  self.total_cosemtics_price+
                                self.total_grocery_price+
                                self.total_beverage_price+
                                self.c_tax+
                                self.g_tax+
                                self.b_tax                                
                            )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Retail Shop\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n=====================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n=====================================")

    def bill_area(self):        
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosemtics_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.beverage_price.get()=="Rs. 0.0" :
            messagebox.showerror("Error","No Product Selected or Purchased")
        else:
            self.welcome_bill()
            #======costmetics==============
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.sunscreen.get()!=0:
                self.txtarea.insert(END,f"\n SunScreen\t\t{self.sunscreen.get()}\t\t{self.c_ss_p}")
            if self.facewash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.facewash.get()}\t\t{self.c_fw_p}")
            if self.h_cond.get()!=0:
                self.txtarea.insert(END,f"\n Hair Conditioner\t\t{self.h_cond.get()}\t\t{self.c_hc_p}")
            if self.h_oil.get()!=0:
                self.txtarea.insert(END,f"\n Hair Oil\t\t{self.h_oil.get()}\t\t{self.c_ho_p}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_l_p}")

            #=======Grocery==================
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.f_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.f_oil.get()}\t\t{self.g_fo_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            #========Drinks======================
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.b_m_p}")
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t\t{self.b_c_p}")
            if self.fanta.get()!=0:
                self.txtarea.insert(END,f"\n Fanta\t\t{self.fanta.get()}\t\t{self.b_f_p}")
            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.b_p_p}")
            if self.mirinda.get()!=0:
                self.txtarea.insert(END,f"\n Mirinda\t\t{self.mirinda.get()}\t\t{self.b_mi_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.b_s_p}")


            self.txtarea.insert(END,f"\n-------------------------------------")
            if self.cosemtics_tax.get()!="Rs 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosemtics_tax.get()}")
            if self.grocery_tax.get()!="Rs 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.beverage_tax.get()!="Rs 0.0":
                self.txtarea.insert(END,f"\n Beverage Tax\t\t\t{self.beverage_tax.get()}")
            
            self.txtarea.insert(END,f"\n Total Bill : \t\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END,f"\n-------------------------------------")
            self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.bill_no.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:           
            #=========cosmetics==========================
            self.soap.set(0)
            self.sunscreen.set(0)
            self.facewash.set(0)
            self.h_cond.set(0)
            self.h_oil.set(0)
            self.lotion.set(0)

            #=======grocery===============
            self.rice.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.f_oil.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #=======beverage===============
            self.pepsi.set(0)
            self.coke.set(0)
            self.maza.set(0)
            self.mirinda.set(0)
            self.sprite.set(0)
            self.fanta.set(0)
            #=========total price======================
            self.cosemtics_price.set("")
            self.grocery_price.set("")
            self.beverage_price.set("")

            self.cosemtics_tax.set("")
            self.grocery_tax.set("")
            self.beverage_tax.set("")
            #========Customer=======================
            self.c_name.set("")
            self.c_phone.set("")
            x = random.randint(1000,9999)
            self.bill_no.set("")
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()            
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


obj = Bill_App(root)
root.mainloop()
