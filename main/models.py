from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    slug=models.SlugField()
    content=models.CharField(max_length=256)

    def __str__(self):
        return self.content
class Answer(models.Model):
    question=models.ForeignKey('Question', on_delete=models.CASCADE)
    choices=models.ForeignKey('Choice', on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Choice(models.Model):
    question=models.ForeignKey('Question', on_delete=models.CASCADE)

    content=models.CharField(max_length=256)

    @property
    def answer_count(self):
        return Answer.objects.filter(
            question=self.question,
            choices=self
        ).count()

    def __str__(self):
        return self.question.content+"-"+self.content


