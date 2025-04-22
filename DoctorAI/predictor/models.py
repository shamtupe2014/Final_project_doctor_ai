from django.contrib.auth.models import User
from django.db import models

class GenomeUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genome_file = models.FileField(upload_to='genomes/')
    symptoms = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)