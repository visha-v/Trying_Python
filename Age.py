age = int(input("Enter your age: "))

if age < 5:
    print("Too young for school.")

elif age == 5:
    print("Go to kindergarten!")

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}!".format(grade))

elsif age < 21:
    print ("Go to college!")
else:
    print("GO TO WORK")
