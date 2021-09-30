import uuid
from django.db import models
from datetime import datetime

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=250)

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=250)

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=250)
    description = models.TextField()
    application_link = models.CharField(max_length=250)
    created_at = models.DateField(default=datetime.now, blank=True)
    posted_at = models.CharField(max_length=250)
    posted_on = models.DateField(blank=True)

    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.DO_NOTHING)

class JobTag(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
