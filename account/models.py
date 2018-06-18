from django.db import models

# models

class users(models.Model):
    """user account datatable
    
    Arguments:
        models {class} -- managed by django
    """
    
    userId = models.CharField(max_length=32)  # a unique id
    email = models.CharField(max_length=50)  # because who has a 50 char long email
    name = models.CharField(max_length=32)  # not unique and human readable
    picture = models.CharField(max_length=700) # user picture
    settings = models.CharField(max_length=5000)  # all user settings in a json dict
