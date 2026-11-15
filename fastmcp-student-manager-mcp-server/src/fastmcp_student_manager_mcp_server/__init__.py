
# from mcp.server import MCPServer
from fastmcp import FastMCP


mcp = FastMCP(name="student-manager-server")


# In-memory student database
STUDENTS = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 15,
        "class": "10th",
        "roll_number": 101
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 13,
        "class": "8th",
        "roll_number": 102
    },
    {
        "id": 3,
        "name": "Amit",
        "age": 14,
        "class": "9th",
        "roll_number": 103
    }
]


# 1. Get all students
@mcp.tool()
def get_all_students() -> list:
    """Return a list of all students."""
    return STUDENTS


# 2. Add a new student
@mcp.tool()
def add_student(
    name: str,
    age: int,
    student_class: str,
    roll_number: int
) -> dict:
    """Add a new student to the student database."""

    # Check if roll number already exists
    for student in STUDENTS:
        if student["roll_number"] == roll_number:
            return {
                "success": False,
                "message": "Roll number already exists"
            }

    new_student = {
        "id": max(
            (student["id"] for student in STUDENTS),
            default=0
        ) + 1,
        "name": name,
        "age": age,
        "class": student_class,
        "roll_number": roll_number
    }

    STUDENTS.append(new_student)

    return {
        "success": True,
        "message": "Student added successfully",
        "student": new_student
    }


# 3. Update an existing student
@mcp.tool()
def update_student(
    student_id: int,
    name: str = None,
    age: int = None,
    student_class: str = None,
    roll_number: int = None
) -> dict:
    """Update an existing student's details using student ID."""

    for student in STUDENTS:
        if student["id"] == student_id:

            if roll_number is not None:
                if any(
                    s["id"] != student_id
                    and s["roll_number"] == roll_number
                    for s in STUDENTS
                ):
                    return {
                        "success": False,
                        "message": "Roll number already exists"
                    }

            if name is not None:
                student["name"] = name

            if age is not None:
                student["age"] = age

            if student_class is not None:
                student["class"] = student_class

            if roll_number is not None:
                student["roll_number"] = roll_number

            return {
                "success": True,
                "message": "Student updated successfully",
                "student": student
            }

    return {
        "success": False,
        "message": "Student not found"
    }


# 4. Get students by roll number
@mcp.tool()
def get_students_by_roll_number(roll_number: int) -> list:
    """Return students matching the given roll number."""

    return [
        student
        for student in STUDENTS
        if student["roll_number"] == roll_number
    ]


if __name__ == "__main__":
    mcp.run(transport="streamable-http",
        host="0.0.0.0",
        port=8000)
