from dataclasses import field
import sqlite3 as sql

def createDB():
    conn = sql.connect("scoreplayer.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE players ( 
            Players text,
            Score integer
        )"""
    )
    conn.commit()
    conn.close()


def inser_row(name, score):
    conn = sql.connect("scoreplayer.db")
    Cursor = conn.cursor()
    instruccion = f"INSERT INTO Players VALUES ('{name}', {score})"
    Cursor.execute(instruccion)
    conn.commit()
    conn.close()


def read_Rows(score):
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"SELECT * FROM players ORDER BY {score} DESC"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    print(datos)
    conn.close()
    return(str(datos[0][0])) +' '+ (str(datos[0][1]))
    

def read_Rows2(field):
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"SELECT * FROM players ORDER BY {field} DESC"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()
    return(str(datos[1][0])) +' '+ (str(datos[1][1]))
    

def read_Rows3(field):
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"SELECT * FROM players ORDER BY {field} DESC "
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()
    return(str(datos[2][0])) +' '+ (str(datos[2][1]))

def read_Rows4(field):
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"SELECT * FROM players ORDER BY {field} DESC"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()
    return(str(datos[3][0])) +''+ (str(datos[3][1]))

def read_Rows5(Score):
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"SELECT * FROM players ORDER BY {Score} DESC"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()
    print(datos)
    return(str(datos[4][0])) +''+(str(datos[4][1]))
    
    

def read_ordered(field):
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"SELECT * FROM players ORDER BY {field} DESC"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()
    print(datos)
    


def delete_row():
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"DELETE FROM players WHERE players BETWEEN 5 AND 20"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()
    


def updatescores():
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"UPDATE * FROM players DESC"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()


#if __name__ == "__main__":
    #createDB()
    #createTable()
    #inser_row(text_name, score)
    #read_ordered("score")
 #   read_Rows("score")
    #delete_row()

