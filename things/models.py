from django.db import models

class Things(models.Model):
    CHOICE_ACT = (
        ('YES', "YES"),
        ('NO', "NO")
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    act = models.CharField(max_length=100, choices=CHOICE_ACT)
    cost = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


