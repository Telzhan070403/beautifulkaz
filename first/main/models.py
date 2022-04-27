from audioop import reverse
from tabnanny import verbose
from timeit import repeat
from django.db import models
from django.urls import reverse
# Create your models here.
class City(models.Model):
    title = models.CharField('Названия', max_length=50)
    description = models.TextField('Описание', blank = True)
    
    
    def  __str__(self):
        return self.title
    
class  Clothers(models.Model):
    titles = models.CharField('Название', max_length=50)
    description1 = models.TextField('Описание', blank = True)
    
    
    def  __str__(self):
            return self.titles
        
class Food(models.Model):
    word = models.CharField('Название', max_length=50)
    description2 = models.TextField('Описание', blank = True)
    
    
    def  __str__(self):
            return self.word
        
class Singers(models.Model):
    song_name = models.CharField('Название', max_length=50)
    about = models.TextField('Описание', blank = True)
    #picture = models.ImageField(default = 'default value')
    
    
    def  __str__(self):
            return self.song_name
        
    def get_absolute_url(self):
             return f'/singers/{self.id}'
    
class Actors(models.Model):
    actor_name = models.CharField('Название', max_length=50)
    about1 = models.TextField('Описание', blank = True)
    #icture1 = models.ImageField(default = 'default value')
    
    
    def  __str__(self):
            return self.actor_name
        
class Films(models.Model):
    film_name = models.CharField('Название', max_length=80)
    about2 = models.TextField('Описание', blank = True)
    #icture2 = models.ImageField(default = 'default value')
    
    
    def  __str__(self):
            return self.film_name
    
    
class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Username")
    is_published = models.BooleanField(default=True, verbose_name="I read regulations")
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="URL")
    
    def __str__(self):
            return reverse('post',kwargs={'post_slug':self.slug})
        
    def get_number(self):
        return 19

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    
    def __str__(self):
        return self.name
    
class Registration(models.Model):
    title = models.CharField(max_length=255, verbose_name="Username")
    name =  models.CharField(max_length=255, verbose_name="First name")
    surname = models.CharField(max_length=255, verbose_name="Last name")
    email = models.CharField(max_length=255, verbose_name="Email")
    password = models.CharField(max_length=255, verbose_name="Password")
    repeat = models.CharField(max_length=255, verbose_name="Repeat password")
    requement = models.CharField(max_length=255, verbose_name = "phone")
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="Address")
    
    
    def __str__(self):
            return reverse('post',kwargs={'post_slug':self.slug})
    