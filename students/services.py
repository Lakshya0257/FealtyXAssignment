from students.models import students, Student

def create_student(data):
    new_student = Student(len(students) + 1, data['name'], data['age'], data['email'])
    students.append(new_student)
    return new_student.to_dict()

def get_all_students():
    return [student.to_dict() for student in students]

def get_student_by_id(student_id):
    return next((student for student in students if student.id == student_id), None)

def update_student(student_id, data):
    student = get_student_by_id(student_id)
    if student:
        student.name = data['name']
        student.age = data['age']
        student.email = data['email']
    return student.to_dict() if student else None

def delete_student(student_id):
    student = get_student_by_id(student_id)
    if student:
        students.remove(student)
    return student is not None
