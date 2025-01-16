from django.db import models

class Geography_statistic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')

class Table_Geography(models.Model):
    stat = models.ForeignKey(Geography_statistic, on_delete=models.CASCADE, related_name='tables', verbose_name="название статистики")
    name = models.CharField(max_length=255, verbose_name="название таблицы")
    data = models.TextField(verbose_name="HTML")
    image = models.ImageField(upload_to='main/img', verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.name

class Demand_statistic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')

class Table_Demand(models.Model):
    stat = models.ForeignKey(Demand_statistic, on_delete=models.CASCADE, related_name='tables', verbose_name="название статистики")
    name = models.CharField(max_length=255, verbose_name="название таблицы")
    data = models.TextField(verbose_name="HTML")
    image = models.ImageField(upload_to='main/img', verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    
    title = models.CharField(max_length=255)

    description = models.TextField()

    skills = models.CharField(max_length=255)

    company = models.CharField(max_length=255)

    salary = models.CharField(max_length=255, blank=True, null=True)

    region = models.CharField(max_length=255)

    published_at = models.DateTimeField()

    vacancy_url = models.URLField()


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

class Skills_statistic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')

class Table_Skills(models.Model):
    stat = models.ForeignKey(Skills_statistic, on_delete=models.CASCADE, related_name='tables', verbose_name="название статистики")
    name = models.CharField(max_length=255, verbose_name="название таблицы")
    data = models.TextField(verbose_name="HTML")
    image = models.ImageField(upload_to='main/img', verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.name
    
