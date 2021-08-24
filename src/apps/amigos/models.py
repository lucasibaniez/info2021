from django.db import models

class Amigo(models.Model):
	nombre = models.CharField(max_length=255)
	domicilio = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255, null=True, blank=True)


	class Meta:
		db_table = 'amigos'

	def __str__(self):
		return self.nombre


CEL_CHOICES = (
	("0", "--"),
	("15", "15")
)

class Telefono(models.Model):
	amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)
	codigo_area = models.CharField(max_length=4)
	codigo_celular = models.CharField(max_length=2, choices=CEL_CHOICES)
	numero = models.CharField(max_length=15)

	class Meta:
		db_table = 'telefonos'

	def __str__(self):
		if self.codigo_celular == "15":
			return f"({self.codigo_area}) - {self.codigo_celular} {self.numero}"

		return f"({self.codigo_area}) - {self.numero}"

