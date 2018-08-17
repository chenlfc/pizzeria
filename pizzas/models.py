from django.db import models

# Create your models here.


class Pizza(models.Model):
    """一个描述披萨的类"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回披萨的名字"""
        return self.name


class Topping(models.Model):
    """用于存储披萨的配料"""
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回披萨的配料"""
        if len(self.name) > 50:
            # space_num = '-' * 25
            return self.name[:50] + '...'  # + space_num + str(self.date_added)
        else:
            # space_num = '-' * ((25 - len(self.name)) + 28)
            return self.name  # + space_num + str(self.date_added)
