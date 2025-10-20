from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=225)
    autor = models.CharField(max_length=225)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome