from django.db import models

# Create your models here.


class EnQuestion(models.Model):

    id                  = models.IntegerField(primary_key=True, unique=True)
    question            = models.CharField(max_length=500)
    question_id         = models.IntegerField(default=1)
    correct_choice      = models.CharField(max_length=200, null=False, blank=False)
    selected_choice     = models.CharField(max_length=200, null=True, blank=True)
    is_correct          = models.IntegerField(default=0)
    date                = models.DateTimeField(auto_now_add=True)
    update_date         = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.question

    def next_url(self):
        return (self.id + 1)
    
    def progress(self):
        return (self.id - 1) * 5


class EnChoice(models.Model):

    question = models.ForeignKey(EnQuestion, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)

    def __str__(self):
        return self.choice


class FrQuestion(models.Model):

    id                  = models.IntegerField(primary_key=True, unique=True)
    question            = models.CharField(max_length=500)
    question_id         = models.IntegerField(default=1)
    correct_choice      = models.CharField(max_length=200, null=False, blank=False)
    selected_choice     = models.CharField(max_length=200, null=True, blank=True)
    is_correct          = models.IntegerField(default=0)
    date                = models.DateTimeField(auto_now_add=True)
    update_date         = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.question

    def next_url(self):
        return (self.id + 1)
    
    def progress(self):
        return (self.id - 1) * 5


class FrChoice(models.Model):

    question = models.ForeignKey(FrQuestion, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)

    def __str__(self):
        return self.choice

