from typing import Any
from django.db import models


class Home(models.Model):
    img_name = models.ImageField(upload_to='name_images/')
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.team.name
    

class Service(models.Model):
    name = models.CharField(max_length=200)
    tariff = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    partners = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Vacancies(models.Model):
    name = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    working_days = models.CharField(max_length=200)
    start_working = models.CharField(max_length=200)
    end_working = models.CharField(max_length=200)
    requariments = models.TextField()
    tasks = models.TextField()
    technology = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    

class VacancyResume(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    cv = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name
    

class Message(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name


