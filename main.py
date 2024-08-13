print("*AREA CALCULATOR*")
print("""Press 1 to find the area of square
      Press 2 to find the area of rectangle
      Press 3 to find the area of circle
      Press 4 to find the area of triangle""")

choice = int(input("Enter the number between 1-4: "))

if choice == 1:
    side = float(input("Enter the number of one side:"))
    area = side**2
    print("The area of square", area)
elif choice == 2:
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the breadth of rectangle: "))
    area = length*width
    print("The area of rectangle", area)
elif choice == 3:
    radius = float(input("Enter the radius of circle: "))
    area = 2*3.14*radius
    print("Area of circle",area)
elif choice == 4:
    base =  float(input("Enter the base of triangle: "))
    height = float(input("Enter the height of triangle: "))
    area = 0.5*base*height
    print("Area of the triangle", area)

else:
    print("Invalid input")
