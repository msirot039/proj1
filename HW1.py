print("Enter dollar ($) (* to exit):")
enter = input()
split = enter.split("@")

def conversion(tofloat):
    ruppe = tofloat * 88.05
    pound = tofloat * 0.73
    y = tofloat * 7.12
    return ruppe,pound,y

if enter == "*":
    print("Bye")
else:
    print(f"{"Dollar ($)":<10} {"Indian Rupee (R)":<15} {"British Pound (Pound)":<15} {"China (Y)":<15}")
    for x in split:
        tofloat = float(x)
        ruppe1, pound1, y1 = conversion(tofloat)
        print(f"{tofloat:<15}  {ruppe1:<15}  {pound1:<15}  {y1:<15}")
    print()


