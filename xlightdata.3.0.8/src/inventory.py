# -*- coding: utf-8 -*-

import binascii
import struct
import subprocess
from os import path

#Defining the class for olt inventory	
class inventory(object):
	def __init__(self):
		self.mac = '0'*12
		self.descricao = '\0'*30
		self.codprod = int(0)
		self.snumber = int(0)
		self.dataf = '\0'*11
		self.npedido = int(0)
		self.vhw = int(0)
		self.vfw = int(0)
		self.vsystem = '\0'*16
		self.vasgos = '\0'*16
		self.vstartup = '\0'*16
		self.notas = '\0'*100
		self.nresets = int(0)
		self.snpon = "46524b5700000000"
		self.newpcode ='\0'*21
	
	#Defining the class for olt inventory	
	def olt(self, mac, descricao, codprod, snumber, dataf, npedido, 
			vhw, vfw, vsystem, vasgos, vstartup, notas, nresets):
		if mac != None and mac.__len__() != 0:
			self.mac = mac[0:12]
			
		if descricao != None and descricao.__len__() != 0:
			self.descricao = descricao[0:30]
			
		if codprod != None and codprod.__len__() != 0:
			self.codprod = int(codprod)
			
		if snumber != None and snumber.__len__() != 0:
			self.snumber = int(snumber)
		
		if dataf != None and dataf.__len__() != 0:
			self.dataf = dataf
		
		if npedido != None and npedido.__len__() != 0:
			self.npedido = int(npedido)
		
		if vhw != None and vhw.__len__() != 0:
			self.vhw = int(vhw)
			
		if vfw != None and vfw.__len__() != 0:
			self.vfw = int(vfw)
		
		if vsystem != None and vsystem.__len__() != 0:
			self.vsystem = vsystem
			
		if vasgos != None and vasgos.__len__() != 0:	
			self.vasgos = vasgos
		
		if vstartup != None and vstartup.__len__() != 0:
			self.vstartup = vstartup
			
		if notas != None and notas.__len__() != 0:
			self.notas = notas[0:100]
			
		if nresets != None and nresets.__len__() != 0:
			self.nresets = int(nresets)
						
	#Defining the class for onu inventory
	def onu(self, mac, descricao, codprod, snumber, snpon, dataf, npedido, 
			vhw, vfw, vsystem, notas, nresets):
		if mac != None and mac.__len__() != 0:
			self.mac = mac[0:12]
			
		if descricao != None and descricao.__len__() != 0:
			self.descricao = descricao[0:30]
			
		if codprod != None and codprod.__len__() != 0:
			self.codprod = int(codprod)
			
		if snumber != None and snumber.__len__() != 0:
			self.snumber = int(snumber)
			
		if snpon != None and snpon.__len__() != 0:
			self.snpon = snpon[0:16]
		
		if dataf != None and dataf.__len__() != 0:
			self.dataf = dataf
		
		if npedido != None and npedido.__len__() != 0:
			self.npedido = int(npedido)
		
		if vhw != None and vhw.__len__() != 0:
			self.vhw = int(vhw)
			
		if vfw != None and vfw.__len__() != 0:
			'''FIXME: colocar códigos corretos [00033 -> ONU582]'''
			if (codprod == '61392' or codprod == '00033'):
				if vfw == 'L3 Full':
					vfw = 2;
				elif vfw == 'L3 Lite':
					vfw = 1;
				else:
					vfw = 0
			self.vfw = int(vfw)
		
		if vsystem != None and vsystem.__len__() != 0:
			self.vsystem = vstartup
			
		if notas != None and notas.__len__() != 0:
			self.notas = notas[0:100]
			
		if nresets != None and nresets.__len__() != 0:
			self.nresets = int(nresets)	
	
	#Defining the class for stm1 inventory	
	def stm1(self, descricao, codprod, snumber, dataf, npedido, 
			vhw, vfw, notas, nresets):

		if descricao != None and descricao.__len__() != 0:
			self.descricao = descricao[0:30]
			
		if codprod != None and codprod.__len__() != 0:
			self.codprod = int(codprod)
			
		if snumber != None and snumber.__len__() != 0:
			self.snumber = int(snumber)
			
		if dataf != None and dataf.__len__() != 0:
			self.dataf = dataf
		
		if npedido != None and npedido.__len__() != 0:
			self.npedido = int(npedido)
		
		if vhw != None and vhw.__len__() != 0:
			self.vhw = int(vhw)
			
		if vfw != None and vfw.__len__() != 0:
			self.vfw = int(vfw)
			
		if notas != None and notas.__len__() != 0:
			self.notas = notas[0:100]
			
		if nresets != None and nresets.__len__() != 0:
			self.nresets = int(nresets)
	
	#Defining the class for oltBlade inventory		
	def oltBlade(self, mac, descricao, codprod, snumber, dataf, npedido, 
			vhw, vfw, vsystem, vasgos, vstartup, notas, nresets):
		if mac != None and mac.__len__() != 0:
			self.mac = mac[0:12]
			
		if descricao != None and descricao.__len__() != 0:
			self.descricao = descricao[0:30]
			
		if codprod != None and codprod.__len__() != 0:
			self.codprod = int(codprod)
			
		if snumber != None and snumber.__len__() != 0:
			self.snumber = int(snumber)
		
		if dataf != None and dataf.__len__() != 0:
			self.dataf = dataf
		
		if npedido != None and npedido.__len__() != 0:
			self.npedido = int(npedido)
		
		if vhw != None and vhw.__len__() != 0:
			self.vhw = int(vhw)
			
		if vfw != None and vfw.__len__() != 0:
			self.vfw = int(vfw)
		
		if vsystem != None and vsystem.__len__() != 0:
			self.vsystem = vsystem
			
		if vasgos != None and vasgos.__len__() != 0:	
			self.vasgos = vasgos
		
		if vstartup != None and vstartup.__len__() != 0:
			self.vstartup = vstartup
			
		if notas != None and notas.__len__() != 0:
			self.notas = notas[0:100]
			
		if nresets != None and nresets.__len__() != 0:
			self.nresets = int(nresets)		
			
	#Defining the class for MSDD inventory
	def msdd(self, mac, descricao, codprod, snumber, snpon, dataf, npedido, 
			vhw, vfw, vsystem, notas, nresets):
		if mac != None and mac.__len__() != 0:
			self.mac = mac[0:12]
			
		if descricao != None and descricao.__len__() != 0:
			self.descricao = descricao[0:30]
			
		if codprod != None and codprod.__len__() != 0:
			self.codprod = int(codprod)
			
		if snumber != None and snumber.__len__() != 0:
			self.snumber = int(snumber)
			
		if snpon != None and snpon.__len__() != 0:
			self.snpon = snpon[0:16]
		
		if dataf != None and dataf.__len__() != 0:
			self.dataf = dataf
		
		if npedido != None and npedido.__len__() != 0:
			self.npedido = int(npedido)
		
		if vhw != None and vhw.__len__() != 0:
			self.vhw = int(vhw)
			
		if vfw != None and vfw.__len__() != 0:
			self.vfw = int(vfw)
		
		if vsystem != None and vsystem.__len__() != 0:
			self.vsystem = vstartup
			
		if notas != None and notas.__len__() != 0:
			self.notas = notas[0:100]
			
		if nresets != None and nresets.__len__() != 0:
			self.nresets = int(nresets)	
			
		#Defining the class for newonu inventory
	def newonu(self, mac, descricao, codprod, snumber, snpon, dataf, npedido, 
			vhw, vfw, vsystem, notas, nresets,newpcode):
		if mac != None and mac.__len__() != 0:
			self.mac = mac[0:12]
			
		if descricao != None and descricao.__len__() != 0:
			self.descricao = descricao[0:30]
			
		if codprod != None and codprod.__len__() != 0:
			self.codprod = int(codprod)
			
		if snumber != None and snumber.__len__() != 0:
			self.snumber = int(snumber)
			
		if snpon != None and snpon.__len__() != 0:
			self.snpon = snpon[0:16]
		
		if dataf != None and dataf.__len__() != 0:
			self.dataf = dataf
		
		if npedido != None and npedido.__len__() != 0:
			self.npedido = int(npedido)
		
		if vhw != None and vhw.__len__() != 0:
			self.vhw = int(vhw)
			
		if vfw != None and vfw.__len__() != 0:
			self.vfw = int(vfw)
		
		if vsystem != None and vsystem.__len__() != 0:
			self.vsystem = vstartup
			
		if notas != None and notas.__len__() != 0:
			self.notas = notas[0:100]
			
		if nresets != None and nresets.__len__() != 0:
			self.nresets = int(nresets)	
			
		if newpcode != None and newpcode.__len__() != 0:
			self.newpcode = newpcode[0:21]

	#Defining the class for oltBlade inventory		
	def oltMaple(self, mac, codprod, snumber, dataf):
		if mac != None and mac.__len__() != 0:
			self.mac = mac[0:12]
			
		if codprod != None and codprod.__len__() != 0:
			self.codprod = int(codprod)
			
		if snumber != None and snumber.__len__() != 0:
			self.snumber = int(snumber)
		
		if dataf != None and dataf.__len__() != 0:
			self.dataf = dataf