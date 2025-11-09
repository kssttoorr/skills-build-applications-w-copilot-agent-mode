from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        user = User.objects.create(email='tony@stark.com', name='Tony Stark', team=team)
        Activity.objects.create(user=user, type='Running', duration=30, date='2025-11-01')
        Workout.objects.create(name='Super Strength', description='Heavy lifting')
        Leaderboard.objects.create(team=team, points=100)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
