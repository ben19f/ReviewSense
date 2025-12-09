from django.db import models

class Feedback(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True, null=True)  # pos/neg/neutral
    summary = models.TextField(blank=True, null=True)
    categories = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]

