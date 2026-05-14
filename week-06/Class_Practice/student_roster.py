# Student Roster Manager
# Exercise 6.2
# Marenza Santarin
# 5/14/2026

# Creating a class named Student
class Student:

    # Class attribute / shared by every student:
    school = "YearUp Academy"

    # Constructor method:
    # Every time a student object is created, it automatically assigns the name, grade, and track attributes to that student.
    # Using double underscores to make grade a private attribute
    def __init__(self, name, __grade, track):
        self.name = name
        self.__grade = __grade
        self.track = track
        
    # Getter for grade:
    # This allows access to the private grade attribute
    def get_grade(self):
        return self.__grade
    
    # Setter for grade:
    # This allows updates to the grade attribute and also includes validation to make sure the new grade is between 0 and 100
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")
        
    # Setting up display method:
    # This method will print out the student's information in a clear format, 
    # including the school name (accessed from the class attribute), student name, grade, and track
    def display_info(self):
        print(f"School: {Student.school}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.get_grade()}")
        print(f"Track: {self.track}")

# Creating student objects:
student1 = Student("Frieren", 98, "The Art of Magic")
student2 = Student("Heiter", 90, "The Art of Healing")

# Testing setter:
student1.set_grade(95)  # valid grade for student1
student2.set_grade(102)  # invalid grade for student2, should trigger error message

# Displaying student information:
print("Student 1 Information:")
student1.display_info()
print("\nStudent 2 Information:")
student2.display_info()

