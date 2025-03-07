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


# Find learners name "Smith"
learner_smith = Learner.objects.filter(last_name="Smith")
print("Find learners name 'Smith':")
print(learner_smith)
print("\n")

# Sort by birthdate and pick only 2 objects
learners = Learner.objects.order_by('-dob')[0:2]
print("Sort all Learners objects by birthdate and pick only 2 objects")
print(learners)
