from django.db import models


class Parent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    resume = models.TextField()
    age = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=250)
    date_started = models.DateTimeField()
    gender = models.CharField(max_length=200)
    parent = models.ForeignKey(Parent, related_name='children',
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
