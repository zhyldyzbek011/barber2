from django.db import models

from account.serializers import User

from master.models import Master


# class RatingStar(models.Model):
#     value = models.PositiveSmallIntegerField('Знанечение', default=0)
#
#     def __str__(self):
#         return str(self.value)
#
#     class Meta:
#         verbose_name = 'Звезда рейтинга'
#         verbose_name_plural ='Звезда рейтинга'
#         ordering = ['-value']
#
#
# class Rating(models.Model):
#     owner = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE, verbose_name='owner' )
#     star = models.ForeignKey(RatingStar, related_name='ratings', on_delete=models.CASCADE, verbose_name='Звезда')
#     master = models.ForeignKey(Master, related_name='ratings', on_delete=models.CharField, verbose_name='мастер')
#
#     def __str__(self):
#         return f'{self.star} - {self.master} '
#
#     class Meta:
#         verbose_name = 'rating'
#         verbose_name_plural = 'ratings'

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        verbose_name="мастер",
        related_name="ratings"
    )

    def __str__(self):
        return f"{self.star} - {self.master}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
