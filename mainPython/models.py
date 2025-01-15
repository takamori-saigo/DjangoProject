from django.db import models


class Statistic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')

class tableStatistic(models.Model):
    stat = models.ForeignKey(Statistic, on_delete=models.CASCADE, related_name='tables', verbose_name="название статистики")
    name = models.CharField(max_length=255, verbose_name="название таблицы")
    data = models.TextField(verbose_name="HTML")
    image = models.ImageField(upload_to='main/img', verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.name

class MainPageContent(models.Model):

    titlePage = models.CharField(max_length=200, verbose_name='заголовок')

    titleContent = models.CharField(max_length=200, verbose_name='заголовок темы')

    contentPage = models.TextField(verbose_name='контент(html)')

    def __str__(self):
        return self.titlePage

