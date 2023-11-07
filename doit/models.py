from django.db import models

# Create your models here.
class DOITLIST(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    done_date = models.DateTimeField()
    is_done = models.BooleanField()
    
    def __str__(self):
        return self.subject