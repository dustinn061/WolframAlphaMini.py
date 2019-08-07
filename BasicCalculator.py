from tkinter import *
root = Tk() # blank window

var1 = IntVar()
c1 = Checkbutton(root, text='Mean', variable=var1)
c1.grid(row=0)

var2 = IntVar()
c2 = Checkbutton(root, text='Median', variable=var2)
c2.grid(row=1)

var3 = IntVar()
c3 = Checkbutton(root, text='RMS', variable=var3)
c3.grid(row=2)

var4 = IntVar()
c4 = Checkbutton(root, text='Middle Average', variable=var4)
c4.grid(row=3)

result1 = Label(root,text='')
result1.grid(row=0,column=1)

result2 = Label(root,text='')
result2.grid(row=1,column=1)

result3 = Label(root,text='')
result3.grid(row=2,column=1)

result4 = Label(root,text='')
result4.grid(row=3,column=1)

entry1 = Entry(root)
entry1.grid(row=4,column=0)

def mean(theList):
    count = 0
    total = 0
    for thing in theList:
        count = count + 1
        total = total + int(thing)
    return total / count

def median(theList):
    theList.sort()
    if len(theList) % 2 == 0:
        return (int(theList[len(theList) // 2]) + int(theList[len(theList) // 2 - 1])) / 2
    else:
        return int(theList[len(theList) // 2])

def rms (theList):
    index = 0
    for each in theList:
        theList[index] = int(theList[index])**2
        index = index + 1
    return mean(theList) ** (1/2)

def middle_average(theList):
    newList = [0,0,0]
    newList[0] = mean(theList)
    newList[1] = median(theList)
    newList[2] = rms(theList)
    print(newList)
    return median(newList)


def doStuff(event):

    myList = entry1.get().strip().split()

    if var1.get() == 1:
        result1.config(text=mean(myList))

    if var2.get() == 1:
        result2.config(text=median(myList))

    if var3.get() == 1:
        result3.config(text=rms(myList))

    if var4.get() == 1:
        result4.config(text=middle_average(myList))


button1 = Button(root, text = 'Calculate')
button1.bind("<Button-1>", doStuff)
button1.grid(row=4,column=1)


root.title('Basic Calculator')
root.mainloop()












Ctemp = input('What is the temperature in Celsius? ')
Ctemp = float(Ctemp)

Ftemp = (Ctemp * 1.8 + 32)
Ftemp = float(Ftemp)
def c2f(Ctemp):
    return Ctemp * 1.8 + 32


def f2c(Ftemp):
    return ((Ftemp - 32) / 1.8)

print('It is', Ftemp, "degrees Fahrenheit.")



#take a expression from a string and calculate it
def binop(s):
    if s.find('*') != -1:           #sees which operator the string is using , sets the position of the operator
        operator_pos = s.find('*')
        int_one = int(s[:operator_pos])  # splits the string into its respective sides
        int_two = int(s[operator_pos + 1:])
        return int_one * int_two
    elif s.find('/') != -1:
        operator_pos = s.find('/')
        int_one = int(s[:operator_pos])  # splits the string into its respective sides
        int_two = int(s[operator_pos + 1:])
        return int_one / int_two
    elif s.find('+') != -1:
        operator_pos = s.find('+')
        int_one = int(s[:operator_pos])  # splits the string into its respective sides
        int_two = int(s[operator_pos + 1:])
        return int_one + int_two
    elif s.find('-') != -1:
        operator_pos = s.find('-')
        int_one = int(s[:operator_pos])   # splits the string into its respective sides
        int_two = int(s[operator_pos + 1:])
        return int_one - int_two

#def equation(s):
#    if s.find('*') == -1 and s.find('/') == -1 and s.find('+') == -1 and s.find('-') == -1:
#        return s
#   if s.find('*') != -1:


print(binop("3+7"))

