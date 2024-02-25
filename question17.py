import pandas as ps

while True:
    a=int(input("Enter your number 1 : "))
    b=int(input("Enter your number 2 : "))
    c=int(input("Enter your number 3 : "))
    print()

    df=ps.DataFrame({"Numbers":["Number 1","Number 2","Number 3"],
                     "Values":[a,b,c]},index=["I","II","III"])
    print(df)
    
    if(a>b and a>c):
        print("\n",a,"Number 1 is greatest.\n")
        print(df[df["Numbers"]=="Number 1"])
    elif(b>a and b>c):
        print("\n",b,"Number 2 is greatest.")
        print(df[df["Numbers"]=="Number 2"])
    elif(c>a and c>b):
        print("\n",c,"Number 3 is greatest.")
        print(df[df["Numbers"]=="Number 3"])
    else:
        print("Invalid Input.....")

    choice=input("\nDo you want to continue or not [y/n] : ")
    if(choice=='n'):
        break
    elif(choice=='y'):
        continue
    else:
        print("Invalid Input...")
        break