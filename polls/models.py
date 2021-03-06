
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question} - {self.choice_text}'

class Carousel(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=250)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.title