from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def __str__(self):
        return self.title
