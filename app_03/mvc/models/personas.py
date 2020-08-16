import mysql.connector

class Personas():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='tdt2o4w5d4pzr9ku',
                password='i0guivg1m23zx58w',
                host='g3v9lgqa8h5nq05o.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port='3306',
                database='npbisznd0tcga0ia'     
            )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)
    
    def select(self):
        try:
            self.connect()
            query = ("SELECT * from personas;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id_persona':row[0],
                    'nombre':row[1],
                    'apellido_p':row[2],
                    'apellido_m':row[3],
                    'edad':row[4],
                    'fecha_nacimiento':row[5],
                    'genero':row[6],
                    'estado':row[7]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result=[]
            return result
    
    def view(self, id_persona):
        try:
            self.connect()
            query = ("SELECT * from personas where id_persona = %s;")
            values = (id_persona,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                r = {
                    'id_persona':row[0],
                    'nombre':row[1],
                    'apellido_p':row[2],
                    'apellido_m':row[3],
                    'edad':row[4],
                    'fecha_nacimiento':row[5],
                    'genero':row[6],
                    'estado':row[7]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
    
    def insert(self, nombre, apellido_p, apellido_m, edad, fecha_nacimiento, genero, estado):
        try:
            self.connect()
            query = ("INSERT INTO personas ( nombre, apellido_p, apellido_m, edad, fecha_nacimiento, genero, estado) values (%s,%s,%s,%s,%s,%s,%s);")
            values = (nombre, apellido_p, apellido_m, edad, fecha_nacimiento, genero, estado)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def delete(self, id_persona):
        try:
            self.connect()
            query = ("DELETE FROM personas WHERE id_persona = %s;")
            values = (id_persona,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def update(self, id_persona, nombre, apellido_p, apellido_m, edad, fecha_nacimiento, genero, estado):
        try:
            self.connect()
            query = ("UPDATE personas SET nombre=%s, apellido_p=%s, apellido_m=%s, edad=%s, fecha_nacimiento=%s, genero=%s, estado=%s WHERE id_persona=%s;")
            values = (nombre, apellido_p, apellido_m, edad, fecha_nacimiento, genero, estado, id_persona)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
            

objeto = Personas()

#objeto.delete(1)
#objeto.insert("Fer","Lopez","Gutierres","20","2000-02-01","Masculino","Hidalgo")
#objeto.update(3, "Armin", "Van", "Buuren", "45", "1998-03-02", "MAsculino", "Amsterdam" )
for row in objeto.select():
    print(row)