from django.db import models

class Customer(models.Model):

    STATUS_CHOICES = (
        ("modem", "モデム"),
        ("wifi", "ワイファイ"),
        ("none", "なし"),
    )

    CAREER_CHOICES = (
        ("sb", "Softbank"),
        ("au", "au by KDDI"),
        ("dcm", "Docomo"),
        ("rk", "Rakuten mobile"),
    )

    controller = models.BooleanField(default=True)
    status = models.CharField(max_length=15, verbose_name="利用状況", blank=False, null=False, choices=STATUS_CHOICES)
    career = models.CharField(max_length=20, blank=False, null=False, choices=CAREER_CHOICES)

    def __str__(self):
        return self.id
