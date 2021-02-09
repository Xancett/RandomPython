

def GrossPay(hours_worked, wage_paid):
    if (hours_worked > 40):
        print("$", (wage_paid * 40) + (wage_paid * 1.5 * (hours_worked - 40)))
    else:
        print("$", hours_worked * wage_paid)

hours = 20
wage = 15
GrossPay(hours, wage)
GrossPay(45, 15)