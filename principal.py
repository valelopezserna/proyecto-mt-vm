# -- coding: utf-8 --
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from db import Run_query

# TODOS LOS 'print' SON SOLAMENTE PARA SEGUIMIENTO DE ALGUNAS FUNCIONES.


######################## VENTANA PRINCIPAL ###########################
class VentanaPrincipal(QMainWindow):
	def __init__(self):
		super(VentanaPrincipal, self).__init__()
		loadUi('principal.ui', self)

		self.lineEditPrinContra.setEchoMode(QtWidgets.QLineEdit.Password)

		self.btnPrinIniciarSesion.clicked.connect(self.InicioSesion)
		self.btnPrinRegistrate.clicked.connect(self.AbrirRegistrate)
		self.btnPrinAcercaDe.clicked.connect(self.AbrirAcercaDe)
		self.btnPrinSalir.clicked.connect(self.SalirPrincipal)

	# Métodos para abrir las correspondientes ventanas
	def AbrirServicios(self):
		vent_serv = VentanaServicios(self)
		vent_serv.show()

	def AbrirRegistrate(self):
		registrate = VentanaRegistrate(self)
		registrate.show()

	def AbrirAcercaDe(self):
		vent_acerca_de = VentanaAcercaDe(self)
		vent_acerca_de.show()

	# Método para cerrar la ventana desde la cruz del margen superior derecho
	def closeEvent(self, event):
		reply = QMessageBox.question(self,'SALIR', "Realmente desea cerrar la aplicacion",QMessageBox.Ok | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Ok:
			event.accept()
		else:
			event.ignore()

	# Creo un objeto QMessageBox que sería una caja para mostrar un mensaje y realizar una acción "Salir"
	def SalirPrincipal(self):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setText("Seguro que desea salir?")
		msgBox.setWindowTitle("Salir")
		msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		returnValue = msgBox.exec_()
		if returnValue == QMessageBox.Ok:
			app.quit()
			#self.parent().show()
			#self.close()
		else:
			print('Cancel')

	# Método paracido al anterior pero personalizado
	def messagebox(self, title, message):
		mess = QtWidgets.QMessageBox()
		mess.resize(400,280)
		mess.setIcon(QMessageBox.Information)
		mess.setWindowTitle(title)
		mess.setText(message)
		mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
		mess.exec_()

	# Tecla Enter
	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Return:
			self.InicioSesion()

	def InicioSesion(self):
		usuario = self.lineEditPrinUsuario.text()
		contrasenia = self.lineEditPrinContra.text()

		query_user = "SELECT usuario FROM usuarios WHERE usuario='%s'" %usuario
		try:	
			user = Run_query(query_user)
			user = str(user).split("'")
			user = user[1]

			if usuario == user:
				query_pass = "SELECT contrasenia FROM usuarios WHERE usuario='%s'" %usuario
				passw = Run_query(query_pass)
				passw = str(passw).split("'")
				passw = passw[1]
				print("El usuario existe")
				
				if contrasenia == passw:
					self.AbrirServicios()
					self.lineEditPrinUsuario.clear()
					self.lineEditPrinContra.clear()
					print("Contraseña correcta")
				else:
					self.messagebox("ERROR", "Contraseña incorrecta")
					self.lineEditPrinContra.clear()
					print("Contraseña incorrecta")
		except:
			self.messagebox("ERROR", "No existe el usuario")
			self.lineEditPrinUsuario.clear()
			print("No existe el usuario")


######################## VENTANA INICIAR SESION ###########################
class VentanaServicios(QMainWindow):
	def __init__(self, parent=None):
		super(VentanaServicios, self).__init__(parent)
		loadUi('servicios.ui', self)

		self.btnAranjuez.clicked.connect(self.Aranjuez)
		self.btnCastilla.clicked.connect(self.Castilla)
		self.btnBello.clicked.connect(self.Bello)
		self.btnSanJavier.clicked.connect(self.SanJavier)
		self.btnItagui.clicked.connect(self.Itagui)
		self.btnSabaneta.clicked.connect(self.Sabaneta)
		self.btnEstrella.clicked.connect(self.Estrella)
		self.btnEnvigado.clicked.connect(self.Envigado)
		self.btnServCerrar.clicked.connect(self.CerrarServicios)

	def CerrarServicios(self):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setText("Seguro que desea salir?")
		msgBox.setWindowTitle("Salir")
		msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		returnValue = msgBox.exec_()
		if returnValue == QMessageBox.Ok:
			self.parent().show()
			self.close()
		else:
			print('Cancel')

	def Aranjuez(self):		
		barrio = "Aranjuez"
		negocio = self.comboBoxNegocio.currentText()
		aviso = self.comboBoxAviso.currentText()

		if negocio == "Alquiler":            #ALQUILER
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))						
				print("ALQUILER APART")

			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER FINCAS")
			
		else:                   #VENTA
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print(" VENTA APART")
			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA LOTES")
			else:  #VENTA
				query_finca = "SELECT fincas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA FINCAS")
				  

	def Castilla(self):
		barrio = "Castilla"
		negocio = self.comboBoxNegocio.currentText()
		aviso = self.comboBoxAviso.currentText()

		if negocio == "Alquiler":     #ALQUILER
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))						
				print("ALQUILER APART")

			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER FINCAS")
			
		else:      #VENTA
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA APART")
			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA FINCAS")
				  

	def Bello(self):
		barrio = "Bello"
		negocio = self.comboBoxNegocio.currentText()
		aviso = self.comboBoxAviso.currentText()

		if negocio == "Alquiler":     #ALQUILER
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))						
				print("ALQUILER APART")

			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER FINCAS")
			
		else:      #VENTA
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA APART")
			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA FINCAS")
				  
		
	def SanJavier(self):
		barrio = "San Javier"
		negocio = self.comboBoxNegocio.currentText()
		aviso = self.comboBoxAviso.currentText()

		if negocio == "Alquiler":     #ALQUILER
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))						
				print("ALQUILER APART")

			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER FINCAS")
			
		else:      #VENTA
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA APART")
			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA FINCAS")
		

	def Itagui(self):
		barrio = "Itagui"
		negocio = self.comboBoxNegocio.currentText()
		aviso = self.comboBoxAviso.currentText()

		if negocio == "Alquiler":     #ALQUILER
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))						
				print("ALQUILER APART")

			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER FINCAS")
			
		else:      #VENTA
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA APART")
			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA FINCAS")


	def Sabaneta(self):
		barrio = "Sabaneta"
		negocio = self.comboBoxNegocio.currentText()
		aviso = self.comboBoxAviso.currentText()

		if negocio == "Alquiler":     #ALQUILER
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))						
				print("ALQUILER APART")

			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER FINCAS")
			
		else:      #VENTA
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA APART")
			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA FINCAS")


	def Estrella(self):
		barrio = "Estrella"
		negocio = self.comboBoxNegocio.currentText()
		aviso = self.comboBoxAviso.currentText()

		if negocio == "Alquiler":     #ALQUILER
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))						
				print("ALQUILER APART")

			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER FINCAS")
			
		else:      #VENTA
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA APART")
			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA FINCAS")


	def Envigado(self):
		barrio = "Envigado"
		negocio = self.comboBoxNegocio.currentText()
		aviso = self.comboBoxAviso.currentText()

		if negocio == "Alquiler":     #ALQUILER
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))						
				print("ALQUILER APART")

			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM alquiler WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("ALQUILER FINCAS")
			
		else:      #VENTA
			if aviso == "Apartamentos":
				query_apart = "SELECT apartamento,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_apart)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA APART")
			elif aviso == "Casas":
				query_casa = "SELECT casas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_casa)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA CASAS")

			elif aviso == "Lotes":
				query_lote = "SELECT lotes,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_lote)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA LOTES")
			else:
				query_finca = "SELECT fincas,zona,barrio,contacto FROM venta WHERE barrio='%s'" %barrio
				resul = Run_query(query_finca)

				self.tableWidgetServicios.setRowCount(0)

				for fila_num, fila_dato in enumerate(resul):
					self.tableWidgetServicios.insertRow(fila_num)
					for colum_num, dato in enumerate(fila_dato):
						self.tableWidgetServicios.setItem(fila_num, colum_num, QtWidgets.QTableWidgetItem(str(dato)))
				print("VENTA FINCAS")

		

