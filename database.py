import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="football_team_management"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS club(club_id INT, name VARCHAR(30),shortform CHAR(5),league VARCHAR(15),ranking INT,value INT)')


def add_data(club_id,name,shortform,league,ranking,value):
    c.execute('INSERT INTO club(club_id,name,shortform,league,ranking,value) VALUES (%s,%s,%s,%s,%s,%s)',
              (club_id,name,shortform,league,ranking,value))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM club')
    data = c.fetchall()
    return data


def view_only_club_id():
    c.execute('SELECT club_id FROM club')
    data = c.fetchall()
    return data


def edit_data(new_value,club_id):
    c.execute("UPDATE club SET value=%s where club_id = %s", (new_value,club_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(club_id):
    c.execute('DELETE FROM club WHERE club_id="{}"'.format(club_id))
    mydb.commit()