from school_schedule.student import Student

class Cohort:
    def __init__(self, cohort_name, students=None):
        self.cohort_name = cohort_name
        # Student is a component of Cohort  
        self.students = students if students is not None else []

    def student_summaries(self):
        for student in self.students:
            print(student.summary())

    def class_list(self, class_name):
        class_list = []
        for student in self.students:
                if class_name in student.classes:
                    class_list.append(student.name)
        return class_list


        