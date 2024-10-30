import machine
import time

# Configurar pines para el 74164
pinEntradaA = machine.Pin(15, machine.Pin.OUT)  # Entrada A (Serial)
pinClock = machine.Pin(16, machine.Pin.OUT)     # Reloj (Clock)
pinClear = machine.Pin(17, machine.Pin.OUT)     # Borrar (Clear)

# Inicializar pines
pinEntradaA.value(0)
pinClock.value(0)
pinClear.value(1)  # Mantener CLR en alto para funcionamiento normal

# Función para enviar un bit al registro
def enviar_bit(bit):
    pinEntradaA.value(bit)   # Establecer valor en la entrada A
    pinClock.value(1)        # Generar pulso de reloj
    time.sleep(0.1)          # Espera corta
    pinClock.value(0)

# Secuencia de bits para enviar al registro 
secuencia_bits = [0, 1, 0, 0, 1, 1, 0, 1]

# Enviar cada bit de la secuencia al registro
for bit in secuencia_bits:
    enviar_bit(bit)
    time.sleep(1)  # Pausa entre cada bit enviado
