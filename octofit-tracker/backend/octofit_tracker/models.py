import uuid
from djongo import models

def gen_id():
    return uuid.uuid4().hex[:24]

class Team(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=gen_id)
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=50)  # Marvel, DC, etc.
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=gen_id)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='members')
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=gen_id)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutos
    date = models.DateField()
    def __str__(self):
        return f"{self.type} - {self.user.name}"

class Workout(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=gen_id)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField('Team')
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=gen_id)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team.name}: {self.points}"
