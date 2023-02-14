#program which accepts the radius of a circle from the user and computes area.

Radius=int(input("Enter the radius of the Circle: "))
Area = 3.14*Radius*Radius
print("Area of the circle is",Area )

#program to accept a filename from the user and print the extension of that.

File_Name= input("Enter File Name: ")
myDict={File_Name : "Python"}
print(myDict)

#Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64
List = [12, -7, 5, 64, -14]
for i in List:
  if i <0:
    List.remove(i)
    print(List)

#Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]
    
NewList = [12, 14, -95, 3]
for i in NewList:
  if i <0:
    NewList.remove(i)
    print(NewList)

#Input : Please enter a string Mississippi; Output : i = 04 s = 04 p =02 m =01

i = ("Mississippi")
print(i.count(input("Enter a character in Mississippi: ")))

