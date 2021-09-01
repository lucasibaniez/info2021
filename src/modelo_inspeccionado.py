# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amigos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amigos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Categorias(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'categorias'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Usuarios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dvds(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    fecha_compra = models.DateTimeField()
    cant_unidades = models.IntegerField()
    estado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dvds'


class DvdsCategorias(models.Model):
    id = models.BigAutoField(primary_key=True)
    dvd = models.ForeignKey(Dvds, models.DO_NOTHING)
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dvds_categorias'
        unique_together = (('dvd', 'categoria'),)


class Telefonos(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo_area = models.CharField(max_length=4)
    codigo_celular = models.CharField(max_length=2)
    numero = models.CharField(max_length=15)
    amigo = models.ForeignKey(Amigos, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'telefonos'


class Usuarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    apodo = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class UsuariosGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuarios_groups'
        unique_together = (('usuario', 'group'),)


class UsuariosUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuarios_user_permissions'
        unique_together = (('usuario', 'permission'),)
