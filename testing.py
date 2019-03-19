#Ask user how many courses they offer
user_input = int(input("how many courses did you offer? "))
total_course_unit_of_course = int(input("what is the total course unit: "))
#create an empty list
total_course_unit = []

#Create a for loop to ask user for input
for i in range(user_input):
    user_grade = input(f"What is your grade in course {i+1}? ")
    user_unit = int(input("what is the course unit? "))
    user_grade = user_grade.upper()
    print("")
    #create a conditional statement that compares Values
    if user_grade == "A":
        grade_point = user_unit * 5

        #Append each value to the list
        total_course_unit.append(grade_point)
    elif user_grade == "B":
        grade_point = user_unit * 4

        #Append each value to the list
        total_course_unit.append(grade_point)
    elif user_grade == "C":
        grade_point = user_unit * 3

        #Append each value to the list
        total_course_unit.append(grade_point)
    elif user_grade == "D":
        grade_point = user_unit * 2

        #Append each value to the list
        total_course_unit.append(grade_point)
    elif user_grade == "E":
        grade_point = user_unit * 1

        #Append each value to the list
        total_course_unit.append(grade_point)
    elif user_grade == "F":
        grade_point = user_unit * 0

        #Append each value to the list
        total_course_unit.append(grade_point)

print(sum(total_course_unit) / int(total_course_unit_of_course))
print(total_course_unit_of_course)
        #Sum the values in the list
#Dvide the total Value by the entire course Unit


