import sqlite3 
from sqlite3.dbapi2 import connect

# Clase para conectar con la base de datos 
class contactos:
    def iniciarConexion(self):
        # Hacemos la conexion
        conexion=sqlite3.connect('sistema.s3db')
        # Le decimos que los caracteres extraños que marquen errores los ignore
        conexion.text_factory=lambda b: b.decode(errors='ignore')
        return conexion

    def leerContactos(self):
        conexion=self.iniciarConexion()
        #Creamos un cursor que seleccione y ejecute una la accion e imprimir los datos
        cursor=conexion.cursor()
        sentencialSQL="SELECT * FROM contactos"
        cursor.execute(sentencialSQL)
        return cursor.fetchall() 
    
    # Funcion crear contactosresive los valores, se conecta a la base de datos inserta 
    # en la tabla contactos el nombre y el correo y cerrara la conexion con la base de datosContacto
    def crearContacto(self, datosContacto):
        conexion=self.iniciarConexion()
        cursor=conexion.cursor()
        sentencialSQL="INSERT INTO contactos(Nombre,Correo, Direccion, Telefono) VALUES(?, ?, ?, ?)"
        cursor.execute(sentencialSQL, datosContacto)
        conexion.commit() # Da como ejecutado 
        conexion.close()

    def borrarContacto(self, idContacto):
        conexion=self.iniciarConexion()
        cursor=conexion.cursor()
        sentencialSQL="DELETE FROM  contactos WHERE id=(?)"
        cursor.execute(sentencialSQL, [idContacto])
        conexion.commit() # Da como ejecutado 
        conexion.close()

    def modificarContacto(self, datosContacto):
        conexion=self.iniciarConexion()
        cursor=conexion.cursor()
        sentencialSQL="UPDATE contactos SET nombre=?, correo=?, Direccion=?, Telefono=? WHERE id=?"
        cursor.execute(sentencialSQL, datosContacto)
        conexion.commit() # Da como ejecutado 
        conexion.close()