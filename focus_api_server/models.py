from django.db import models
class Plan(models.Model):
    types = models.CharField(max_length=60)
    content = models.TextField()
    def __str__(self):
        return self.content[:50] + '...'
