from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import conexion


# Funciones para la accion de los botones 
def agregar():
    if validacion():
        return False
    print("Hola agregar")
    nombre=ventana.txtNombre.text()
    correo=ventana.txtCorreo.text()
    print(nombre, correo)

    objContactos=conexion.contactos()
    Contactos=objContactos.crearContacto((nombre, correo))
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
    print(nombre, correo)

    objContactos=conexion.contactos()
    Contactos=objContactos.modificarContacto((nombre, correo, id))
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
        indicecontrol+=1
    
    ventana.txtID.setText("")
    ventana.txtNombre.setText("")
    ventana.txtCorreo.setText("")
    
    ventana.btnAgregar.setEnabled(True)
    ventana.btnEliminar.setEnabled(False)
    ventana.btnModificar.setEnabled(False)
    ventana.btnCancelar.setEnabled(False)

# Selecciona la fila a la que el usuario le dio click 
def seleccionar():
    id=ventana.tblContactos.selectedIndexes()[0].data()
    nombre=ventana.tblContactos.selectedIndexes()[1].data()
    correo=ventana.tblContactos.selectedIndexes()[2].data()
    print(id, nombre, correo)
    ventana.txtID.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtCorreo.setText(correo)

    ventana.btnAgregar.setEnabled(False)
    ventana.btnEliminar.setEnabled(True)
    ventana.btnModificar.setEnabled(True)
    ventana.btnCancelar.setEnabled(True)

def validacion():
    if ventana.txtNombre.text()=="" or ventana.txtCorreo.text()=="":
        alerta=QMessageBox()
        alerta.setText("Debes de llenar los campos")
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        return True

aplicacion = QtWidgets.QApplication([]) #instancia de la aplicacion
ventana = uic.loadUi("Ventana.ui") #cargar la interfaz grafica 
ventana.show() # mostrar la ventana 

consultar()

 #Se modifica la cabecera de la tabla
ventana.tblContactos.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo'])
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