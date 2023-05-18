# -*- coding: utf-8 -*-

import binascii
import struct
import subprocess
import sys
import os 
import socket
import datetime
import time
from inventory import *

class invSend(object):
	def oltMaple(self, ui):
		inv = inventory()
		inv.oltMaple(str(ui.LeOltMapleMac.text()), str(ui.LeOltMapleCprod.text()),
		str(ui.LeOltMapleNserie.text()), str(ui.LeOltMapleData.text()))

		UDP_IP = '192.168.20.1'
		UDP_PORT = 10000

		t = datetime.datetime.now()

		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(str(t), (UDP_IP, UDP_PORT))

			sock.settimeout(5)
			ret = sock.recvfrom(1)

			if ret[0] == '0':
				#Mac
				data = inv.mac

				#Code of product
				data = data + str(inv.codprod)

				#Serial Number
				data = data + str(inv.snumber).zfill(6)

				#Manufactoring date
				data = data + inv.dataf
				sock.sendto(str(data), (UDP_IP, UDP_PORT))
				return "Inventario gravado com sucesso"
			else:
				return "Erro ao gravar inventario"

		except socket.timeout:
			return "Sem conexao com a OLT TimeOut"
