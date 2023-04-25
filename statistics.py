#statistics
from tkinter import *
#from tkinter import ttk
import math
nums = input("Please enter a series of numbers").split(" ")
print(nums)
    
def std_dev(nums):
    global entry1
    sum = 0

    for x in nums:
     x = int(x)
     sum+=x

    mean = sum/len(nums)
    sig = 0

    for x in nums:
        x= int(x)
        sig+=(x-mean)**2
        print(x, sig)

    std= pow((sig/(len(nums)-1)),1/2)
    print(sig/(len(nums)-1))
    print("Standard Deviation = ",std)
    print("Variance = ", pow(std,2))
    return std
    


def correlation(list): 
    xs = []
    ys= []
    xsum = 0.0
    ysum = 0.0
    xmean = 0.0
    ymean=0.0
    tsum = 0.0
    
    for (x,y) in list:
        xs.append(x)
        ys.append(y)
    for x in xs:
        xsum+=float(x)
    xmean=xsum/len(xs)
    for y in ys:
        ysum+=float(y)
    ymean = ysum/len(ys)
    
    for i in range(0,len(xs)):
        tsum+=((float(xs[i])-xmean)*(float(ys[i])-ymean))
    corr = tsum/(std_dev(xs)*(std_dev(ys)))
    corr = corr*(1/(len(xs)-1))
    
    x2_sum = 0
    for i in range(0,len(xs)):
        x2_sum+=((float(xs[i])-xmean)**2)
    print(x2_sum)
    b1 = tsum/x2_sum
    print(b1)
    b0 = ymean - (b1*xmean)
    equation = f"y = {b0} + ({b1}x)"
    return [corr,equation]
    
        

std_dev(nums)
nums =(input("Please enter a series of coordinates:").split(" "))
nums_formatted = []
for num in nums:
    num = tuple(num.split(","))
    nums_formatted.append(num)

result = correlation(nums_formatted)

print("Correlation = "+str(result[0]))
print("Equation: " + result[1])
# root = Tk()
# frm = Frame(root, padx=150,pady=150)
# frm.grid()
# stringexample = ""
# entry1 = Entry(root,textvariable=stringexample).grid(column=0,row=0)
# b = Button(root, text="Calculate StdDev", command=std_dev).grid(column=1,row=0)


# mainloop()