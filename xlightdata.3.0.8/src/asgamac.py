# -*- coding: utf-8 -*-

# Implementation for comunication with AsGa Mac Server
# Created: Wed Jul 25 10:11:19 2012
# By AluÃ­sio Leonello Victal


try:
	import kinterbasdb as k; k.init(type_conv=200)
except:
	import fdb as k; k
	
import psycopg2 as p
import psycopg2.extras
import binascii

class MAC(object):
	def mac_base(self, isFurukawa):
			if isFurukawa == 1: 
				return 0xB826D4700000
			else:
				return 0x14FA000000

	def insertEAN(self, ean, ProdCode, isFurukawa, Gtin):
		sql_asga = "insert into mac (mac_codbarra,mac_switch) values ('"+ str(ean) +"','"+ str(ean) +"')"
		sql2_asga = "insert into mac (mac_switch) values ('"+ str(ean) +"')"
		sql_fio = "insert into macfio (mac_codbarra,mac_switch) values ('"+ str(ean) +"','"+ str(ean) +"')"
		sql2_fio = "insert into macfio (mac_switch) values ('"+ str(ean) +"')"
		
		
		#  name          					PCode
		# ONU 500 - Fitec 					18094
		# ONU 500 PC 	 					27772
		# ONU 500 APC	 					56254
		# ONU 500S APC	 					55982
		# ONU 500S PC	 					58938
		# ONU 500V	 						56109
		# ONU 1600 PC	 					55980 7899936802757
		# ONU 1600 APC	 					57107
		# ONU LD 582 L2+L3 Lite+ L3 Full 	61392 7899936802733 7899936802740
		# ONU LD 1180						62441
		# ONU LD 1182						62439
		# ONU LD 1182-W						61728
		# ONU LD 1182-V						62445
		# ONU LD 1182-Y						62620
		# ONU LD 1182-WV					62448
		# ONU LD 1182-WY					62450
		# ONU LD 111				    	7899936800050 7899936802665
		# ONU LD industrial					7899936002782 7899936006063
		# ONU LD POE Industrial LW510-40RP  PCBA 7899936006865 Produto 7899936006971
		#									7893137299699 Turnkey
		# ONU LD POE WM	  LW110-20BP  PCBA 	7899936000610 Produto 7899936000610
		# 									7893137299699
		#----------------------------------------
		# OLT 2502 	 26676 7899936802597 7899936802603 7899936802627
		# OLT 2504 	 26677 7899936802771
		# OLT FIT  	 61952 7899936802610
		# OLT BLADE  		(Fictício)		00011
		# MSDD		  		(Fictício)		00022
		# ONU LD 581 L2+L3 	(Fictício)		00033
		# OLT MAPLE 3516 		            7899936006131
		# OLT MAPLE 3508 		           	7893137283605
		'''FIXME: corrigir códigos de produto'''
		
		
		if (ProdCode == '26676' or ProdCode == '26677' or ProdCode == '61952'
			or ProdCode == '80259' or ProdCode == '80260' or ProdCode == '80262'
			or ProdCode == '80277' or ProdCode == '80261' or Gtin == '7899936006131'
			or Gtin == '7893137283605'):
			n_macs = 20
		elif (ProdCode == '18094' or ProdCode == '27772' or ProdCode == '56254'
			or ProdCode == '55982' or ProdCode == '58938' or ProdCode == '56109'
			or ProdCode == '00033'):
			n_macs = 4
		elif (ProdCode == '55980' or ProdCode == '57107' or ProdCode == '80275'):
			n_macs = 8
		elif ( ProdCode == '62441' or ProdCode == '62439' or ProdCode == '61728' 
			or ProdCode == '62445' or ProdCode == '62620' or ProdCode == '62448' 
			or ProdCode == '62450' or ProdCode == '00022'):
			n_macs = 8
		elif (ProdCode == '61392' or ProdCode == '80273' or ProdCode == '80274'):
			n_macs = 5
		elif ( Gtin == '7899936800050' or Gtin == '7899936002782'
			 or Gtin == '7899936802665' or Gtin == '7899936006063'
			 or Gtin == '7899936006865' or Gtin == '7899936000610'):
			n_macs = 8
		else:
			return None
		
		try:
			#con = k.connect(dsn='10.0.0.4:e:\\basefb\\baixateste.gdb', user='sysdba', password='masterkey',timeout={'period': 3.0})
			con = k.connect(dsn=r'10.41.122.204:e:\\basefb\\baixa.gdb', user='sysdba', password='masterkey',timeout={'period': 3.0})
			cur = con.cursor()
			if isFurukawa == 1:
				cur.execute(sql_fio)
			else:
				cur.execute(sql_asga)
			con.commit()
			
			i = 1
			while i < n_macs:
				if isFurukawa == 1:
					cur.execute(sql2_fio)
				else:
					cur.execute(sql2_asga)
				con.commit()
				i = i + 1
			
			con.close()
		except:
			return None
		
		
	def getMAC(self, ean, isFurukawa):
		sql_asga = "Select * From mac where mac_codbarra = '"+ str(ean) + "'"
		sql_fio = "Select * From macfio where mac_codbarra = '"+ str(ean) + "'"
		
		try: 
			#con = k.connect(dsn='10.0.0.4:e:\\basefb\\baixateste.gdb', user='sysdba', password='masterkey',timeout={'period': 3.0})
			con = k.connect(dsn='10.41.122.204:e:\\basefb\\baixa.gdb', user='sysdba', password='masterkey',timeout={'period': 3.0})
			cur = con.cursor()
			if isFurukawa == 1:
				cur.execute(sql_fio)
			else:
				cur.execute(sql_asga)
				
			tupple = cur.fetchone()
			
			if tupple != None:
				# Python 2 vs Python 3
				try:
					mac = long(self.mac_base(isFurukawa)) + long(tupple[0])	
				except:
					mac = int(self.mac_base(isFurukawa)) + int(tupple[0])	
			else:
				con.close()
				return None
				
			con.close()
			if isFurukawa == 1:
				return str(hex(mac).rstrip("L").lstrip("0x"))
			else:
				return str(hex(mac).rstrip("L").lstrip("0x"))
		except:
			return None
