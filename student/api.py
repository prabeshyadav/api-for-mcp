from typing import List
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from ninja import NinjaAPI
from django.db import IntegrityError
# /app/student/api.py
from .models import Student, Teacher, Subject, Grade, CourseAssignment
# In student/api.py
from .schema import TeacherSchema  # Change TeacherIn to TeacherSchema
from .schema import (
    StudentOut, StudentCreateSchema,
    TeacherSchema, TeacherIn,
    SubjectSchema, SubjectCreateSchema,
    GradeOut, GradeCreateSchema,
    CourseAssignmentOut, CourseAssignmentCreate
)


api = NinjaAPI(title="School Management System API")


@api.post("/subjects", response={201: SubjectSchema}, tags=["Subjects"])
def create_subject(request, data: SubjectCreateSchema):
    subject = Subject.objects.create(**data.dict())
    return 201, subject

@api.get("/subjects", response=List[SubjectSchema], tags=["Subjects"])
def list_subjects(request):
    return Subject.objects.all()

# --- GRADE ENDPOINTS ---

@api.post("/grades", response={201: GradeOut}, tags=["Grades"])
def create_grade(request, data: GradeCreateSchema):
    grade = Grade.objects.create(**data.dict())
    return 201, grade

@api.get("/grades", response=List[GradeOut], tags=["Grades"])
def list_grades(request):
    return Grade.objects.all()


@api.get("/grades/{grade_id}", response=GradeOut, tags=["Grades"])
def get_grade(request, grade_id: int):
    """
    Returns the grade and all subjects assigned to it 
    (e.g., 4 for Grade 1, 10 for Grade 9).
    """
    return get_object_or_404(Grade, id=grade_id)

# --- ASSIGNMENT ENDPOINTS (The Logic) ---

@api.post("/assignments", response={201: CourseAssignmentOut}, tags=["Assignments"])
def assign_teacher_to_subject(request, data: CourseAssignmentCreate):
    """
    This is where you link a Subject to a Grade and assign a Teacher.
    """
    assignment = CourseAssignment.objects.create(
        grade_id=data.grade_id,
        subject_id=data.subject_id,
        teacher_id=data.teacher_id
    )
    return 201, assignment

# --- STUDENT ENDPOINTS ---

@api.post("/students", response={201: StudentOut}, tags=["Students"])
def create_student(request, data: StudentCreateSchema):
    # We pull the grade_id from the schema to link the student
    student = Student.objects.create(
        name=data.name,
        age=data.age,
        grade_id=data.grade_id
    )
    return 201, student

@api.get("/students", response=List[StudentOut], tags=["Students"])
def list_students(request):
    return Student.objects.select_related('grade').all()

@api.post("/teachers", response={201: TeacherSchema}, tags=["Teachers"])
def create_teacher(request, data: TeacherIn):
    teacher = Teacher.objects.create(**data.dict())

    return 201, teacher

@api.get("/teachers", response=List[TeacherSchema], tags=["Teachers"])
def list_teachers(request):
    return Teacher.objects.all()

@api.post("/assignments", response={201: CourseAssignmentOut}, tags=["Assignments"])
def create_assignment(request, data: CourseAssignmentCreate):
    """
    Links a Subject to a Grade and assigns a Teacher.
    """
    assignment = CourseAssignment.objects.create(
        grade_id=data.grade_id,
        subject_id=data.subject_id,
        teacher_id=data.teacher_id
    )
    return 201, assignment

@api.get("/grades/{grade_id}/curriculum", response=List[CourseAssignmentOut], tags=["Grades"])
def get_grade_curriculum(request, grade_id: int):
    # This fetches all subjects and teachers assigned to a specific grade
    return CourseAssignment.objects.filter(grade_id=grade_id).select_related('subject', 'teacher')

@api.get("/teachers/{teacher_id}/assignments", response=List[CourseAssignmentOut], tags=["Teachers"])
def get_teacher_assignments(request, teacher_id: int):
    """
    Returns a list of all grades and subjects this teacher is assigned to.
    """
    # select_related joins the tables so you get the Grade and Subject names too
    return CourseAssignment.objects.filter(teacher_id=teacher_id).select_related('grade', 'subject')