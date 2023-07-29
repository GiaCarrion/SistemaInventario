import mysql.connector

class Registro_funciones():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='inventario_casa', 
                                            user = 'root',
                                            password ='admin')
    
    def agregar(self,codigo,titulo,autor,editorial, año, ubicacion):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO libros (CODIGO, TITULO, AUTOR, EDITORIAL, AÑO, UBICACION)
        VALUES ('{}','{}','{}','{}','{}','{}')'''.format(codigo,titulo,autor,editorial, año, ubicacion)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    
    def mostrar(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM libros" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    
    def burcar(self, titulo):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM libros WHERE TITULO = {}".format(titulo)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 
    
    def eliminar(self, titulo):
        cur = self.conexion.cursor()
        sql='''DELETE FROM libros WHERE titulo = {}'''.format(titulo)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()