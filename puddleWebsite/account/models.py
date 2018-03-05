from django.db import models

# models

class account(models.Model):
    """user account datatable
    
    Arguments:
        models {class} -- managed by django
    """
    
    userId = models.CharField(max_length=16)  # a unique id
    username = models.CharField(max_length=32)  # unique and human readable
    email = models.CharField(max_length=50)  # because who has a 50 char long email
    salt = models.CharField(max_length=9)  # unique password salt, changes on pass change
    passHash = models.CharField(max_length=5000)  # encoded in json
    settings = models.CharField(max_length=5000)  # all user settings in a json dict
