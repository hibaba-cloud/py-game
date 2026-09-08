print("this is my first vs code scentece")
#variable is a container that stores value
name="hiba"
print(name)
#Lists are used to store multiple values together
names=["hiba","muhammad hussain","hassan","tanshi","andrea"]
print(names)
#Dictionaries are used to store multiple values in pairs(key-value pair)
nameDict={
    "hiba":"white",
    "muhammad hussain":"green",
    "hassan":"blue",
    "tanshi":"lavender",
    "andrea":"black",
}
print(nameDict)
#only print names from dictionary
print(nameDict.keys())
#only print colors from dictionary
print(nameDict.values())
#only print hiba and her value
print("hiba",nameDict["hiba"])
while True:
    name2=input("Enter your name\exit: ").lower()
    if name2 =="exit":
        print("Bye")
        break
    color1=input("Enter ur fav color\exit: ").lower()
    if  color1=="exit":
        print("Bye")
        break
    nameDict[name2]=color1
    print(nameDict)



    
    
