from django.db import models

class EmailInvitation(models.Model):
    status_choices = (
        ("new", "New"),
        ("is", "Invite send"),
        ("reg", "Registered"),
    )
    emailid = models.EmailField()
    status = models.CharField(max_length=10, choices=status_choices)
    secret_key = models.CharField(max_length=100)

    def __unicode__(self):
        return self.emailid
