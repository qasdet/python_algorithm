import hashlib, uuid, sqlite3


def passwd_check():
    login = input("Введите логин")
    passwd = input("Введите пароль")
    salt = 'my_salt'
    hashed_passwd = hashlib.sha256(passwd.encode() + salt.encode()).hexdigest()
    passwd_2 = input("Введите пароль еще раз для проверки:")
    hashed_passwd_2 = hashlib.sha256(passwd_2.encode() + salt.encode()).hexdigest()

    conn = sqlite3.connect('Chinook_Sqlite.sqlite')

    cursor = conn.cursor()


cursor.execute("""create table if not exists users (
        id SERIAL PRIMARY KEY,
        lgn VARCHAR(100),
        password_hash VARCHAR(100)
    ); """)
cursor.execute("select password_hash from users where lgn =?", (login,))
res = cursor.fetchall()
if res:
    if hashed_passwd_2 == str(res[0][0]) and hashed_passwd_2 == hashed_passwd:
        print("Вы ввели правильный пароль")
    else:
        print("Вы ввели неправильный пароль! Попробуйте еще раз")
        conn.close()
        passwd_check()
else:
    if hashed_passwd == hashed_passwd_2:
        cursor.execute("insert into users(lgn, password_hash) values (?, ?)", (login, hashed_passwd,))
        conn.commit()
        print(f'Пароли совпадают! Регистрация прошла успешно!'
              f'В базе данных хранится строка: {hashed_passwd}')
        conn.close()
    else:
        print("Пароли не совпадают! Попробуйте еще раз!")
        conn.close()
        passwd_check()
