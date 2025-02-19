cp= int(input("Please enter your cost price:"))
sp= int(input("Please enter your selling price:"))
if sp>cp:
    print("Hey,you got a profit of", sp-cp)
else :
    print("Sorry, you faced a loss of", cp-sp)
