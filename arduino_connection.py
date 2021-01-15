#!/usr/bin/python
# -*- coding: utf-8-*-
import time
import serial


class Arduino_Connection:
  def __init__(self, bits, steps, port, bitrate=9600):
    self.port = port
    self.bitrate = bitrate
    self.bits = bits
    self.steps = steps

  def open_arduino_connection(self):
    # Iniciando conexión serial
    self.conn = serial.Serial(self.port, self.bitrate)
    time.sleep(2) 
  
  def close_arduino_connection(self):
    # Cerrando puerto serial
    self.conn.close()

  def get_arduino_val(self):
    # Leer Linea recibida de conexion serial
    buffer = ""
    while True:
      serial_value = self.conn.read(1)
      if serial_value == b"\r":
        return self.convert_output(int(buffer.strip()))
      else:
        buffer += serial_value.decode("ascii")
  
  def convert_output(self, value):
    # Convierte la salida digital par que sea legible
    digital_out = pow(2,self.bits)
    return ((self.steps/digital_out)*value)-0.1