# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


# Find a single instructor with first name Yan:
instructor_yan = Instructor.objects.get(first_name="Yan")
print("Find a single instructor with first name Yan")
print(instructor_yan)

print("\n")
#Try to find a non-existing instructor with first name Andy
try:
    instructor_andy = Instructor.objects.get(first_name="Andy")
except:
    print("Try to find a non-existing instructor with first name Andy")
    print("Object Instructor Andy not exist")

print("\n")

#Find all part time instructors
part_time_instructors = Instructor.objects.filter(full_time=False)
print("Find all part time instructors")
print(part_time_instructors)

print("\n")

#Find all full time instructors with First Name starts with Y and learners count greater than 30000
full_time_instructors = Instructor.objects.exclude(full_time=False).filter(total_learners__gt=30000).\
    filter(first_name__startswith='Y')
print("Find all full time instructors with First Name starts with Y and learners count greater than 30000")
print(full_time_instructors)

print("\n")

#Find all full time instructors with First Name starts with Y and learners count greater than 30000
#using multiple parameters
full_time_instructors = Instructor.objects.filter(full_time=True, total_learners__gt=30000,
                                                      first_name__startswith='Y')
print("Find all full time instructors with First Name starts with Y \
and learners count greater than 30000 using multiple parameters")
print(full_time_instructors)