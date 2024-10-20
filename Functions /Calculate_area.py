def calculateArea(base,height):
    return float(0.5 *base*height)
#base=int(input("enter base : "))


#height=int(input("enter height: "))
#print(f"the Area of triangle is : {calculateArea(base,height)}")

#function will take now the shape type as parameter 
def Calculate_area_shape(a,b,shape):
    if shape.lower()=="rectangle":
        print(shape)
        return float(a*b)
    else:
          return float(0.5 *a*b)

#b=int(input("enter base : "))
#shape=input("enter the shape : ")
#h=int(input("enter height: "))
#print(f"the Area of triangle is : {Calculate_area_shape(b,h,shape)}")


def print_pattern(N):
     for i in range(N):
          for j in range(i+1):
               print("*", end="")
          

print_pattern(5)
print()