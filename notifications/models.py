from django.db import models

from account.models import User
from comman.models import BaseModel


class Notification(BaseModel):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_read = models.BooleanField(default=False)


    class Meta:
        db_table = "notification"
        ordering = ('-created_at',)
