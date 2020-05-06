from django.db import models


class GWevent(models.Model):
    gwevent = models.CharField(max_length=64)


class GWfield(models.Model):
    field = models.CharField(max_length=64)
    gwevent = models.ForeignKey(GWevent, on_delete=models.CASCADE, blank=True, null=True)


class GWCandidate(models.Model):
    candidate_id = models.CharField(max_length=64)
    ra = models.CharField(max_length=64)
    dec = models.CharField(max_length=64)
    imagedir = models.CharField(max_length=128)
    likelyvote = models.IntegerField(default=0)
    possiblevote = models.IntegerField(default=0)
    unlikelyvote = models.IntegerField(default=0)
    percentlikely = models.FloatField(default=0)
    percentpossible = models.FloatField(default=0)
    field = models.ForeignKey(GWfield, on_delete=models.CASCADE, blank=True, null=True)
    gwevent = models.ForeignKey(GWevent, on_delete=models.CASCADE, blank=True, null=True)
    snr = models.FloatField(default=0)


