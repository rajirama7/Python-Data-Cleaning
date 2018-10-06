x=eval(input("Enter a number:"))
y=str(x)
#i=" "
for i in range(0,x):
    print(y,end="")
    
    if i==(x-1):
      print(y*i,end="")  
    else:    
      print(y*i,end="+") 