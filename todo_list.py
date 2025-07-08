import tkinter

from tkinter import *



window = Tk()
window.geometry("400x700+400+100")
window.title("TO Do List")
# window.resizable(0,0)
window.configure(bg="#ecf3f9")  # Very dark slate blue
# window.configure(bg = "#AFF849")
# window.iconbitmap("flower.png")


# photo = PhotoImage(file = "flower.png")

# label = Label(image = photo)
# label.pack()

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+ "\n")

        
        listbox.delete(ANCHOR)

def openTaskFile():

    try: 

        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n': 
                task_list.append(task)
                listbox.insert(END ,task)
    except:
        file = open('tasklist.txt','w')
        file.close()

Image_icon = PhotoImage(file = "task.png")
window.iconphoto(False , Image_icon)



# noteImage = PhotoImage(file = "task.png")
# Label(window , image = noteImage , bg = "#eff0e9").place(x = 340 , y = 25)


heading = Label(window , text = "All Task", font =("arial",25, "bold") ,fg = "black" , bg = "white" )
heading.place(x =130 , y = 20)

frame = Frame(window, width = 420 , height =50 , bg = "white")
frame.place(x = 0 , y = 180)

task = StringVar()
task_entry = Entry(frame , width = 18 , font = ("arial", 20) , bd = 0 )
task_entry.place(x = 10 , y =7)
task_entry.focus()


button = Button(frame , text = "Add" ,font = ("arial", 20 ,"bold"), width = 6 , bg = "#5a95ff", fg = "#fff",bd = 0 , command= addTask)
button.place(x = 300 , y = 0)

frame1 = Frame(window , bd = 2 , width =700 , height=280 , bg ="#32405b" )
frame1.pack(pady = (230,0))

listbox = Listbox(frame1 , font =("Italic" , 12), width = 40 , height = 16 , bg = "#0d1118" ,fg = "white" , cursor = "hand2",selectbackground= "#a6bde9")
listbox.pack(side = LEFT , fill = BOTH ,padx = 2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = BOTH)


listbox.config(yscrollcommand = Scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

delete_icon = PhotoImage(file= "trash_4.png" )
Button(window ,image = delete_icon,bd = 0, command=deleteTask).pack(side = BOTTOM , pady=13 )



listbox.config()



window.mainloop()