# 			return str(hex(self.mac_base(isFurukawa)).rstrip("L").lstrip("0x"))
		#finally:
		#	con.close()
		#	return None
		
	def verify_asgaDb(self):
		try: 
#			con = k.connect(dsn='10.0.0.4:e:\\basefb\\baixateste.gdb', user='sysdba', password='masterkey',timeout={'period': 3.0})
			con = k.connect(dsn='10.41.122.204:e:\\basefb\\baixa.gdb', user='sysdba', password='masterkey',timeout={'period': 3.0})

			con.close()
			return '1'
		except:
			return str('Base de Dados AsGa')
	
	def verify_chronosDb(self):
		try:
			con = p.connect(database="cmdata", user="postgres", password="pk6HHmg40", host="10.41.122.205", port="5432")
			con.close()
			return '1'
		except:
			return str('Base de Dados Chronos') 
		
	def insertEAN_chronos(self, ean, layer):
		sql = "insert into LAYER_ONU (serial_number,layer) values ('"+ str(ean) +"','"+str(layer)+"')"
		try:
			con = p.connect(database="cmdata", user="postgres", password="pk6HHmg40", host="10.41.122.205", port="5432")
# 			con = f.connect(dsn='localhost:/home/pedro/Projetos/opt/database/chronos.gdb', user='sysdba', password='masterkey')
			cur = con.cursor()
			cur.execute(sql)
			con.commit()
			con.close()
		except:
			return None;
	
	# get firmware value from chronos, and simultaneusly verify if already exists an entry with the passed EAN;
	def getFirmware_chronos(self, ean):
		sql = "Select * From layer_onu where serial_number = '"+ str(ean) + "'"
		
		try: 
			con = p.connect(database="cmdata", user="postgres", password="pk6HHmg40", host="10.41.122.205", port="5432")
# 			con = f.connect(dsn='localhost:/home/pedro/Projetos/opt/database/chronos.gdb', user='sysdba', password='masterkey')
			cur = con.cursor()
			cur.execute(sql)
			tupple = cur.fetchone()
			
			if tupple != None:
				firm =int(tupple[1])
			else:
				con.close()
				return None
				
			con.close()
			return str(firm)
		except:
			return None
		
		
	def catchMAC(self, ean, ProdCode, isFurukawa, Gtin):
		mac = self.getMAC(ean, isFurukawa)
		return mac
			
