from django.db import models

class Target(models.Model):
    target_id = models.CharField(max_length=200)

    def __str__(self):
        return self.target_id


class Neighbor(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    neighbor_id = models.CharField(max_length=200)
    neighbor_rank = models.IntegerField(default = -1)
    sdss_link = models.CharField(max_length=200, default = '')

    def __str__(self):
        return self.neighbor_id
