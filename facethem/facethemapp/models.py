from django.db import models
import datetime

#Korisnik
class User(models.Model):
    player_id = models.CharField(max_length=200, primary_key=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    date = models.DateField(null=True)
    avatar = models.CharField(max_length=200,null=True)
    cover_image = models.CharField(max_length=200,null=True)
    date_created = models.DateField(default=datetime.date.today)
    def __repr__(self):
        return f"{self.username}"

#Match
class Match(models.Model):
    match_id = models.CharField(max_length=200, primary_key=True)
    winner = models.IntegerField()
    player = models.ForeignKey(User, on_delete=models.CASCADE)

#Tim koji je sacinjen od 5 igraca
class Team(models.Model):
    team_no = models.IntegerField()
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    player_id = models.CharField(max_length=200)

#Predstavljanje prijateljstva
class Friendship(models.Model):
    date_friends = models.DateTimeField()
    person_1 = models.ForeignKey(User,related_name='person_1', on_delete=models.CASCADE)
    person_2 = models.ForeignKey(User,related_name='person_2', on_delete=models.CASCADE)

