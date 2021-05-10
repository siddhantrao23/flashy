from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Set(models.Model):
    set_name = models.CharField(max_length=200)
    # TODO add topics

    def __str__(self):
        return self.set_name

class Card(models.Model):
    containing_set = models.ForeignKey(Set, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
