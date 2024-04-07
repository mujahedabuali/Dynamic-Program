import tkinter as tk
from tkinter import Scrollbar,filedialog,messagebox
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from MaxLED_Lighting_Algo import MaxLED_Lighting
from PIL import Image
from algo import LED_Lighting

#For make results page
class page3(ctk.CTkFrame):   
    def __init__(self, root, controller):
         ctk.CTkFrame.__init__(self, root)
         self.controller = controller
         ctk.set_appearance_mode("dark")
         ctk.set_default_color_theme("green")

         #design shape in form
         self.canvas = tk.Canvas(self, width=10000, height=2000, scrollregion=(0, 0, 10000,500),highlightthickness=0)

         h_scro = ctk.CTkScrollbar(self,width=800,orientation="horizontal", command=self.canvas.xview)
         h_scro.place(x=520, y=970)
         self.canvas.configure(xscrollcommand=h_scro.set)

         frame=ctk.CTkFrame(self.canvas, width=10000, height=2000)   
         
         label = ctk.CTkLabel(frame, text="Results Page",font=("Times", 30, "bold")) 

         label2 = ctk.CTkLabel(frame, text="# of Power Source:",font=("Times", 17, "bold")) 
         self.label3= ctk.CTkLabel(frame, text="",font=("Times", 16, "bold")) 
         label4 = ctk.CTkLabel(frame, text="Order of LEDs:",font=("Times", 17, "bold")) 
         self.label5= ctk.CTkLabel(frame, text="",font=("Times", 16, "bold"))         

         label6 = ctk.CTkLabel(frame, text="Maximum # of LEDs :",font=("Times", 17, "bold")) 
         self.label7= ctk.CTkLabel(frame, text="",font=("Times", 16, "bold")) 
         
         label8 = ctk.CTkLabel(frame, text="Suggested LEDs :",font=("Times", 17, "bold")) 
         self.label9= ctk.CTkLabel(frame, text="",font=("Times", 17, "bold"))
         
         label10 = ctk.CTkLabel(frame, text="DP Table :",font=("Times", 17, "bold")) 
         self.text_box = ctk.CTkTextbox(frame, wrap=tk.WORD,width=360,height=275) 
         dpButton = ctk.CTkButton(frame,text="View clearly",command=lambda:self.controller("dpTable",self.text_box.get(1.0,tk.END)))
         
         self.img5 = ctk.CTkImage(Image.open("img/back.png"),size=(30,30)) 
         button = ctk.CTkButton(frame,text="Back",cursor='hand2',command=lambda:self.controller("Page2"),image=self.img5, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
         
         self.img1 = ctk.CTkImage(Image.open("img/printer.png"),size=(30,30)) 
         button2 = ctk.CTkButton(frame,text="Print",cursor='hand2',command=self.print_data,image=self.img1, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))

         self.img2 = ctk.CTkImage(Image.open("img/color-palette.png"),size=(30,30)) 
         self.button3 = ctk.CTkButton(frame,text="Draw",cursor='hand2',image=self.img2, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
         
        #place entity in page
         button.place(x=20,y=20)
         label.place(x=710,y=20)
         
         label2.place(x=520,y=120)
         self.label3.place(x=705,y=120)
         
         label4.place(x=830,y=120)
         self.label5.place(x=970,y=120)

         label6.place(x=630,y=220)
         self.label7.place(x=835,y=220)

         label8.place(x=630,y=270)
         self.label9.place(x=805,y=270)

         label10.place(x=630,y=330)
         dpButton.place(x=750,y=330)
         self.text_box.place(x=710,y=390)

         button2.place(x=685,y=700)
         self.button3.place(x=845,y=700)

         self.canvas.create_window((0, 0), window=frame,anchor="nw")
         self.canvas.pack()

    #method to get data form page2 "n,order" and display it
    def get_data(self, v1, v2):
        self.label3.configure(text=f"{v1}")
        self.label5.configure(text=f"{v2}")

        self.maxLeds = MaxLED_Lighting(v1, v2)  
        exp_result,opt_leds,dp_table= self.maxLeds.print_res() 
        
        opt_leds,exp_result,dp_table=LED_Lighting(v2)

        self.label7.configure(text=f"{exp_result}")
        self.label9.configure(text=f"{opt_leds}")
       
        self.text_box.configure(state=tk.NORMAL)
        self.text_box.delete(1.0,tk.END)
        self.text_box.insert(1.0,dp_table)
        self.text_box.configure(state=tk.DISABLED)

        # split_first_solu = [i.strip() for i in opt_leds.split(',')]
        # solu = split_first_solu[0].replace("'", "").strip()
        # arr = [int(value) for value in solu.split()]
        self.button3.configure(command=lambda:self.controller('Page4',v2,v1,opt_leds))

    #method for print result data in file 
    def print_data(self):
          try:
             fileP = filedialog.asksaveasfilename(title="Select a file",initialdir='C:\\Users\\Lenovo\\OneDrive\\Desktop\\Algo\\proj1',filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
             with open(fileP, 'w') as file:     
                 file.write(f"# of Power Source: {self.label3.cget('text')} \n") 
                 file.write(f"Order of LEDs: {self.label5.cget('text')} \n") 
                 file.write(f"Maximum # of LEDs : {self.label7.cget('text')} \n") 
                 file.write(f"Suggested LEDs : {self.label9.cget('text')} \n") 
                 file.write(f"DP Table : {self.text_box.get(1.0,tk.END)}")
                 messagebox.showinfo("Done",f"Done Its printed in {fileP.split('/')[-1]}")

          except ValueError:
                CTkMessagebox(title="Invalid Input", message="There is a problem in your file!!!", icon="warning") 

class dpTable(ctk.CTkFrame):
    def __init__(self, root, controller):
        ctk.CTkFrame.__init__(self, root)
        self.controller = controller
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        
        canvas = ctk.CTkCanvas(self,width=15000, height=15000, scrollregion=(0, 0, 25000, 25000),highlightthickness=0)
        canvas.place(x=0,y=0)

        v_scro = Scrollbar(self, orient="vertical", command=canvas.yview)
        v_scro.place(x=1580,y=150,height=600)

        h_scro = Scrollbar(self, orient="horizontal", command=canvas.xview)
        h_scro.place(x=520, y=970, width=800)
        
        canvas.configure(yscrollcommand=v_scro.set, xscrollcommand=h_scro.set)
        canvas.configure(background="black")

        frame= ctk.CTkFrame(canvas, width=15000, height=15000)   
 
        self.label2 = ctk.CTkLabel(frame,font=("Times", 16, "bold")) 
        
        self.img5 = ctk.CTkImage(Image.open("img/back.png"),size=(30,30)) 
        button = ctk.CTkButton(frame,text="Back",cursor='hand2',command=lambda:self.controller("Page3"),image=self.img5, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
        button.place(x=20,y=20)

        canvas.create_window((0, 0), window=frame,anchor="nw")
     
    def printDP(self,t):

        text = t.split('\n\n')
        ftext="Table of Valuse: \n"
        ftext+=text[0]

        self.label2.place(x=400,y=150) 
        self.label2.configure(text=f"{ftext}")