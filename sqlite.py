import sqlite3 as sq
async def db_start():
    global db, cur

    db = sq.connect('databd.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS opros(user_id TEXT PRIMARY KEY"
                ", price_quality TEXT, Company TEXT, rate TEXT, quality_assessment TEXT"
                ", cost_estimation TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY"
                ", Familiya TEXT, Name TEXT, LastName TEXT,"
                " street TEXT"
                ", Dom TEXT,"
                "Kvartira TEXT,"
                "PhoneNumber TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS text_table(HelolText TEXT,WherePlus TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS tarifi(MainName TEXT,caption TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS questions(q1 TEXT,q2 TEXT,q3 TEXT,q4 TEXT,q5 TEXT)")

    db.commit()

def update_table(text,obj):
    """Обновление базы данных , сначало ввод какой именно текст изменить , а потом его содержимое"""
    db = sq.connect('databd.db')
    cur = db.cursor()
    sql = cur.execute("UPDATE text_table SET {} = '{}' ".format(text,obj))
    db.commit()

def show_on_bd(name_table):
    db = sq.connect('databd.db')
    cur = db.cursor()
    sql = cur.execute("SELECT {key} FROM text_table".format(key=name_table)).fetchone()
    db.commit()
    return  sql[0]


async def create_opros(user_id):
    db = sq.connect('databd.db')
    cur = db.cursor()

    user = cur.execute("SELECT 1 FROM opros WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO opros VALUES(?, ? , ? , ? , ?,?)", (user_id, '', '', '', '',''))
        db.commit()

async def create_profile(user_id):
    db = sq.connect('databd.db')
    cur = db.cursor()

    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ? , ? , ? , ?,?, ?,?)", (user_id, '', '', '', '','', '',''))
        db.commit()

async def edit_opros(user_id,data):
    db = sq.connect('databd.db')
    cur = db.cursor()


    cur.execute("UPDATE opros SET price_quality = '{}', Company = '{}', rate = '{}', quality_assessment = '{}',cost_estimation = '{}' WHERE user_id == '{}'".format(
        data['question1'], data['question2'], data['question3'], data['question4'],data['question5'],user_id))
    db.commit()

async def edit_profile(user_id,data):
    db = sq.connect('databd.db')
    cur = db.cursor()


    cur.execute("UPDATE profile SET Familiya = '{}', Name = '{}', LastName = '{}', street = '{}',Dom = '{}',Kvartira = '{}',PhoneNumber ='{}' WHERE user_id == '{}'".format(
        data['Фамилия'], data['Имя'], data['Отчество'], data['Улица'],data['Дом'],data['Квартира'],data['Номер Телефона'],user_id))
    db.commit()

