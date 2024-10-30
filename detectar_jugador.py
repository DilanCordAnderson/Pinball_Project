from machine import Pin
import time

# Configuración de los pines
led_brownie = Pin(32, Pin.OUT)
led_job = Pin(31, Pin.OUT)

from machine import Pin, UART
import time

# Configuración de los LEDs
led_brownie = Pin(32, Pin.OUT)
led_job = Pin(31, Pin.OUT)

# Configuración de UART para la comunicación serial
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))  # Usa los pines 0 y 1 para UART

def actualizar_leds(jugador):
    if jugador == "brownie":
        led_brownie.on()
        led_job.off()
    elif jugador == "job":
        led_brownie.off()
        led_job.on()
    else:
        led_brownie.off()
        led_job.off()

# Bucle principal para leer el nombre del jugador y actualizar LEDs
while True:
    if uart.any():
        jugador = uart.readline().decode().strip()  # Leer y decodificar el mensaje
        actualizar_leds(jugador)  # Actualizar LEDs en función del jugador recibido
    time.sleep(0.1)

