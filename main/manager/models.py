from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='posts/photos')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title)


class Students(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150, default='example@gmail.com')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
