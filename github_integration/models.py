from django.db import models

# Create your models here.
class repo_issues(models.Model):
    user = models.CharField(max_length=100, null= True, blank= True)
    state = models.CharField(max_length=50, null= True, blank= True)
    labels = models.IntegerField(null= True, blank= True)
    create_date = models.DateField(null= True, blank= True)