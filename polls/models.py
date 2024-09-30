from django.db import models

class job(models.Model):
    pass
class employer(models.Model):
    vacancies = models.ManyToManyField(job)
class employee(models.Model): #, degree = 'bachelor', specialization = 'none', experience = 0):
    jobs = models.ManyToManyField(job)
    boss = models.ManyToManyField(employer)
    # employee.experience = experience
    # employee.specialization = specialization
    # employee.experience = experience