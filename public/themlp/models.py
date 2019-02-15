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

    M_CHOICES = (
        ("ntt", 'NTT'),
        ("au", "au光"),
        ("sb","sb光"),
        ("hc","光コラボ"),
        ("jc", "j:com"),
        ("eo","eo光"),
    )

    controller = models.BooleanField(default=True)
    status = models.CharField(max_length=15, verbose_name="利用状況", blank=False, null=False, choices=STATUS_CHOICES)
    m_name = models.CharField("回線名", max_length="25", blank=True, null=True, default="わからない", choices=M_CHOICES)
    career = models.CharField(max_length=20, blank=False, null=False, choices=CAREER_CHOICES)

    def __str__(self):
        return self.id
