from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=225)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.title


class Review(Base):
    course = models.ForeignKey(Course, related_name='avaliacoes', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    nota = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'course']

    def _str_(self):
        return f'{self.name} avaliou o curos {self.course} com a nota {self.nota}'
