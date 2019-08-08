from tkinter import *
root = Tk() # blank window
'''-----------------buttons and labels-------------------------------------'''
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

result5 = Label(root,text='')
result5.grid(row=0,column=6)

result6 = Label(root,text='Temp: ')
result6.grid(row=3,column=4)

entry1 = Entry(root)
entry1.grid(row=4,column=0)

entry2 = Entry(root)
entry2.grid(row=0,column=4)

entry3 = Entry(root)
entry3.grid(row=2,column=5)

'''-----------------functions-------------------------------------'''
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
    newList = theList.copy()
    for each in theList:
        newList[index] = int(theList[index])**2
        index = index + 1
    return mean(newList) ** (1/2)

def equation(s):
    if s.find('*') == -1 and s.find('/') == -1 and s.find('+') == -1 and s.find('x') == -1:
        result5.config(text='Answer: ' + s)
        return s

    if s.find('*') != -1 or s.find('/') != -1:
        x1 = 999
        x2 = 999
        if s.find('*') != -1:
            x1 = s.find('*')
        if s.find('/') != -1:
            x2 = s.find('/')

        operator_pos = min(x1,x2)
        part1 = (s[:operator_pos])  # splits the string into its respective sides
        part2 = (s[operator_pos + 1:])

        index1 = max(part1.rfind('+'), part1.rfind('x'), part1.rfind('/'),part1.rfind('*') )
        num1 = part1[index1 + 1:]

        v1 = 999
        v2 = 999
        v3 = 999
        v4 = 999
        if part2.find('+') != -1:
            v1 = part2.find('+')
        if part2.find('x') != -1:
            v2 = part2.find('x')
        if part2.find('/') != -1:
            v3 = part2.find('/')
        if part2.find('*') != -1:
            v4 = part2.find('*')

        index2 = min(v1, v2, v3, v4)
        num2 = part2[:index2]
        if x1 < x2:
            ans = float(num1) * float(num2)

        else:
            ans = float(num1) / float(num2)

        newString = s[:index1 + 1] + str(ans) + s[operator_pos + len(num2) + 1:]
        return equation(newString)
    if s.find('+') != -1 or s.find('x') != -1:
        x1 = 999
        x2 = 999
        if s.find('+') != -1:
            x1 = s.find('+')
        if s.find('x') != -1:
            x2 = s.find('x')
        operator_pos = min(x1, x2)
        part1 = (s[:operator_pos])  # splits the string into its respective sides
        part2 = (s[operator_pos + 1:])

        index1 = max(part1.rfind('+'), part1.rfind('x'), part1.rfind('/'), part1.rfind('*'))
        num1 = part1[index1 + 1:]

        v1 = 999
        v2 = 999
        v3 = 999
        v4 = 999
        if part2.find('+') != -1:
            v1 = part2.find('+')
        if part2.find('x') != -1:
            v2 = part2.find('x')
        if part2.find('/') != -1:
            v3 = part2.find('/')
        if part2.find('*') != -1:
            v4 = part2.find('*')

        index2 = min(v1, v2, v3, v4)
        num2 = part2[:index2]
        if x1 < x2:
            ans = float(num1) + float(num2)
        else:
            ans = float(num1) - float(num2)

        newString = s[:index1 + 1] + str(ans) + s[operator_pos + len(num2) + 1:]
        return equation(newString)

def doStuff(event):
    myList = entry1.get().strip().split()
    if var1.get() == 1:
        result1.config(text=mean(myList))
    else:
        result1.config(text='')

    if var2.get() == 1:
        result2.config(text=median(myList))
    else:
        result2.config(text='')

    if var3.get() == 1:
        result3.config(text=rms(myList))
    else:
        result3.config(text='')

    if var4.get() == 1:
        middleList = [mean(myList),median(myList),rms(myList)]
        result4.config(text=median(middleList))
    else:
        result4.config(text='')

def doStuff2(event):
    equation(entry2.get().strip().replace('-','x'))

def c2f(self):
    result6.config(text = 'Temp ' + str((float(entry3.get())) * 1.8 + 32))

def f2c(self):
    result6.config(text = 'Temp ' + str(((float(entry3.get()) - 32) / 1.8)))

button1 = Button(root, text='Calculate')
button1.bind("<Button-1>", doStuff)
button1.grid(row=4, column=1)

button2 = Button(root, text='Equate')
button2.bind("<Button-1>", doStuff2)
button2.grid(row=0, column=5)

button3 = Button(root, text='FtoC')
button3.bind("<Button-1>", f2c)
button3.grid(row=3, column=5)

button4 = Button(root, text='CtoF')
button4.bind("<Button-1>", c2f)
button4.grid(row=4, column=5)

root.title('Basic Calculator')
root.mainloop()