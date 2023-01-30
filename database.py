from databases import Database
import asyncio
import asyncpg


async def create():
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        print('Соединение с БД установлено')
        create = """create table users_test (id int, name varchar(10), gender varchar(10))"""
        print('Таблица users_test создана успешно')
        await database.execute(query=create)
        insert = """insert into users_test (id, name, gender) values
                    (1,'Александр','Мужской'),
                    (2,'Константин','Мужской'),
                    (3,'Светлана','Женский'),
                    (4,'Алевтина','Женский'),
                    (5,'Всеволод','Мужской')"""
        await database.execute(query=insert)
        await database.disconnect()
        print('Соединение с БД разорвано')

    except:
        print('Ошибка подключения к БД')

asyncio.run(create())