from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    birthday = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Animal(models.Model):
    owner = models.ForeignKey(Owner)
    name = models.CharField(max_length=300)
    birthday = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return self.name


class Dog(Animal):
    """"""

class Cat(Animal):
    """"""