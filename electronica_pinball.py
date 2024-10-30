import machine
import time
from machine import Pin, PWM, ADC
import random

# Configuración de pines
led_pins = [
    Pin(2, Pin.OUT),  # LED 1
    Pin(3, Pin.OUT),  # LED 2
    Pin(4, Pin.OUT),  # LED 3
    Pin(5, Pin.OUT),  # LED 4
    Pin(6, Pin.OUT),  # LED 5
    Pin(7, Pin.OUT)   # LED 6
]

# Pines para zonas de anotación
score_zones = [
    Pin(8, Pin.IN, Pin.PULL_UP),   # Zona A
    Pin(9, Pin.IN, Pin.PULL_UP),   # Zona B
    Pin(10, Pin.IN, Pin.PULL_UP),  # Zona C
    Pin(11, Pin.IN, Pin.PULL_UP),  # Zona D
    Pin(12, Pin.IN, Pin.PULL_UP)   # Zona E (especial)
]

# Potenciómetro
pot = ADC(26)

# Botón de cambio manual
button = Pin(13, Pin.IN, Pin.PULL_UP)

class PinballGame:
    def __init__(self):
        self.scores = [0, 0]  # Puntuaciones [jugador1, jugador2]
        self.current_player = 0
        self.balls_remaining = 3
        self.auto_change = True
        self.game_active = False
        
    def blink_led(self, led_num, duration=3):
        """Parpadea un LED específico por la duración especificada"""
        for _ in range(duration * 3):  # Parpadeo cada 1/3 segundo
            led_pins[led_num].value(1)
            time.sleep(0.17)
            led_pins[led_num].value(0)
            time.sleep(0.17)
    
    def handle_score_zone(self, zone):
        """Maneja la detección de una zona de anotación"""
        points = 100 if zone < 4 else 500  # Zona especial vale más
        self.scores[self.current_player] += points
        
        # Enciende LEDs correspondientes
        if zone == 4:  # Zona especial
            self.blink_led(4)
            self.blink_led(5)
        else:
            self.blink_led(zone)
            
    def read_potentiometer(self):
        """Lee el valor del potenciómetro y lo mapea a 0-15"""
        return int((pot.read_u16() / 65535) * 15)
    
    def check_zones(self):
        """Verifica todas las zonas de anotación"""
        for i, zone in enumerate(score_zones):
            if zone.value() == 0:  # Contacto detectado
                self.handle_score_zone(i)
                time.sleep(0.1)  # Debounce
    
    def main_loop(self):
        """Bucle principal del juego"""
        while True:
            if self.game_active:
                self.check_zones()
                
                # Verifica botón de cambio manual si no está en modo automático
                if not self.auto_change and button.value() == 0:
                    self.current_player = 1 - self.current_player
                    time.sleep(0.2)  # Debounce
                
                # Envía datos al PC
                print(f"P{self.current_player}:{self.scores[self.current_player]}")
            
            # Lee comandos del PC
            if input_available():  # Función hipotética
                cmd = read_command()  # Función hipotética
                self.process_command(cmd)
            
            time.sleep(0.01)  # Pequeña pausa para no saturar el CPU

    def process_command(self, cmd):
        """Procesa comandos recibidos del PC"""
        if cmd == 'START':
            self.game_active = True
        elif cmd == 'STOP':
            self.game_active = False
        elif cmd == 'RESET':
            self.scores = [0, 0]
            self.balls_remaining = 3
        elif cmd == 'AUTO':
            self.auto_change = True
        elif cmd == 'MANUAL':
            self.auto_change = False

# Iniciar el juego
game = PinballGame()
game.main_loop()