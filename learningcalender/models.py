from django.db import models
from multiselectfield import MultiSelectField
from courses.models import LearningCourses

# Create your models here.

WEEK_DAYS = (
    ('0', 'Shanbe'),
    ('1', 'YekShanbe'),
    ('2', 'DoShanbe'),
    ('3', 'SeShanbe'),
    ('4', 'CharShanbe'),
    ('5', 'PanjShanbe'),
    ('6', 'Jomae'),
)

class WinterSchedule (models.Model):
    course_name = models.ForeignKey(LearningCourses, on_delete=models.CASCADE, related_name="course")
    start_date = models.DateField(verbose_name="")
    session_date = MultiSelectField(choices=WEEK_DAYS, verbose_name="روز های برگذاری")
    session_time = models.TimeField()
    enrollment_capacity = models.IntegerField(verbose_name="ظرفیت ثبت نام")
    group = models.ManyToManyField(LearningCourses, related_name="catagory")


class AutumnSchedule (models.Model):
    course_name = models.ForeignKey(LearningCourses, on_delete=models.CASCADE, related_name="course_name")
    start_date = models.DateField(verbose_name="")
    session_date = MultiSelectField(choices=WEEK_DAYS, verbose_name="روز های برگذاری")
    session_time = models.TimeField()
    enrollment_capacity = models.IntegerField(verbose_name="ظرفیت ثبت نام")
    group = models.ManyToManyField(LearningCourses, related_name="amir")