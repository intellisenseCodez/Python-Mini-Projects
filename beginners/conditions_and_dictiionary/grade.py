
# gradebook
student_data = [
    {"id": 1, "name": "John Holt", "score": 45, "subject": "Data Science"},
    {"id": 2, "name": "Shina Ranbow", "score": 50, "subject": "Data Science"},
    {"id": 3, "name": "Kiss Daniel", "score": 38, "subject": "Data Science"},
    {"id": 4, "name": "Wole Soyinka", "score": 83, "subject": "Data Science"},
    {"id": 5, "name": "Naira Marley", "score": 12, "subject": "Data Science"},
]

#Given the student data in a python dictionary. find
# the grade of the student

# return John Holt scored 67 in Data Science with a Grade of B

if (student_data["score"] >= 70) and (student_data["score"] <= 100):
    grade = "A"
elif (student_data["score"] >= 60) and (student_data["score"] <=69):
    grade = "B"
elif (student_data["score"] >= 50) and (student_data["score"] <=59):
    grade = "C"
elif (student_data["score"] >= 45) and (student_data["score"] <=49):
    grade = "D"
elif (student_data["score"] >= 40) and (student_data["score"] <=44):
    grade = "E"
elif (student_data["score"] >= 0) and (student_data["score"] <=39):
    grade = "F"
else:
    print("INVALID SCORE!")

# message = name + " scored " + str(score) + " in " + subject + " with a Grade of B"

message1 = "{} scored {} in {} with a Grade of {}".format(student_data["name"],student_data["score"],student_data["subject"],grade)
print(message1)