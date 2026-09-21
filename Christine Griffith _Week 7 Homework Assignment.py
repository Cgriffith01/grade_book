#
#Christine Griffith
#Week 7 Homework Assignment 
#
quiz_scores = []

class Gradebook:
    """Keeps track of quiz scores and average scores for student 1 and 2"""
    count = 0
    
    
    def __init__(self,name):
        self.name = name
        self.grades = []
        Gradebook.count += 1
        return
    
    def quizScore(self,score):
       self.grades.append(q_score_1)
       self.grades.append(q_score_2)
        
    def full_student_1(self, name, grades):
        self.name1 = {student_1}
        self.grades = {Gradebook.s1_score}
        
    def full_student_2(self, name,grades):
        self.name = {student_1}
        self.grades = {Gradebook.s1_score}
        
    def currentAverage(self):
         
        print(f"{student_1} average: ")
    
student_1 = input("Please enter the name for Student 1: ")
Gradebook(student_1)
print(f"There are {Gradebook.count} students in the GradeBook.\n")

student_2 = input("Please enter the name for Student 2: ")
Gradebook(student_2)
print(f"There are {Gradebook.count} students in the GradeBook.\n")

prompt = "\nGrade Book\n\n0: Exit\n1: Enter quiz grade for Student 1\n2: Enter quiz grade for Student 2\n3: Display current grades for all students\n "
prompt += "\nPlease enter a choice: "

active = True
while active:
    selection = input(prompt)
    
    if selection == '0':
        active = False
        exit
        
    elif selection == '1':
        q_score_1 = input(f"Please enter the quiz score for {student_1}: ")
        q_score_1 = int(q_score_1)
        
      
        Gradebook.quizScore
        
    elif selection == '2':
        q_score_2 = input(f"Please enter the quiz score for {student_2}: ")
        q_score_2 = int(q_score_2)

        Gradebook.quizScore
        
    elif selection == '3':
        print("Displaying current grades for all students.\n")
        print(student_1)
        print(q_score_1)
        print("---------------------------")
        print(student_2)
        print(q_score_2)
        
    else:
        print("Please select 0,1,2 or 3 only.")

       

