'''
TPRG 2131 Fall 2023 Assignment 1
Sept, 2023
Nelson Hukclebridge

******

This program is made to calculate various shape areas and volumes

******

'''
#Introduction for the user

print("welcome too Nelsons A_V calculator")


def square_area(x,y):
    """Area Calculation for a Square"""
    return x * y

def cyl_vol(x, y):#
    """Volume Calculation for a Cylinder"""
    return x * y

def triangle_area(x, y):
    """Area Calculation for a Triangle"""
    return round((x*y)/2, 2)

def pyramid_volume(x, y):
    """Volume Calculation for a Pyramid"""
    return round((x*y)/3, 2)

def rectangle_tank_volume(x, y):
    """Volume Calculation for a Rectangulare Tank"""
    return x * y

def gone(q):
    """Q for quiting the program or option too continue the program"""
    if q in ("Q", "q"):#Q or q
        return False
    return True

while True:
    #user choice for different views of the calculation
    CHOICE = input("hit V/v for calculated view or D/d for default view:")

    if CHOICE in ("V", "v"):# if statement for V
        #different operations for the user
        print("Select operation.")
        print("1.SQUARE AREA")
        print("2.CYLINDER VOLUME")
        print("3.TRIANGLE AREA")
        print("4.PYRAMID VALUME")
        print("5.RECTANGLE TANK VOLUME")


        choice = input("Enter choice(1/2/3/4): ")#for user input


        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number in cm, if options 2, 4 or 5 were chosen in cm^2: "))
            num2 = float(input("Enter second number in cm: "))
            #each option corresponding too each calculation
            if choice == '1':
                print(num1, "cm", "*", num2, "cm", "=", square_area(num1, num2), "cm^2", "(Width x Length = Area)")

            elif choice == '2':
                print(num1, "cm^2", "*", num2, "cm", "=", cyl_vol(num1, num2), "cm^3", "(Area x Height = Volume)")

            elif choice == '3':
                print(num1, "cm", "*", num2, "cm", "/2", "=", triangle_area(num1, num2), "cm^2", "((Width x Length)/2 = Area)")

            elif choice == '4':
                print(num1, "cm^2", "*", num2, "cm", "/3", "=", pyramid_volume(num1, num2), "cm^3", "((Width x 2 x Height)/3 = Volume)")

            elif choice == '5':
                print(num1, "cm^2", "*", num2, "cm", "=", rectangle_tank_volume(num1, num2), "cm^3","(Area x Height = Volume)")
                #input for user option too continue program or quit with q
            next_calculation = input("Hit Q or q too quit if not hit any other key for another calculation:")
            if not gone(next_calculation):
                break

    elif CHOICE in ("D", "d"):# if statement for D
        print("Select operation.")
        print("1.SQUARE AREA")
        print("2.CYLINDER VOLUME")
        print("3.TRIANGLE AREA")
        print("4.PYRAMID VALUME")
        print("5.RECTANGLE TANK VOLUME")

        choice = input("Enter choice(1/2/3/4): ")#for user input


        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number in cm, if options 2, 4 or 5 were chosen in cm^2: "))
            num2 = float(input("Enter second number: "))
            #each option corresponding too each calculation
            if choice == '1':
                print(num1, "cm", "*", num2, "cm", "=", square_area(num1, num2), "cm^2")

            elif choice == '2':
                print(num1, "cm^2", "*", num2, "cm", "=", cyl_vol(num1, num2), "cm^3")

            elif choice == '3':
                print(num1, "cm", "*", num2, "cm", "/2", "=", triangle_area(num1, num2), "cm^2")

            elif choice == '4':
                print(num1, "^2", "cm", "*", num2, "cm", "/3", "=", pyramid_volume(num1, num2), "cm^3")

            elif choice == '5':
                print(num1, "cm^2", "*", num2, "cm", "=", rectangle_tank_volume(num1, num2), "cm^3")
            #input for user option too continue program or quit with q
            next_calculation = input("Hit Q or q too quit if not hit any other key for another calculation:")
            if not gone(next_calculation):
                break

if __name__ == "__main__": # this is for pytest
    #fixed numbers to replace x and y
    square_area(2, 2)
    cyl_vol(2, 2)
    triangle_area(2, 2)
    pyramid_volume(2, 4)
    rectangle_tank_volume(2, 2)
    #if runs correctly no Assertion error will appear
    if square_area(2, 2) != 4:
        raise AssertionError
    if cyl_vol(2, 2) != 4:
        raise AssertionError
    if triangle_area(2, 2) != 2:
        raise AssertionError
    if pyramid_volume(2, 3) != 2:
        raise AssertionError
    if rectangle_tank_volume(2, 2) != 4:
        raise AssertionError
    print("\nDone")
