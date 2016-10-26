import os
import sys
import json
file_name='data.json'
with open(file_name) as f:
    data=json.load(f)

        
def main():
    choice=showMenu()
    while choice!=4:
        if choice==1:
            createUser()
        elif choice==2:
            editUser()
        elif choice==3:
            printDataFile()
        else:
            print("Invalid option\n")
        choice=showMenu()
            
def showMenu():
    print("Menu :")
    print("1) Create User")
    print("2) Edit User")
    print("3) Show Leaderboard")
    print("4) Exit")
    print("Enter Your Choice (1-4) :")
    choice=int(input())
    return choice


def editUser():
    print "Username"
    k=raw_input()
    global data
    flag=None
    for i in range(len(data)):
        if(k==str(data.values()[i]['name'])):
            flag=i
    if(flag!=None):
        print "Password"
        passs=raw_input()
        if(passs==str(data.values()[flag]['password'])):
            print "Authentication Successful"
            AuthS(flag)
        else:
            print "Incorrect Password"
            return
    else:
        print "Invalid username"
        return

def AuthS(n):
    global data
    print "Change age?(y/n)"
    x=raw_input()
    if(x=='y'):
        print "Enter new age:"
        agen=input()
        data.values()[n]['age']=agen
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
    print "Change score?(y/n)"
    y=raw_input()
    if(y=='y'):
        print "Enter new score:"
        scoren=input()
        data.values()[n]['score']=scoren
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
    
def createUser():
    global data
    print "Enter Username:"
    uname=raw_input()
    for i in range(len(data)):
        if(uname==str(data.values()[i]['name'])):
            print "This username already exists"
            return
    print "Enter Password:"
    upass=raw_input()
    print "Enter Age:"
    uage=input()
    print "Enter Score:"
    uscore=input()
    newuser=str(len(data)+1)
    newdic={
        newuser:{
            "score":uscore,
            "age":uage,
            "password":upass,
            "name":uname
            }
        }
    data.update(newdic)
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    
    
    
def printDataFile():
    global data
    d=(json.dumps(data, indent=2, sort_keys=False))
    k=[]
    for i in range(len(data)):
        k.append(data.values()[i]['score'])
    k=list(set(k))
    k.sort()
    k.reverse()
    
    for m in range(len(k)):
        temp=k[m]
        for i in range(len(data)):
            if(data.values()[i]['score']==temp):
                print str(data.values()[i]['name']) + ' - ' + str(data.values()[i]['score'])+' points (age:'+str(data.values()[i]['age'])+')' 

main()
