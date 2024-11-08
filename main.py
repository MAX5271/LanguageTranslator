from tkinter import *
from tkinter import ttk
from googletrans import Translator
from googletrans import LANGUAGES


def change(text="Type",srl="English",tran="Hindi"):#defining the function to translate text and also assigining the default values to the parameters
    trans = Translator() #creating an object to use the functions of googletrans api
    translation = trans.translate(text,src=srl,dest=tran)# translating the text
    return translation.text

def data():
    #getting the data inputed by the user int the text fields
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0,END)
    #calling the function to translate the text inputed by the user to the selected language
    textGet = change(text=msg,srl=s,tran=d)
    #removing the result of the previous query
    Dest_txt.delete(1.0,END)
    #inserting the result of the current query
    Dest_txt.insert(END,textGet)

#creating an object to use the tkinter module    
root = Tk()
root.title("Translator")#setting the title of the app
root.geometry("800x820")#setting the resolution of the app
root.config(bg='Black')

#creating ans positioning the head line of the app
lab_txt=Label(root,text="Translator",font=("Cascadia Code",36,"bold"),bg="Black",foreground="White")
lab_txt.place(x=250,y=40,height=45,width=300)

frame = Frame(root).pack(side=BOTTOM)# adjusting the placements of the frame and assining the widget to the variable


#creating and placing the label and text field widgets
lab_Sor=Label(root,text="Enter Text",font=("Cascadia Code",32,"bold"),bg="Black",foreground="White")
lab_Sor.place(x=0,y=100,height=40,width=300)
Sor_txt = Text(frame,font=("Cascadia Code",28,"bold"),wrap=WORD,bg="Black",foreground="White")
Sor_txt.place(x=10,y=160,height=250,width=780)

#creating a list of all the available languages
list_text = list(LANGUAGES.values())

#creating a combobox to display the inputed language
comb_sor = ttk.Combobox(frame,values=list_text,font=("Cascadia Code",14),background="white",foreground="Black")
comb_sor.place(x=155,y=430,height=50,width=130)
comb_sor.set("English")

#creating a button that translates the inputed text to selected language
button_change= Button(text="Translate",font=("Cascadia Code",14),bg="Black",foreground="White",borderwidth=0,relief=RAISED,command=data)
button_change.place(x=335,y=430,height=50,width=130)

#creating a combobox to display the different languages to translate the inputed text to
comb_dest = ttk.Combobox(frame,values=list_text,font=("Cascadia Code",14),background="white",foreground="Black")
comb_dest.place(x=515,y=430,height=50,width=130)
comb_dest.set("English")

#creating and placing the label and text field to display the output translated text    
lab_Sor=Label(root,text="Translation",font=("Cascadia Code",32,"bold"),bg="Black",foreground="White")
lab_Sor.place(x=0,y=500,height=40,width=300)
Dest_txt = Text(frame,font=("Cascadia Code",28,"bold"),wrap=WORD,bg="Black",foreground="White")
Dest_txt.place(x=10,y=560,height=250,width=780)

#updating and keeping up the program
root.mainloop()