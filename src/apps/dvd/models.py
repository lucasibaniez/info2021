from django.db import models

ESTADO_CHOICES = (
	("A", "ACTIVO"),
	("I", "INACTIVO")
)

class Categoria(models.Model):
	nombre = models.CharField(max_length=255)

	class Meta:
		db_table = 'categorias'

	def __str__(self):
		return self.nombre

class Dvd(models.Model):
	nombre = models.CharField(max_length=255)
	fecha_compra = models.DateTimeField()
	cant_unidades = models.IntegerField(verbose_name='Cantidad de unidades')
	categorias = models.ManyToManyField(Categoria, related_name="categorias")	

	estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default="A")

	estado2 = models.BooleanField(default=True)

	class Meta:
		db_table = 'dvds'
		# verbose_name_plural='Dvdses'

	def __str__(self):
		return f"({self.id}) - {self.nombre}"
"""
class DvdCat(models.Model):
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	dvd = models.ForeignKey(Dvd, on_delete=models.CASCADE)
"""