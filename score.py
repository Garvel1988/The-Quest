from dis import Instruction
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


def read_Rows():
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"SELECT * FROM players"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()
    print(datos)

def read_ordered(field):
    conn = sql.connect("scoreplayer.db")
    cursor = conn.cursor()
    Instruction = f"SELECT * FROM players ORDER BY {field} DESC"
    cursor.execute(Instruction)
    datos = cursor.fetchall()
    conn.close()
    print(datos)


if __name__ == "__main__":
    #createDB()
    #createTable()
    #inser_row(text_name, score)
    read_ordered("Score")
