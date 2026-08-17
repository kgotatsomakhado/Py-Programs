print("*******************************************************")
print("         Welcome To The Area program")
print("")
print("*******************************************************")
print("")
print("Choose your favoured program:")
print("")
print("1. Area of a square")
print("2. Area of a triangle")
print("3. Area of a rectangle")
print("4. Area of a circle")
print("")
programs=int(input("Select your program: "))
print("")
print("*******************************************************")



def switches(programs):
    match programs:
        case 1:
            print("*******************************************************")
            print("")
            print("     We are finding the Area of a square right now")
            print("")
            print("*******************************************************")
            print("")
            side= input("Please enter the length of one side so that we can calculate the area: ")
            side=int(side)
            square_area = side*side
            print("")
            print(f"The area of your square is {square_area}")
            print("")
            print("*******************************************************")
            return
        case 2:
            print("*******************************************************")
            print("")
            print("We are finding the Area of a triangle right now")
            print("")
            print("*******************************************************")
            print("")
            base= input("Please enter the base of the triangle: ")
            height= input("Please enter the height of the triangle: ")
            base=int(base)
            height=int(height)
            triangle_area = 0.5 * base * height
            print("")
            print(f"The area of your triangle is {triangle_area}")
            print("")
            print("*******************************************************")
            return 
        case 3:
            print("*******************************************************")
            print("")
            print("We are finding the Area of a rectangle right now")
            print("")
            print("*******************************************************")
            print("")
            width= input("Enter the width of the rectangle: ")
            height= input("Enter the height of the rectangle: ")
            width= int(width)
            height= int(height)
            rectangle_area = width * height
            print("")
            print(f"The area of your rectangle is {rectangle_area}")
            print("")
            print("*******************************************************")
            return
        case 4:
            print("*******************************************************")
            print("")
            print("We are finding the Area of a circle right now")
            print("")
            print("*******************************************************")
            print("")
            radius= input("Enter the radius of the circle: ")
            radius=int(radius)
            circle_area = 3.14 * (radius**2)
            print("")
            print(f"The area of your circle is {circle_area}")
            print("")
            print("*******************************************************")
            return
        case _:
            print("Invalid program selected.")

switches(programs)            