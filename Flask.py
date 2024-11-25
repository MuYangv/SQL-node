from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)

# 配置数据库连接
def get_db_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=MYANG;"  # 服务器地址
        "Database=students;"  # 数据库名称
        "Trusted_Connection=yes;"
    )
    return conn

# 获取所有学生
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip([column[0] for column in cursor.description], row)) for row in students])

# 获取单个学生
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudentID=?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    if student:
        return jsonify(dict(zip([column[0] for column in cursor.description], student)))
    else:
        return jsonify({"error": "Student not found"}), 404

# 创建新学生
@app.route('/students', methods=['POST'])
def create_student():
    new_student = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Students (StudentID, Name, StudentNumber, Class) VALUES (?, ?, ?, ?)",
        (new_student['StudentID'], new_student['Name'], new_student['StudentNumber'], new_student['Class'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Student created successfully!"}), 201

# 更新学生信息
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    updated_student = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Students SET Name=?, StudentNumber=?, Class=? WHERE StudentID=?",
        (updated_student['Name'], updated_student['StudentNumber'], updated_student['Class'], student_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Student updated successfully!"})

# 删除学生
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE StudentID=?", (student_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
