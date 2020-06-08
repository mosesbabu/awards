from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

# Create your models here.
class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,categories):
        cls.objects.filter(categories=categories).delete()


class technologies(models.Model):
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.technologies

    def save_technology(self):
        self.save()

    @classmethod
    def delete_technology(cls,technologies):
        cls.objects.filter(technologies=technologies).delete()


class colors(models.Model):
    colors = models.CharField(max_length=100)

    def __str__(self):
        return self.colors

    def save_color(self):
        self.save()

    @classmethod
    def delete_color(cls,colors):
        cls.objects.filter(colors=colors).delete()

class countries(models.Model):
    countries = models.CharField(max_length=100)

    def __str__(self):
        return self.countries

    class Meta:
        ordering = ['countries']


    def save_country(self):
        self.save()

    @classmethod
    def delete_country(cls,countries):
        cls.objects.filter(countries=countries).delete()

class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='landingpage/')
    description = HTMLField()
    link= models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    screenshot1 = models.ImageField(upload_to='screenshots/')
    screenshot2 = models.ImageField(upload_to='screenshots/')
    screenshot3 = models.ImageField(upload_to='screenshots/')
    screenshot4 = models.ImageField(upload_to='screenshots/')
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    country = models.ForeignKey(countries,on_delete=models.CASCADE)
    technologies = models.ManyToManyField(technologies)
    categories = models.ManyToManyField(categories)
    colors = models.ManyToManyField(colors)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls,search_term):
        # projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(colors__colors=search_term) | Q(technologies__technologies=search_term) | Q(categories__categories=search_term) | Q(country__countries=search_term))
        projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(country__countries=search_term) | Q(overall_score__icontains=search_term))
        return projects


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    country = models.ForeignKey(countries,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
