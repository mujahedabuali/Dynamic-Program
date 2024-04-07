from sre_parse import State
import stat
import tkinter as tk 
from tkinter import NORMAL, filedialog
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import random 
from PIL import Image

#For make Main page
class page2(ctk.CTkFrame):
    def __init__(self, root, controller):
        ctk.CTkFrame.__init__(self, root)
        self.controller = controller
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        #design shape in form
        frame=ctk.CTkFrame(self, width=2000, height=2000)
        
        label = ctk.CTkLabel(frame,text="Home",font=("Times", 30, "bold"))
        
        label1 = ctk.CTkLabel(frame, text="# of Power Source:",font=("Arial", 16, "bold"))
        self.entry1 = ctk.CTkEntry(frame,placeholder_text="eg.3", width=200,border_width=4, corner_radius=20,validate="key",font=("Arial",16))
        
        self.img1 = ctk.CTkImage(Image.open("img/writing.png"),size=(30,30))
        Btn=ctk.CTkButton(frame,text="Manual",command = self.set_entry2,cursor='hand2',image=self.img1, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
        
        self.img2 = ctk.CTkImage(Image.open("img/folder.png"),size=(30,30))
        Btn2=ctk.CTkButton(frame,text="File",command= self.read_from_file,cursor='hand2',image=self.img2, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))
        
        self.img3 = ctk.CTkImage(Image.open("img/dices.png"),size=(30,30))
        Btn3=ctk.CTkButton(frame,text="Random",command= self.random_data,cursor='hand2',image=self.img3, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))

        label2 = ctk.CTkLabel(frame, text="Order of LEDs:",font=("Arial", 16, "bold"))
        self.entry2 = ctk.CTkEntry(frame, width=200,placeholder_text="eg.<2,3,1>",border_width=4, corner_radius=20,font=("Arial",16))
       
        self.img4 = ctk.CTkImage(Image.open("img/led-light2.png"),size=(30,30))
        self.button1 = ctk.CTkButton(frame,text="Result",command=self.goto_result,cursor='hand2',image=self.img4, compound="left",corner_radius=10,font=ctk.CTkFont(size=15, weight="bold"))

        self.img5 = ctk.CTkImage(Image.open("img/back.png"),size=(30,30)) 
       
        self.img = tk.PhotoImage(file='img/img2.png')
        image_label = tk.Label(frame,image=self.img,width=680,height=370)

        self.infoLabel = ctk.CTkLabel(frame, text="",text_color="RED",font=("Arial", 16, "bold"))

        #place entity in page
        label.place(x=758,y=20)
        label1.place(x=525,y=120)
        self.entry1.place(x=790,y=120)
        Btn.place(x=1040,y=115)
        Btn3.place(x=1200,y=115)
        label2.place(x=525,y=220)
        self.entry2.place(x=790,y=220)
        Btn2.place(x=1040,y=215)
        self.button1.place(x=825,y=300)
        image_label.place(x=550,y=440)
        self.infoLabel.place(x=790,y=400)

        frame.pack()

     #action button function
    def set_entry2(self):
        try:
            num = int(self.entry1.get())
            if(num>0 and num <520):            
                result = '<' + ',' * (num-1) + '>'#O(n)
                self.entry2.delete(0, tk.END)
                self.entry2.insert(0, result)
                self.infoLabel.configure(text="")
            else:  raise ValueError()        
        except ValueError:
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.infoLabel.configure(text="Error when input!!!")
    
    #to check input data and go to results page O(n log n)
    def goto_result(self):
        try:
            self.n = int(self.entry1.get())
            self.infoLabel.configure(text="")
            if self.n <= 0: raise ValueError
            
            str1 = self.entry2.get().replace("<", "").replace(">", "").replace(" ", "")

            # O(n)
            self.numbers=[]
            for num in str1.split(','):
                self.numbers.append(int(num))

            if self.n != len(self.numbers): raise ValueError 
            
            arr=self.numbers[:]
            # O(n log n)           
            quick_sort(arr, 0, len(arr) - 1)
            # O(n)
            for i in range(len(arr)):
                if arr[i] <= 0 or arr[i] > self.n or arr[i] == arr[i-1]:
                    raise ValueError

            self.controller("Page3",self.n,self.numbers)              
        except ValueError:
             self.infoLabel.configure(text="Error when input!!!")

    # To read data order from file O(n log n)
    def read_from_file(self):
     fileP = filedialog.askopenfilename(title="Select a file",initialdir='C:\\Users\\Lenovo\\OneDrive\\Desktop\\Algo\\proj1',filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
     if fileP:
        with open(fileP, 'r') as file:
            try: 
                 # O(n)     
                 n = int(file.readline().strip())
                 arr = [int(i) for i in file.readline().strip().split(' ')]

                 if(len(arr) != n): raise ValueError
                 
                 arr2=arr[:]
                 # O(n log n)           
                 quick_sort(arr2, 0, len(arr2) - 1)

                 # O(n)
                 for i in range(len(arr2)):
                    if arr2[i] <= 0 or arr2[i] > n or arr2[i]== arr2[i-1]:
                        raise ValueError
                 self.infoLabel.configure(text="")
                 self.controller("Page3", n, arr)
        
            except ValueError:
             self.infoLabel.configure(text="Error when input!!!")
           
    # To set order of LEDs random o(n)
    def random_data(self):
        try :
             n = int(self.entry1.get())
             if n > 0 and n <600:
                r=random.sample(range(1,n+1),n)
                str1 = ""
                for i in r:
                    str1 += str(i) + ", "
                str1 = str1.rstrip(", ") 
        
                self.entry2.delete(0, tk.END)
                self.entry2.insert(0, f"<{str1}>")
                self.infoLabel.configure(text="")

             else: raise ValueError
               
        except ValueError:
             self.infoLabel.configure(text="Error when input!!!")
                        

#O(nlogn)
def quick_sort(arr, low, high):
  if low < high:
    pi = pivot(arr, low, high)

    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)

def pivot(arr, low, high):
  pivot = arr[high]
  i = (low - 1)

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return (i + 1)


