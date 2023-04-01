from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    menu_name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
