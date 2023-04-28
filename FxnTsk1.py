# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.

def area_of_tri(k,b,h):
    b =float(input("Enter the base: ") )
    h = float(input("Enter the height: "))
    k=0.5
    area=float(k*b*h)   
    return area
          
area_of_triangle =area_of_tri('k','b','h')
print("The triangle area is: ", area_of_triangle)

