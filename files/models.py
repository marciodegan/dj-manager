from django.db import models

# Create your models here.

class File(models.Model):
    file_name = models.FileField(upload_to='files/filebackup')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"


class FileLancamento(models.Model):
    file_name = models.FileField(upload_to='files/filebackup')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"


class FileDate(models.Model):
    file_name = models.FileField(upload_to='files/filebackup')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"