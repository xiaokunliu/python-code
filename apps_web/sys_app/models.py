
## TODO add top message 

from django.db import models

# Create your models here.
class AppFeedback(models.Model):
    feed_id = models.PositiveIntegerField(auto_created=True,primary_key=True)
    feed_email = models.EmailField(max_length=50,blank=True,null=True)
    feed_context = models.TextField()
    
    class Meta:
        db_table = "ss_apps_feedback"

