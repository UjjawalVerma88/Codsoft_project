from tkinter import *
# from tkinter import font


window = Tk()
window.geometry('280x428')
window.title("Calculator")
window.resizable(0,0)
window.configure(bg = "black")

equation = ""

def show(value):
    global equation
    equation += value
    label1.config(text = equation)




def clear():
    label1.config(text='')


def calculate():
    global equation
    result = "" 
    if equation !="":
        try:
            result = eval(equation)      # eval() is a built-in Python function that takes a string as input and evaluates it as a Python expression

        except:
            result = "error"
            equation = ""
    label1.config(text = result)

for i in range(4):
    window.columnconfigure(i, weight=1)




label1 = Label(window ,text = '',  bg = "black", fg = "white" ) 
label1.grid(row = 0 , column = 0 ,columnspan= 5, pady = (50,25),sticky = 'w')
label1.config(font =('verdana',20,"bold") )





btn_C = Button(window , text = 'C', bg = "#CD6565" , fg = 'white' ,width = 5, height =2 , command= lambda :clear())
btn_C.grid(row = 1, column = 0 )
btn_C.config(font =('verdana',14))

# btn_brac = Button(window , text = '()', bg = '#00a65a' , fg = 'white', width = 5 , height =2)
# btn_brac.grid(row = 1, column = 1)
# btn_brac.config(font =('verdana',14))

btn_mod = Button(window , text = '%', bg = '#8707E9' , fg = 'white', width = 5 , height =2 , command=lambda : show('%'))
btn_mod.grid(row = 1, column = 2)
btn_mod.config(font =('verdana',14))

btn_devide = Button(window , text = '/', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('/'))
btn_devide.grid(row = 1, column = 3)
btn_devide.config(font =('verdana',14))





btn7 = Button(window , text = '7', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('7'))
btn7.grid(row = 2, column = 0)
btn7.config(font =('verdana',14))

btn8 = Button(window , text = '8', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('8'))
btn8.grid(row = 2, column = 1)
btn8.config(font =('verdana',14))

btn9 = Button(window , text = '9', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('9'))
btn9.grid(row = 2, column = 2)
btn9.config(font =('verdana',14))

btn4 = Button(window , text = '4', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('4'))
btn4.grid(row = 3, column = 0)
btn4.config(font =('verdana',14))

btn5 = Button(window , text = '5', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('5'))
btn5.grid(row = 3, column = 1)
btn5.config(font =('verdana',14))

btn6 = Button(window , text = '6', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('6'))
btn6.grid(row = 3, column = 2)
btn6.config(font =('verdana',14))

btn1 = Button(window , text = '1', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('1'))
btn1.grid(row = 4, column = 0)
btn1.config(font =('verdana',14))

btn2 = Button(window , text = '2', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('2'))
btn2.grid(row = 4, column = 1)
btn2.config(font =('verdana',14))

btn3 = Button(window , text = '3', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('3'))
btn3.grid(row = 4, column = 2)
btn3.config(font =('verdana',14))


btn_mul = Button(window , text = '*', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('*'))
btn_mul.grid(row = 2, column = 3)
btn_mul.config(font =('verdana',14))

btn_sub = Button(window , text = '-', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('-'))
btn_sub.grid(row = 3, column = 3)
btn_sub.config(font =('verdana',14))

btn_add = Button(window , text = '+', bg = '#8707E9' , fg = 'white', width = 5 , height =2, command=lambda : show('+') )
btn_add.grid(row = 4, column = 3)
btn_add.config(font =('verdana',14))

btn_equal = Button(window , text = '=', bg = "#C3AED9" , fg = 'black', width = 5 , height =2, command=lambda : calculate())
btn_equal.grid(row = 5, column = 3)
btn_equal.config(font =('verdana',14))



btn_dot = Button(window , text = '.', bg = "#8707E9" , fg = 'white', width = 5 , height =2, command=lambda : show('.'))
btn_dot.grid(row = 1, column = 1)
btn_dot.config(font =('verdana',14))

btn_zero = Button(window , text = '0', bg = "#8707E9" , fg = 'white', width = 5 , height =2, command=lambda : show('0'))
btn_zero.grid(row = 5, column = 0,)
btn_zero.config(font =('verdana' ,14))

btn_bar = Button(window , text = '(', bg = "#B2C12B" , fg = 'black', width = 5 , height =2, command=lambda : show('('))
btn_bar.grid(row = 5, column = 1)
btn_bar.config(font =('verdana',14))

btn_bar1 = Button(window , text = ')', bg = "#B2C12B" , fg = 'black', width = 5 , height =2, command=lambda : show(')'))
btn_bar1.grid(row = 5, column = 2,)
btn_bar1.config(font =('verdana' ,14))







window.mainloop()