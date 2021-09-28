from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes) 
        self.gets_transportation = gets_transportation
    
    def summary(self):
        student_sumamry = super().summary()
        transportation_message = self.display_transportation_message()

        return "\n".join(student_sumamry, transportation_message)

    def display_transportation_message(self):
        gets_message = "gets" if self.gets_transportation else "doesn't get"
        return f"{self.name} {gets_message} transportation"