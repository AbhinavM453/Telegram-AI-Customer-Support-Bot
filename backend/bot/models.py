from django.db import models

class ChatMessage(models.Model):
    user_id = models.CharField(max_length=50)
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id
