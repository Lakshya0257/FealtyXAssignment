from flask import Blueprint, jsonify, request
from students.services import create_student, get_all_students, get_student_by_id, update_student, delete_student
from students.summary import generate_student_summary

students_blueprint = Blueprint('students', __name__)

@students_blueprint.route('/students', methods=['POST'])
def create_student_route():
    data = request.get_json()
    new_student = create_student(data)
    return jsonify(new_student), 201

@students_blueprint.route('/students', methods=['GET'])
def get_all_students_route():
    return jsonify(get_all_students())

@students_blueprint.route('/students/<int:student_id>', methods=['GET'])
def get_student_route(student_id):
    student = get_student_by_id(student_id)
    if student:
        return jsonify(student.to_dict())
    else:
        return jsonify({'error': 'Student not found'}), 404

@students_blueprint.route('/students/<int:student_id>', methods=['PUT'])
def update_student_route(student_id):
    data = request.get_json()
    student = update_student(student_id, data)
    if student:
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404

@students_blueprint.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student_route(student_id):
    success = delete_student(student_id)
    if success:
        return jsonify({'message': 'Student deleted'}), 200
    else:
        return jsonify({'error': 'Student not found'}), 404

@students_blueprint.route('/students/<int:student_id>/summary', methods=['GET'])
def get_student_summary_route(student_id):
    student = get_student_by_id(student_id)
    if student:
        summary = generate_student_summary(student.to_dict())
        return jsonify({'summary': summary})
    else:
        return jsonify({'error': 'Student not found'}), 404
