def area_of_rectangle (length, width):
    return length * width

length = float(input("enter the length of the rectangle: "))
width = float(input("enter the width of the rectangle: "))

area = area_of_rectangle(length, width)
print("The are of the rectangle is: ",area)