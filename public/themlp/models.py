from django.db import models

class Customer(models.Model):

    STATUS_CHOICES = (
        ("modem", "モデム"),
        ("wifi", "ポケットワイファイ"),
        ("none", "なし"),
    )

    CAREER_CHOICES = (
        ("sb", "Softbank"),
        ("au", "au by KDDI"),
        ("dcm", "Docomo"),
        ("rk", "Rakuten mobile"),
    )

    MONEY_CHOICES = (
        ("cheaper", "2000円"),
        ("same", "3800円"),
        ("expensive", "はい"),
    )

    controller = models.BooleanField(default=True)
    status = models.CharField(max_length=15, verbose_name="利用状況", blank=False, null=False, choices=STATUS_CHOICES)
    career = models.CharField(max_length=20, verbose_name="キャリア", blank=False, null=False, choices=CAREER_CHOICES)
    money = models.CharField(max_length=20, verbose_name="現状利用価格", blank=False, null=False, choices=MONEY_CHOICES, default="")



    def __int__(self):
        return self.id
