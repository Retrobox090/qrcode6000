import tkinter as tf
import qrcode as qr
from tkinter import ttk
import sv_ttk
import darkdetect
i=1
fra="#1c1c1c"
theme=darkdetect.theme()
print(theme)
if theme=="Dark":
    fra="#1c1c1c"
elif theme=="Light":
    fra="#fafafa"
bor=1
ver=1
fi="blue"
ba="blue"

root=tf.Tk()
root.title("Qr code creator")
sv_ttk.set_theme(darkdetect.theme())
root.resizable(width=False,height=False)
root.geometry("800x600"),root.config(bg=fra)        #root settings


box=ttk.Frame(border=10)       #box frame
box.pack(),box.place(x=0,y=200)


input=tf.Text(master=box,name="determination",width=40,height=10,font="arial")    #text box
label=ttk.Label(text="Input your text here:")       #label
label.pack(),label.place(x=5,y=180)
input.pack()

fram3=ttk.Frame(width=300,height=300,border=6)
fram3.pack(),fram3.place(x=480,y=200)
fram3.pack_propagate(0)




frame2=ttk.Frame(width=550,height=130,)
frame2.pack(fill="both",expand=False),frame2.place(x=0,y=30)

strv=tf.StringVar(root)#option1 stuff




option2=["1","2","3","4"]#option1 list 
option3=["fight","act","save","items","mercy"]
option6=["blue","green","white","yellow"]
optio=["1","2","3","4","5","6","7","8"]
option8=option6.copy()

strv.set("size")#option1 stuff
strv2=tf.StringVar(root)
strv2.set("qr version")
strv3=tf.StringVar(root)
strv3.set("Fill colour")
strv4=tf.StringVar(root)
strv4.set("Back colour")
strv5=tf.StringVar(root)
strv5.set("idk")

frame2.pack_propagate(0)


def create():
    ans=input.get("1.0","end-1c")
    border=strv.get()
    Fill=strv3.get()
    Back=strv4.get()
    size=strv5.get()
    bor=str(border)
    fi=str(Fill)
    ba=str(Back)
    ver=str(size)
    ss=qr.QRCode(version=ver,border=bor,box_size=3)
    ss.add_data(ans)
    ss.make(fit=True)
    ss2=ss.make_image(fill_color = fi,back_color = ba)
    ss2.save("ans.jpg")
    img=tf.PhotoImage(file="ans.jpg")              #image widget
    img2=ttk.Label(master=fram3,image=img)
    img2.image_names=img
    img2.pack()

convert=ttk.Button(text="Convert",width=20,command=create)
convert.pack(),convert.place(x=5,y=500)       #convert button




option=ttk.OptionMenu(frame2,strv,*option2)   #option button 1
option4=ttk.OptionMenu(frame2,strv2,*option3) #option button 2
option5=ttk.OptionMenu(frame2,strv3,*option6)
option7=ttk.OptionMenu(frame2,strv4,*option8)
opy=ttk.OptionMenu(frame2,strv5,*optio)
opy.pack(expand=False),opy.place(x=220)
option7.pack(expand=False),option7.place(x=300,y=50)
option5.pack(expand=False),option5.place(x=100,y=50)
option4.pack(expand=False),option4.place(x=20)
option.pack(expand=False),option.place(x=80)

option4.destroy()




label1=ttk.Label(master=frame2,text="Border:")
label1.pack(),label1.place(x=20,y=5)
label2=ttk.Label(master=frame2,text="Fill colour:")           #all the labels for size 
label2.pack(),label2.place(x=20,y=55)
label3=ttk.Label(text="Back colour:")
label3.pack(),label3.place(x=200,y=85)
la=ttk.Label(master=frame2,text="Size:")
la.pack(),la.place(x=180,y=7)



def des():
    for test in fram3.winfo_children():
        test.destroy()



button2=ttk.Button(text="Img clear",command=des)

button2.pack(),button2.place(x=300,y=30)
label4=ttk.Label(text=" Warning:converting automatically saves the qrcode",font=3)
label4.pack(),label4.place(x=300,y=500)




root.mainloop()