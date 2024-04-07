import tkinter as tk
import customtkinter as ctk
from Page2 import page2
from Page3 import page3
from Page3 import dpTable
from Page4 import page4
from PIL import Image

#For make Welcome page      
class page1(ctk.CTkFrame):
    def __init__(self, root, controller):
        ctk.CTkFrame.__init__(self, root)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Welcome to our application, Max LED Lighting",font=("Times", 30, "bold")) 
        label.pack(side="top",pady=20)

        self.img = tk.PhotoImage(file='img/img1.png')
        my_image_label = tk.Label(self,image=self.img,width=800,height=400).pack()

        self.img1 = ctk.CTkImage(Image.open("img/arrow.png"),size=(40,40))

        button = ctk.CTkButton(self,text="Enter",cursor='hand2',image=self.img1, compound="left",corner_radius=10,font=ctk.CTkFont(size=20, weight="bold"),width=220,height=40,command=lambda:self.controller("Page2"))
        button.pack(side="bottom",pady=5,expand=True)

#to connect pages and move between them
class main():
    def __init__(self,root):
        self.root=root
        self.root.title("Max LED Lighting")
        self.root.geometry("1600x2000")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.pages = {}
        self.pages["Page1"] = page1(self.root, self.show_page)
        self.pages["Page2"] = page2(self.root, self.show_page)
        self.pages["Page3"] = page3(self.root, self.show_page)
        self.pages["Page4"] = page4(self.root, self.show_page)
        self.pages["dpTable"] = dpTable(self.root, self.show_page)

        self.show_page("Page1")

    def show_page(self, page_name,*args):
        for page in self.pages.values():
            page.pack_forget()
           
        page=self.pages[page_name]
        page.pack(expand=True,fill="both") 

        if page_name == "dpTable" : page.printDP(*args)  
        if page_name == "Page3" and len(args) == 2 : page.get_data(*args)  
        if page_name == "Page4" and len(args) == 3 : page.get_data2(*args)  
            

if __name__ == "__main__":
     root = ctk.CTk()
     app = main(root)
     root.mainloop()

