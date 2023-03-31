from django.db import models


class Routine(models.Model):
    name = models.CharField(max_length=200)


class Week(models.Model):
    routine = models.ForeignKey("Routine", on_delete=models.CASCADE)
    number = models.IntegerField(default=0)


class Workout(models.Model):
    week = models.ForeignKey("Week", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    DAYS_OF_WEEK = (
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    )
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)


class Exercise(models.Model):
    workout = models.ForeignKey("Workout", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    min_reps = models.IntegerField(default=0)
    max_reps = models.IntegerField(default=0)


class Set(models.Model):
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    reps = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True)
