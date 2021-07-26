from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import conexion
import re



# Funciones para la accion de los botones 
def agregar():
    if validacion():
        return False
    print("Hola agregar")
    nombre=ventana.txtNombre.text()
    correo=ventana.txtCorreo.text()
    direccion=ventana.txtDireccion.text()
    telefono=ventana.txtTelefono.text()
    print(nombre, correo, direccion, telefono)

    objContactos=conexion.contactos()
    Contactos=objContactos.crearContacto((nombre, correo, direccion, telefono))
    consultar()

def eliminar():
    print("Hola eliminar")
    id=ventana.txtID.text()
    objContactos=conexion.contactos()
    Contactos=objContactos.borrarContacto(id) 
    consultar() 

def modificar():
    print("Hola modificar")
    id=ventana.txtID.text()
    nombre=ventana.txtNombre.text()
    correo=ventana.txtCorreo.text()
    direccion=ventana.txtDireccion.text()
    telefono=ventana.txtTelefono.text()
    print(nombre, correo, direccion, telefono)

    objContactos=conexion.contactos()
    Contactos=objContactos.modificarContacto((nombre, correo, direccion, telefono, id))
    consultar()

def cancelar():
    print("Hola cancelar")
    consultar()

# Buscar registros con el metodo leerContactos, llena y actualiza  los registros de la tabla 
def consultar(): 
    ventana.tblContactos.setRowCount(0)
    indicecontrol=0

    objContactos=conexion.contactos()
    Contactos=objContactos.leerContactos()

    for contacto in Contactos:
        ventana.tblContactos.setRowCount(indicecontrol+1)
        ventana.tblContactos.setItem(indicecontrol, 0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indicecontrol, 1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indicecontrol, 2, QTableWidgetItem(str(contacto[2])))
        ventana.tblContactos.setItem(indicecontrol, 3, QTableWidgetItem(str(contacto[3])))
        ventana.tblContactos.setItem(indicecontrol, 4, QTableWidgetItem(str(contacto[4])))
        
        indicecontrol+=1
    
    ventana.txtID.setText("")
    ventana.txtNombre.setText("")
    ventana.txtCorreo.setText("")
    ventana.txtDireccion.setText("")
    ventana.txtTelefono.setText("")
    
    ventana.btnAgregar.setEnabled(True)
    ventana.btnEliminar.setEnabled(False)
    ventana.btnModificar.setEnabled(False)
    ventana.btnCancelar.setEnabled(False)

# Selecciona la fila a la que el usuario le dio click 
def seleccionar():
    id=ventana.tblContactos.selectedIndexes()[0].data()
    nombre=ventana.tblContactos.selectedIndexes()[1].data()
    correo=ventana.tblContactos.selectedIndexes()[2].data()
    direccion=ventana.tblContactos.selectedIndexes()[3].data()
    telefono=ventana.tblContactos.selectedIndexes()[4].data()
    print(id, nombre, correo, direccion, telefono)
    ventana.txtID.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtCorreo.setText(correo)
    ventana.txtDireccion.setText(direccion)
    ventana.txtTelefono.setText(telefono)

    ventana.btnAgregar.setEnabled(False)
    ventana.btnEliminar.setEnabled(True)
    ventana.btnModificar.setEnabled(True)
    ventana.btnCancelar.setEnabled(True)

def validacion():
    #Expresiones regulares para la validacion en el ingreso de los datos
    validarNombre=re.match('^[a-zA-Z\sáéíóúñ]+$', ventana.txtNombre.text())
    validarCorreo=re.match('^[a-zA-Z0-9.!#$%&*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', ventana.txtCorreo.text())
    validarTelefono=re.match('^[0-9]+$', ventana.txtTelefono.text())
    
    #validacion para que todos los campos sean llenados
    if ventana.txtNombre.text()=="" or ventana.txtCorreo.text()=="" or ventana.txtDireccion.text()=="" or ventana.txtTelefono.text()=="":
        alerta=QMessageBox()
        alerta.setText("Debes de llenar todos los campos")
        alerta.setIcon(QMessageBox.Information)
        alerta.setWindowTitle("Alerta")
        alerta.exec()
        return True
    #Validar que el nombre se ingrese correctamente
    elif not validarNombre:
        #Pintar el borde de la qlineedit de rojo y amarillo
        ventana.txtNombre.setStyleSheet("border: 5px solid red;")
        ventana.txtNombre.setStyleSheet("background-color: yellow")
        #Mensaje de alerta
        alerta=QMessageBox()
        alerta.setText("El campo nombre solo debe tener caracteres de a-z ")
        alerta.setIcon(QMessageBox.Information)
        alerta.setWindowTitle("Alerta")
        alerta.exec()
        return True
    #Validar formato del correo
    elif not validarCorreo:
        ventana.txtCorreo.setStyleSheet("border: 5px solid red;")
        ventana.txtCorreo.setStyleSheet("background-color: yellow")
        alerta=QMessageBox()
        alerta.setText("Ingrese un formato de correo valido")
        alerta.setIcon(QMessageBox.Information)
        alerta.setWindowTitle("Alerta")
        alerta.exec()
        return True
    #Validar que en el campo telefono solo se ingresen numeros
    elif not validarTelefono:
        ventana.txtTelefono.setStyleSheet("border: 5px solid red;")
        ventana.txtTelefono.setStyleSheet("background-color: yellow")
        alerta=QMessageBox()
        alerta.setText("En el campo de telefono solo puede ingresar numeros")
        alerta.setIcon(QMessageBox.Information)
        alerta.setWindowTitle("Alerta")
        alerta.exec()
        return True
    #Despintar los qlineedite cuando se ingrese correctamente el dato
    else:
        #Nombre
        ventana.txtNombre.setStyleSheet("border: 1px solid black;")
        ventana.txtNombre.setStyleSheet("background-color: white")
        #Correo
        ventana.txtCorreo.setStyleSheet("border: 1px solid black;")
        ventana.txtCorreo.setStyleSheet("background-color: white")
        #Telefono
        ventana.txtTelefono.setStyleSheet("border: 1px solid black;")
        ventana.txtTelefono.setStyleSheet("background-color: white")
        return False
    
aplicacion = QtWidgets.QApplication([]) #instancia de la aplicacion
ventana = uic.loadUi("Ventana.ui") #cargar la interfaz grafica 
ventana.show() # mostrar la ventana 
consultar()

 #Se modifica la cabecera de la tabla
ventana.tblContactos.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo', 'Direccion', 'Telefono'])

#Se bloquea la primera fila al usuario
ventana.tblContactos.setEditTriggers(QTableWidget.NoEditTriggers)

#Se resalta la fila seleccionada
ventana.tblContactos.setSelectionBehavior(QTableWidget.SelectRows)
ventana.tblContactos.cellClicked.connect(seleccionar)

#Configuracion de botones para conectar con la base de datos
ventana.btnAgregar.clicked.connect(agregar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec()) #Cerramos la aplicacion 