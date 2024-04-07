import tkinter as tk
import customtkinter as ctk
from PIL import Image

#For make results page
class page4(ctk.CTkFrame):   
    def __init__(self, root, controller):
         ctk.CTkFrame.__init__(self, root)
         self.controller = controller
         ctk.set_appearance_mode("dark")
         ctk.set_default_color_theme("green")
        
         #design shape in form
         self.canvas = ctk.CTkCanvas(self,width=35000, height=1200, scrollregion=(0, 0, 35000,500),highlightthickness=0)
         h_scro = ctk.CTkScrollbar(self, orientation="horizontal", command=self.canvas.xview,width=800)
         h_scro.place(x=490, y=970)
         self.canvas.configure(xscrollcommand=h_scro.set)

         self.frame=ctk.CTkFrame(self.canvas, width=35000, height=1200) 
         self.canvas2 = ctk.CTkCanvas(self.frame, width=35000, height=420,highlightthickness=0,bg="#2b2b2b")
        
         self.label =ctk.CTkLabel(self.frame, text="Graphic Page",font=("Times", 30, "bold")) 
         self.label.place(x=710,y=20)
         
         self.img5 = ctk.CTkImage(Image.open("img/back.png"),size=(30,30)) 
         self.button = ctk.CTkButton(self.frame,text="Back",cursor='hand2',command=self.back,image=self.img5, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
         self.button.place(x=20,y=20)

         self.img1 = ctk.CTkImage(Image.open("img/led-light2.png"),size=(60,60))
         self.img2 = ctk.CTkImage(Image.open('img/led-light.png'),size=(60,60))
         self.img3 = ctk.CTkImage(Image.open('img/power.png'),size=(50,50))

         self.canvas.create_window((0, 0), window=self.frame,anchor="nw")

    def back(self):
         self.canvas2.destroy()
         self.canvas2 = ctk.CTkCanvas(self.frame, width=1525, height=200,highlightthickness=0,bg="#222222")
         self.controller("Page3")
   
    #method to get data form page3 "n,order,result" and display it
    def get_data2(self, order, numPower,result):
         self.n=order#order
         self.r=result#result
         self.v=numPower
         
         #set leds and power source at center of page
         if self.v % 2 == 0:
            center_x = 750
         else:
            center_x = 720
        
         #draw power source o(n)
         pox_x=[] 
         for i in range(1,self.v+1) :
          if(self.v <=21):
            x_axis1=center_x + (i - (self.v) / 2) * 70
          else: x_axis1=60+(i-1)*80

          ctk.CTkLabel(self.frame,text=str(i)).place(x=x_axis1+22,y=535)
          px=ctk.CTkLabel(self.frame,image=self.img3,text="")
          px.place(x=x_axis1,y=490)
          pox_x.append(px.place_info()['x'])
        
         #display a order of LEDs o(n)
         num_order=len(self.n)
         for i in range(1,num_order+1) :
            if(self.v <=21):
               x_axis1=center_x + (i - (self.v) / 2) * 70
            else: x_axis1=60+(i-1)*80
            ctk.CTkLabel(self.frame,text=self.n[i-1]).place(x=x_axis1+22,y=270)
         
         #disply a LEDs  o(n) 
         for i in range(1,self.v+1):   
            if(self.v <=21):
               x_axis1=center_x + (i - (self.v) / 2) * 70
            else: x_axis1=60+(i-1)*80

            if self.n[i-1] in self.r :
                led=ctk.CTkLabel(self.frame,image=self.img1,text="")
                led.place(x=x_axis1,y=300)
                x=int(led.place_info()['x'])
                self.canvas2.create_line(x+30, 12, int(pox_x[self.n[i-1]-1])+30, 150, fill="yellow")
            else:
                ctk.CTkLabel(self.frame,image=self.img2,text="").place(x=x_axis1,y=300)
         
         #place entity in page
         self.canvas2.place(x=0,y=350)
         self.canvas.pack()
                