from django.db import models

class Set(models.Model):
    set_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default='')
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.set_name

class Card(models.Model):
    containing_set = models.ForeignKey(Set, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    answer_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text
