from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'Поверх {self.floor} Кімната №{self.number}'


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('director-detail', args=[self.id])


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (MALE, 'Актор'),
        (FEMALE, 'Актриса'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актор {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    UAN = 'UAN'

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (UAN, 'Hryvnia'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    slug = models.SlugField(default='', null=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name}-{self.rating}%'
