from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Crear usuarios
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        captain = User.objects.create(email='cap@marvel.com', name='Captain America', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # Crear actividades
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2025-11-01')
        Activity.objects.create(user=batman, type='Cycling', duration=45, date='2025-11-01')

        # Crear workouts
        w1 = Workout.objects.create(name='Super Strength', description='Heavy lifting')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic and flying')
        w1.suggested_for.add(marvel, dc)
        w2.suggested_for.add(dc)

        # Crear leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        # Crear índice único en email de users
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.user.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db poblada con datos de ejemplo.'))
