mydict = {}
loop = True
while loop:
    print("What would you like to do [A]dd items [C]hange Items [R]emove [D]isplay [S]earch")
    choice = input()

    match choice:
        case "A":
            print("Enter Item Name: ")
            item = input()
            key = len(mydict) + 1
            if key > 3:
                print("Maximum of 3 items only")
            else:
                mydict[key] = item
        case "C":
            print("Enter key to search: ")
            change = int(input())
            if change in mydict:
                print(f"Found: {mydict.get(change)}")
                print("Enter Value: ")
                value = input()
                mydict[change] = value
            else:
                print("Not Found")
        case "R":
            print("Enter key to remove: ")
            remove = int(input())
            if remove in mydict:
                mydict.pop(remove)
            else:
                print("Key Not Found")
        case "S":
            print("Enter Item to Search: ")
            search = int(input())
            if search in mydict:
                print(f"found {mydict.get(search)} item")
            else:
                print("Im sorry, not in the cart")
        case "D":
            print("Key","   Value")
            for x,y in mydict.items():
                print("",x, "    ",y)
        case "*":
            print("Bye")
            break
    
                
            

