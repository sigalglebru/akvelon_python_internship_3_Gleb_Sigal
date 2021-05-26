from django.db import models
from datetime import date
from users.models import CustomUser


class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='User')
    amount = models.FloatField(verbose_name='Amount (sum)')
    date = models.DateField(default=date.today)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return '{} — ${} ({})'.format(str(self.date), str(self.amount), str(self.user))
