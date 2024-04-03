name = input("which shape do you want to calculate to calculate?")
while name!=



  if name:
        length = float(input(f"enter the lenghth? (in cm) "))
        width = float(input(f"enter the width? (in cm) "))
        length = (length) / 100
        width = (width) / 100
        area = length * width
        print("the area of this rectangle is", area)
  elif name== "t" or name == "T" or name=="triangle":
        base = float(input("enter the base of the triangle? (in cm) "))
        height = float(input("enter the height of the triangle? (in cm) "))
        base = (base) / 100
        height = (height) / 100
        area = base * height / 2
        print("the area of this triangle is", area)
 else name== "c","C","circle"
        radius = float(input("enter the radius of the circle? "))
        π = 3.14
        radius1 = pow(radius, 2)
        area = π * radius1
        print("the area of this circle is", area)

