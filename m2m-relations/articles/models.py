from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField('Scope', related_name='Scope', through='ScopesInArticle')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    """
    Разделы
    """

    topic = models.CharField(max_length=256, verbose_name='Название раздела')

    def __str__(self):
        return self.topic


class ScopesInArticle(models.Model):
    scope = models.ForeignKey(Scope, verbose_name='Scope', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='Article', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Главный раздел', default=False)

    def __str__(self):
        return f"{self.id} -- {self.article.scopes}"