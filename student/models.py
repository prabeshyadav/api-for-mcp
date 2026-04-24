from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(
        Subject, 
        through='CourseAssignment',
        related_name='grades'
    )

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Changed from SchoolClass to Grade to match your model name
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

class CourseAssignment(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='assignments')

    class Meta:
        unique_together = ('grade', 'subject')

    def __str__(self):
        return f"{self.teacher.name} - {self.subject.name} ({self.grade.name})"