from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

root = Tk()

root.title("Rdonalds")
root.geometry("900x500")

burger = ImageTk.PhotoImage(Image.open("burger1.png"))

lbl_img = Label(root)
lbl_img["image"]=burger
lbl_img.place(relx=0.7,rely=0.5,anchor=CENTER)

lbl_heading = Label(root,text="Rdonalds",font=("times",40,"bold"),fg="Red")
lbl_heading.place(relx=0.12,rely=0.1,anchor=CENTER)

lbl_select_dish = Label(root,text="Select Dish: ",font=("times",15))
lbl_select_dish.place(relx=0.06,rely=0.2,anchor=CENTER)

dish = ["Burger","Iced_Americano"]
dish_dd = ttk.Combobox(root,state="readonly",values=dish)
dish_dd.place(relx=0.25,rely=0.2)

lbl_addons = Label(root,text="Select Addons: ",font=("times",15))
lbl_addons.place(relx=0.08,rely=0.5,anchor=CENTER)

toppings_list = []
toppings_dd = ttk.Combobox(root,state="readonly",values=toppings_list)
toppings_dd.place(relx=0.25,rely=0.5,anchor=CENTER)

dish_amount = Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2,rely=0.75,anchor=CENTER)

class ParentClass():
    def __init__(self):
        print("This is a parent class")
        
    def menu(dish):
        if dish=="Burger":
            print("You can add following toppings")
            toppings=["Cheese","Jalapenos"]
            toppings_dd["values"]=toppings
            print("More cheese | Add jalapeno")
        elif dish=="Iced_Americano":
            toppings=["Chocolate_flavour","Caramel_flavour"]
            toppings_dd["values"]=toppings
            print("Add chocolate flavour | Add caramel flavour")
        else:   
            print("please enter valid dish")
            
    def final_amount(dish,addons):
        if(dish == "Burger" and addons == "Cheese"):
            dish_amount["text"]="You need to pay 250 USD"
            
        elif(dish == "Burger" and addons == "Jalapenos"):
            dish_amount["text"]="You need to pay 350 USD"
            
        elif(dish == "Iced_Americano" and addons == "Chocolate_flavour"):
            dish_amount["text"]="You need to pay 250 USD"
            
        elif(dish == "Iced_Americano" and addons == "Caramel_flavour"):
            dish_amount["text"]="You need to pay 450 USD"
            
class Child1(ParentClass):
    def __init__(self,dish):
        self.new_dish = dish
        
    def getMenu(self):
        new_dish = dish_dd.get()
        ParentClass.menu(new_dish)
        
class Child2(ParentClass):
    def __init__(self,dish,toppings):
        self.new_dish = dish
        self.toppings = toppings
        
    def getFinalAmount(self):
        new_dish = dish_dd.get()
        toppings = toppings_dd.get()
        ParentClass.final_amount(new_dish,toppings)
        

child1_obj = Child1(dish_dd.get())
child1_obj.getMenu()

child2_obj = Child2(toppings_dd.get(),dish_dd.get())
child2_obj.getFinalAmount()

btn_amount = Button(root,text="Amount",command=child2_obj.getFinalAmount)
btn_amount.place(relx=0.04,rely=0.6,anchor=CENTER)

btn_addons = Button(root,text="Addons",command=child1_obj.getMenu)
btn_addons.place(relx=0.06,rely=0.3,anchor=CENTER)

root.mainloop()
