
age = int(input("Enter your age: "))

if age < 5:
    print("Too young for school.")

elif age == 5:
    print("Go to kindergarten!")

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}!".format(grade))

else:
    print ("Go to college!")
