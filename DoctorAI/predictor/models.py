from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username

class GenomeUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genome_file = models.FileField(upload_to='genomes/')
    symptoms = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.uploaded_at}"