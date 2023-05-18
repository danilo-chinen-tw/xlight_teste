# -*- coding: utf-8 -*-

import binascii
import struct
import subprocess
import sys
import os 
from inventory import *

class invfile(object):
	def olt(self, ui):
		f = open('tftpboot/oltinv','w')
		inv = inventory()
		inv.olt(str(ui.LeOltMac.text()), str(ui.LeOltDproduto.text()),
				str(ui.LeOltCprod.text()), str(ui.LeOltNserie.text()),
				str(ui.LeOltData.text()), str(ui.LeOltNpedido.text()),
				str(ui.LeOltVhw.text()), str(ui.LeOltVfw.text()), 
				str(ui.LeOltSystem.text()), str(ui.LeOltAsgos.text()), 
				str(ui.LeOltStartup.text()), str(ui.LeOltTec.text()),
				str(ui.LeOltResets.text()))
		
		#Mac
		tmp = binascii.a2b_hex(inv.mac)
		data = struct.pack("6s", tmp)
		f.write(data)
		
		#Description
		data = struct.pack("30s", inv.descricao)
		f.write(data)
		
		#Code of product
		data = struct.pack(">H", inv.codprod)
		f.write(data)
		
		#Serial Number
		data = struct.pack(">I", inv.snumber)
		f.write(data)
		
		#Manufactoring date
		data = struct.pack("11s", inv.dataf)
		f.write(data)
		
		#Order Number
		data = struct.pack(">H", inv.npedido)
		f.write(data)
		
		#Hardware Version
		data = struct.pack(">B", inv.vhw)
		f.write(data)
		
		#Firmware Version
		data = struct.pack(">B", inv.vfw)
		f.write(data)
		
		#System Version
		data = struct.pack("16s", inv.vsystem)
		f.write(data)
		
		#Startup Version
		data = struct.pack("16s", inv.vstartup)
		f.write(data)
		
		#Asgos Version
		data = struct.pack("16s", inv.vasgos)
		f.write(data)
		
		#Notes
		data = struct.pack("100s", inv.notas)
		f.write(data)
		
		#Resets
		data = struct.pack("H", inv.nresets)
		f.write(data)
		
		f.close()
		if sys.platform == "win32":
			os.system("ccrypt.exe -efK dp2a3r2mhbolt tftpboot/oltinv")
		else:
			os.system("ccrypt -efK dp2a3r2mhbolt tftpboot/oltinv")

		
	def onu(self, ui):
		f = open('tftpboot/onuinv','wb')
		inv = inventory()
		inv.onu(str(ui.LeOnuMac.text()), str(ui.LeOnuDproduto.text()),
				str(ui.LeOnuCprod.text()), str(ui.LeOnuNserie.text()),
				str(ui.LeOnuNspon.text()), str(ui.LeOnuData.text()), 
				str(ui.LeOnuNpedido.text()), str(ui.LeOnuVhw.text()),
				str(ui.LeOnuVfw.text()), str(ui.LeOnuSystem.text()),  
				str(ui.LeOnuTec.text()), str(ui.LeOnuResets.text()))
		
		#Mac
		tmp = binascii.a2b_hex(inv.mac)
		data = struct.pack("6s", tmp)
		f.write(data)
		
		#Description
		data = struct.pack("30s", inv.descricao)
		f.write(data)
		
		#Code of product
		data = struct.pack(">H", inv.codprod)
		f.write(data)
		
		#Serial Number
		data = struct.pack(">I", inv.snumber)
		f.write(data)
		
		#Pon Serial Number
		tmp = binascii.a2b_hex(inv.snpon)
		data = struct.pack("8s", tmp)
		f.write(data)
		
		
		#Manufactoring date
		data = struct.pack("11s", inv.dataf)
		f.write(data)
		
		#Order Number
		data = struct.pack(">H", inv.npedido)
		f.write(data)
		
		#Hardware Version
		data = struct.pack(">B", inv.vhw)
		f.write(data)
		
		#Firmware Version
		data = struct.pack(">B", inv.vfw)
		f.write(data)
		
		#System Version
		data = struct.pack("16s", inv.vsystem)
		f.write(data)
		
		#Notes
		data = struct.pack("100s", inv.notas)
		f.write(data)
		
		#Resets
		data = struct.pack("H", inv.nresets)
		f.write(data)
		
		f.close()
		if sys.platform == "win32":
			os.system("ccrypt.exe -efK dp2a3r2mhb tftpboot/onuinv")
		else:
			os.system("ccrypt -efK dp2a3r2mhb tftpboot/onuinv")
			
	def stm1(self, ui):
		f = open('tftpboot/stm1inv','w')
		inv = inventory()
		inv.stm1(str(ui.LeSTM1Dproduto.text()), str(ui.LeSTM1Cprod.text()), 
			str(ui.LeSTM1Nserie.text()), str(ui.LeSTM1Data.text()), 
			str(ui.LeSTM1Npedido.text()), str(ui.LeSTM1Vhw.text()),
			str(ui.LeSTM1Vfw.text()), str(ui.LeSTM1Tec.text()), 
			str(ui.LeSTM1Resets.text()))
		
		#Description
		data = struct.pack("30s", inv.descricao)
		f.write(data)
		
		#Code of product
		data = struct.pack(">H", inv.codprod)
		f.write(data)
		
		#Serial Number
		data = struct.pack(">I", inv.snumber)
		f.write(data)
		
		#Manufactoring date
		data = struct.pack("11s", inv.dataf)
		f.write(data)
		
		#Order Number
		data = struct.pack(">H", inv.npedido)
		f.write(data)
		
		#Hardware Version
		data = struct.pack(">B", inv.vhw)
		f.write(data)
		
		#Firmware Version
		data = struct.pack(">B", inv.vfw)
		f.write(data)
		
		#Notes
		data = struct.pack("100s", inv.notas)
		f.write(data)
		
		#Resets
		data = struct.pack("H", inv.nresets)
		f.write(data)
		
		f.close()
		if sys.platform == "win32":
			os.system("ccrypt.exe -efK dp2a3r2mhbstm1 tftpboot/stm1inv")
		else:
			os.system("ccrypt -efK dp2a3r2mhbstm1 tftpboot/stm1inv")

	def oltblade(self, ui):
		f = open('tftpboot/oltbladeinv','w')
		inv = inventory()
		inv.oltBlade(str(ui.LeOltBladeMac.text()), str(ui.LeOltBladeDproduto.text()),
				str(ui.LeOltBladeCprod.text()), str(ui.LeOltBladeNserie.text()),
				str(ui.LeOltBladeData.text()), str(ui.LeOltBladeNpedido.text()),
				str(ui.LeOltBladeVhw.text()), str(ui.LeOltBladeVfw.text()), 
				str(ui.LeOltBladeSystem.text()), str(ui.LeOltBladeAsgos.text()), 
				str(ui.LeOltBladeStartup.text()), str(ui.LeOltBladeTec.text()),
				str(ui.LeOltBladeResets.text()))
		
		#Mac
		tmp = binascii.a2b_hex(inv.mac)
		data = struct.pack("6s", tmp)
		f.write(data)
		
		#Description
		data = struct.pack("30s", inv.descricao)
		f.write(data)
		
		#Code of product
		data = struct.pack(">H", inv.codprod)
		f.write(data)
		
		#Serial Number
		data = struct.pack(">I", inv.snumber)
		f.write(data)
		
		#Manufactoring date
		data = struct.pack("11s", inv.dataf)
		f.write(data)
		
		#Order Number
		data = struct.pack(">H", inv.npedido)
		f.write(data)
		
		#Hardware Version
		data = struct.pack(">B", inv.vhw)
		f.write(data)
		
		#Firmware Version
		data = struct.pack(">B", inv.vfw)
		f.write(data)
		
		#System Version
		data = struct.pack("16s", inv.vsystem)
		f.write(data)
		
		#Startup Version
		data = struct.pack("16s", inv.vstartup)
		f.write(data)
		
		#Asgos Version
		data = struct.pack("16s", inv.vasgos)
		f.write(data)
		
		#Notes
		data = struct.pack("100s", inv.notas)
		f.write(data)
		
		#Resets
		data = struct.pack("H", inv.nresets)
		f.write(data)
		
		f.close()
		
		if sys.platform == "win32":
			os.system("ccrypt.exe -efK dp2a3r2mhboltblade tftpboot/oltbladeinv")
		else:
			os.system("ccrypt -efK dp2a3r2mhboltblade tftpboot/oltbladeinv")

	def msdd(self, ui):
		f = open('tftpboot/msddinv','w')
		inv = inventory()
		inv.msdd(str(ui.LeMSDDMac.text()), str(ui.LeMSDDDproduto.text()),
				str(ui.LeMSDDCprod.text()), str(ui.LeMSDDNserie.text()),
				str(ui.LeMSDDNspon.text()), str(ui.LeMSDDData.text()), 
				str(ui.LeMSDDNpedido.text()), str(ui.LeMSDDVhw.text()),
				str(ui.LeMSDDVfw.text()), str(ui.LeMSDDSystem.text()),  
				str(ui.LeMSDDTec.text()), str(ui.LeMSDDResets.text()))
		
		#Mac
		tmp = binascii.a2b_hex(inv.mac)
		data = struct.pack("6s", tmp)
		f.write(data)
		
		#Description
		data = struct.pack("30s", inv.descricao)
		f.write(data)
		
		#Code of product
		data = struct.pack(">H", inv.codprod)
		f.write(data)
		
		#Serial Number
		data = struct.pack(">I", inv.snumber)
		f.write(data)
		
		#Pon Serial Number
		tmp = binascii.a2b_hex(inv.snpon)
		data = struct.pack("8s", tmp)
		f.write(data)
		
		
		#Manufactoring date
		data = struct.pack("11s", inv.dataf)
		f.write(data)
		
		#Order Number
		data = struct.pack(">H", inv.npedido)
		f.write(data)
		
		#Hardware Version
		data = struct.pack(">B", inv.vhw)
		f.write(data)
		
		#Firmware Version
		data = struct.pack(">B", inv.vfw)
		f.write(data)
		
		#System Version
		data = struct.pack("16s", inv.vsystem)
		f.write(data)
		
		#Notes
		data = struct.pack("100s", inv.notas)
		f.write(data)
		
		#Resets
		data = struct.pack("H", inv.nresets)
		f.write(data)
		
		f.close()
		if sys.platform == "win32":
			os.system("ccrypt.exe -efK dp2a3r2mhbmsdd tftpboot/msddinv")
		else:
			os.system("ccrypt -efK dp2a3r2mhbmsdd tftpboot/msddinv")
			
	def newonu(self, ui):
		f = open('tftpboot/onuinv','wb')
		inv = inventory()
		inv.newonu(str(ui.LeOnuMac.text()), str(ui.LeOnuDproduto.text()),
				str(ui.LeOnuCprod.text()), str(ui.LeOnuNserie.text()),
				str(ui.LeOnuNspon.text()), str(ui.LeOnuData.text()), 
				str(ui.LeOnuNpedido.text()), str(ui.LeOnuVhw.text()),
				str(ui.LeOnuVfw.text()), str(ui.LeOnuSystem.text()),  
				str(ui.LeOnuTec.text()), str(ui.LeOnuResets.text()),
				str(ui.LeOnuGtin.text()))
		
		#Mac
		tmp = binascii.a2b_hex(inv.mac)
		data = struct.pack("6s", tmp)
		f.write(data)
		
		#Description
		try:
			data = struct.pack("30s", inv.descricao)
		except:
			data = struct.pack("30s", inv.descricao.encode("ascii"))
		f.write(data)
		
		#Code of product
		data = struct.pack(">H", inv.codprod)
		f.write(data)
		
		#Serial Number
		data = struct.pack(">I", inv.snumber)
		f.write(data)
		
		#Pon Serial Number
		tmp = binascii.a2b_hex(inv.snpon)
		data = struct.pack("8s", tmp)
		f.write(data)
		
		
		#Manufactoring date
		try:
			data = struct.pack("11s", inv.dataf)
		except:
			data = struct.pack("11s", inv.dataf.encode("ascii"))
		f.write(data)
		
		#Order Number
		data = struct.pack(">H", inv.npedido)
		f.write(data)
		
		#Hardware Version
		data = struct.pack(">B", inv.vhw)
		f.write(data)
		
		#Firmware Version
		data = struct.pack(">B", inv.vfw)
		f.write(data)
		
		#System Version
		try:
			data = struct.pack("16s", inv.vsystem)
		except:
			data = struct.pack("16s", inv.vsystem.encode("ascii"))
		f.write(data)
		
		#Notes
		try:
			data = struct.pack("100s", inv.notas)
		except:
			data = struct.pack("100s", inv.notas.encode("ascii"))
		f.write(data)
		
		#Resets
		data = struct.pack("H", inv.nresets)
		f.write(data)
		
		#gtin
		try:
			data = struct.pack("21s", inv.newpcode)
		except:
			data = struct.pack("21s", inv.newpcode.encode("ascii"))
		f.write(data)
		
		f.close()
		if sys.platform == "win32":
			os.system("ccrypt.exe -efK dp2a3r2mhb tftpboot/onuinv")
		else:
			os.system("ccrypt -efK dp2a3r2mhb tftpboot/onuinv")

