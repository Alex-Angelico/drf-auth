from django.db import models
from django.contrib.auth.models import User

class Jets(models.Model):
    name = models.CharField(max_length=256)
    engines = models.IntegerField(default=0)
    description = models.TextField(default='')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
		
    def __str__(self):
			  return self.name
		
    def get_absolute_url(self):
        return reverse('jets_detail', args=[str(self.id)])


# Create your models here.