######################## VENTANA REGISTRATE ###########################
class VentanaRegistrate(QMainWindow):
	def __init__(self, parent=None):
		super(VentanaRegistrate, self).__init__(parent)
		loadUi('registrate.ui', self)

		self.lineEditCedula.setValidator(QtGui.QDoubleValidator()) #Valida sólo números.

		self.btnRegGuardar.clicked.connect(self.InsertarDatosUsuario)
		self.btnRegCerrar.clicked.connect(self.CerrarRegistrate)
		self.btnRegContinuar.clicked.connect(self.AbrirVentanaPrincipal)

	def AbrirVentanaPrincipal(self):
		self.close()		
		self.parent().show()

	def CerrarRegistrate(self):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setText("Seguro que desea salir?")
		msgBox.setWindowTitle("Salir")
		msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		returnValue = msgBox.exec_()
		if returnValue == QMessageBox.Ok:
			self.parent().show()
			self.close()
		else:
			print('Cancel')

	def InsertarDatosUsuario(self):
		nombre = self.lineEditNombreCompleto.text()
		DNI = self.lineEditCedula.text()
		direccion = self.lineEditDireccion.text()
		email = self.lineEditEmail.text()
		usuario = self.lineEditRegUsuario.text()
		contrasenia = self.lineEditRegContra.text()

		query_reg = ("INSERT INTO usuarios(nombre, DNI, direccion, email, usuario, contrasenia) VALUES ('%s','%s','%s','%s','%s','%s')" %(''.join(nombre),
					''.join(DNI),''.join(direccion),''.join(email),''.join(usuario),''.join(contrasenia)))

		Run_query(query_reg)
		if(query_reg):
			VentanaPrincipal.messagebox(self, "Bien!!!", "ALTA EXITOSA!")
			self.lineEditNombreCompleto.clear()
			self.lineEditCedula.clear()
			self.lineEditDireccion.clear()
			self.lineEditEmail.clear()
			self.lineEditRegUsuario.clear()
			self.lineEditRegContra.clear()  #Limpia los campos
			print("Datos guardados!")


######################## VENTANA ACERCA DE ###########################
class VentanaAcercaDe(QMainWindow):
	def __init__(self, parent=None):
		super(VentanaAcercaDe, self).__init__(parent)
		loadUi('acercade.ui', self)

		self.btnAcerCerrar.clicked.connect(self.AbrirVentanaPrincipal)

	def AbrirVentanaPrincipal(self):
		self.close()		
		self.parent().show()




	

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())