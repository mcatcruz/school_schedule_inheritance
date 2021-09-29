class Cohort:
    def __init__(self, cohort_name, students=None):
        self.cohort_name = cohort_name
        self.students = students if students is not None else []

    def student_summaries(self):
        for student in self.students:
            print(student.summary())