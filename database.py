import sqlite3

BD = sqlite3.connect("bd_2048.sqlite")


def get_best():
    cursor = BD.cursor()
    cursor.execute("""
        create table if not exists RECORDS(
            name text,
            score integer
        )
    """)
    cursor.execute("""
        SELECT name, max(score) score from RECORDS
        GROUP by name
        ORDER by score DESC
        limit 3
        
    """)
    rez = cursor.fetchall()
    print(rez)
    cursor.close()
    return (rez)


def insert_result(Username, score):
    cursor = BD.cursor()
    cursor.execute(f"""
            INSERT INTO RECORDS (name, score)
            VALUES ('{Username}', '{score}');
        """)
    BD.commit()
    cursor.close()
