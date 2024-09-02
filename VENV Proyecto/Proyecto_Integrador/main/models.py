from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=20)
    mail = models.CharField(max_length=60)
    
    def __str__(self):
        return str(self.id_cliente)

class PistaBowling(models.Model):
    id_pista = models.AutoField(primary_key=True)
    capacidad_maxima = models.IntegerField()
    descripcion = models.CharField(max_length=240)
    
    ESTADOS_PISTA = (
        ('DIS', 'Disponible'),
        ('OCU', 'Ocupada'),
        ('MAN', 'Mantenimiento'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS_PISTA)
    
    def __str__(self):
        return str(self.id_pista)

class EstadoPista(models.Model):
    estado = models.CharField(max_length=20, primary_key=True)
    descripcion = models.CharField(max_length=240)
    
    def __str__(self):
        return str(self.estado)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_pista = models.ForeignKey(PistaBowling, on_delete=models.CASCADE)
    fecha_hora_reserva = models.DateField()

    ESTADOS_RESERVA = (
        ('PEN', 'Pendiente'),
        ('CONF', 'Confirmada'),
        ('CAN', 'Cancelada'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA)
    
    def __str__(self):
        return str(self.id_reserva)

class Partida(models.Model):
    id_partida = models.AutoField(primary_key=True)
    id_pista = models.ForeignKey(PistaBowling, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    
    ESTADOS_PARTIDA = (
        ('INI', 'Iniciada'),
        ('TER', 'Terminada'),
        ('CAN', 'Cancelada'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS_PARTIDA)
    
    def __str__(self):
        return str(self.id_partida)

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha_hora_pedido = models.DateField()
    
    ESTADOS_PEDIDO = (
        ('PEN', 'Pendiente'),
        ('PRO', 'Procesando'),
        ('COM', 'Completado'),
        ('CAN', 'Cancelado'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO)
    
    def __str__(self):
        return str(self.id_pedido)

class Jugador(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    id_partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    nombre_jugador = models.CharField(max_length=10)
    orden = models.IntegerField()

    class Meta:
        unique_together = ('id_jugador', 'id_partida')
        
    def __str__(self):
        return str(self.id_jugador, self.id_partida)

class Turno(models.Model):
    numero_turno = models.AutoField(primary_key=True)
    id_partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    orden = models.CharField(max_length=20)
    ultimo_turno = models.BooleanField()
    
    def __str__(self):
        return str(self.numero_turno)

class Tirada(models.Model):
    numero_tirada = models.AutoField(primary_key=True)
    pinos_deribados = models.IntegerField()
    orden = models.IntegerField()
    id_jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    numero_turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.numero_tirada)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=240)
    precio = models.IntegerField()
    
    def __str__(self):
        return str(self.id_producto)

class PedidoXProducto(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ('id_pedido', 'id_producto')
        
    def __str__(self):
        return str(self.id_pedido, self.id_producto)

class HistorialEstado(models.Model):
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    
    ESTADOS_RESERVA = (
        ('PEN', 'Pendiente'),
        ('CONF', 'Confirmada'),
        ('CAN', 'Cancelada'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA)
    
    
    fecha_hora_inicio = models.DateField()
    fecha_hora_fin = models.DateField()

    class Meta:
        unique_together = ('id_reserva', 'estado')
        
    def __str__(self):
        return str(self.id_reserva, self.estado)
