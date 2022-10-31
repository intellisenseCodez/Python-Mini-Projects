
class Grade_book:

    grade = ""
    
    def __init__(self, teacher, subject):
        self.teacher = teacher
        self.subject = subject

    
    def score_grade(self,score):
        if (score >= 70) and (score <= 100):
            self.grade = "A"
        elif (score >= 60) and (score <=69):
            self.grade = "B"
        elif (score >= 50) and (score <=59):
            self.grade = "C"
        elif (score >= 45) and (score <=49):
            self.grade = "D"
        elif (score >= 40) and (score <=44):
            self.grade = "E"
        elif (score >= 0) and (score <=39):
            self.grade = "F"
        else:
            print("INVALID SCORE!")
        return self.grade

    def results(self,data):
        #all students
        for stud in data:
            stud_name = stud["name"]
            stud_score = stud["score"]
            stud_grade = self.score_grade(stud_score)
            print(f"{stud_name} scored {stud_score} in {self.subject} with a grade of {stud_grade}")






