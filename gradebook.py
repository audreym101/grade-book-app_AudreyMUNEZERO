
class Student:
    def __init__(self, email, names, gender, date_of_birth, location, credit_score):
        self.email = email
        self.names = names
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.location = location
        self.credit_score = credit_score
        self.courses_registered = []
        self.gpa = 0.0

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def calculate_GPA(self):
        total_points = sum(course.credits for course in self.courses_registered)
        if total_points > 0:
            self.gpa = sum(course.grade * course.credits for course in self.courses_registered) / total_points
        else:
            self.gpa = 0.0

class Course:
    def __init__(self, name, trimester, credits, grade=0.0):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade = grade


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names, gender, date_of_birth, location, credit_score):
        student = Student(email, names, gender, date_of_birth, location, credit_score)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            course.grade = grade
            student.register_for_course(course)
            student.calculate_GPA()

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.gpa, reverse=True)
        return [(student.names, student.gpa) for student in self.student_list]

    def search_by_grade(self, course_name, min_grade):
        return [student for student in self.student_list if any(course.name == course_name and course.grade >= min_grade for course in student.courses_registered)]

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            return {
                "name": student.names,
                "email": student.email,
                "date_of_birth": student.date_of_birth,
                "location": student.location,
                "credit_score": student.credit_score,
                "gender": student.gender,
                "courses": [(course.name, course.grade, course.credits) for course in student.courses_registered],
                "gpa": student.gpa
            }
        return None

def main():
    gradebook = GradeBook()

    while True:
        print("\nGrade Book Application")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for a course")
        print("4. Calculate ranking")
        print("5. Search by grade")
        print("6. Generate transcript")
        print("7. Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gender = input("Enter student gender (Male/Female): ")
            date_of_birth = input("Enter student date of birth (YYYY-MM-DD): ")
            location = input("Enter student location: ")
            credit_score = int(input("Enter student credit score: "))
            gradebook.add_student(email, names, gender, date_of_birth, location, credit_score)
        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = float(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif choice == "3":
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(student_email, course_name, grade)
        elif choice == "4":
            ranking = gradebook.calculate_ranking()
            for i, (name, gpa) in enumerate(ranking, start=1):
                print(f"{i}. {name} - GPA: {gpa:.2f}")
        elif choice == "5":
            course_name = input("Enter course name: ")
            min_grade = float(input("Enter minimum grade: "))
            students = gradebook.search_by_grade(course_name, min_grade)
            for student in students:
                print(f"{student.names} - Email: {student.email}")
        elif choice == "6":
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            if transcript:
                print(f"Transcript for {transcript['name']}:")
                print(f"Date of Birth: {transcript['date_of_birth']}")
                print(f"Location: {transcript['location']}")
                print(f"Credit Score: {transcript['credit_score']}")
                print(f"Gender: {transcript['gender']}")
                for course in transcript['courses']:
                    print(f"{course[0]}: {course[1]} (Credits: {course[2]})")
                print(f"GPA: {transcript['gpa']:.2f}")
            else:
                print("Student not found.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

