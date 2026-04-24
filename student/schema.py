from typing import List, Optional
from ninja import Schema, ModelSchema
from .models import Student, Teacher, Subject, Grade, CourseAssignment

# --- 1. Subject Schemas ---
class SubjectSchema(Schema):
    id: int
    name: str

class SubjectCreateSchema(Schema):
    name: str

# --- 2. Teacher Schemas ---
class TeacherSchema(Schema):
    id: int
    name: str
    email: str
    
    

# Add this to your student/schema.py
class TeacherIn(Schema):
    name: str
    email: str

class GradeSchema(Schema):
    id: int
    name: str

# --- 3. Assignment Schemas (The Bridge) ---
class CourseAssignmentOut(Schema):
    id: int
    grade: GradeSchema
    subject: SubjectSchema
    teacher: TeacherSchema
    # We don't include Grade here to avoid circular recursion 
    # when GradeOut calls this schema.

class CourseAssignmentCreate(Schema):
    subject_id: int
    teacher_id: int
    grade_id: int

# --- 4. Grade Schemas ---
class GradeOut(Schema):
    id: int
    name: str
    # This will return the list of assignments (subject + teacher) for the grade
    assignments: List[CourseAssignmentOut] = [] 

    @staticmethod
    def resolve_assignments(obj):
        # This helper method fetches the 'through' model data
        return CourseAssignment.objects.filter(grade=obj)

class GradeCreateSchema(Schema):
    name: str

# --- 5. Student Schemas ---
class StudentOut(Schema):
    id: int
    name: str
    age: int
    grade: GradeCreateSchema # Simple grade info (id/name)

class StudentCreateSchema(Schema):
    name: str
    age: int
    grade_id: int