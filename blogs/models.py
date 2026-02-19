from django.db import models


class Blog(models.Model):
    """
    Класс блогов
    """

    title = models.CharField(max_length=200, verbose_name="заголовок", help_text="Введите название заголовок")
    content = models.TextField(verbose_name="содержимое", help_text="Введите содержимое")
    img = models.ImageField(verbose_name="превью", upload_to="images/blogs", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="признак публикации")
    viewcount = models.IntegerField(verbose_name="количество просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title"]
