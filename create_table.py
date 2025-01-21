import  psycopg2
import os

# Получите параметры подключения из переменных окружения
db_name =  'metabase' #os.getenv('DB_NAME')
db_user = 'metabase' #os.getenv('DB_USER')
db_password = 'metabase' #os.getenv('DB_PASSWORD')
db_host = 'localhost'  # или используйте IP-адрес вашего хоста
db_port = 5432

cursor = None
connection = None


# Установите соединение с базой данных
connection = psycopg2.connect(
        dbname='metabase',
        user='metabase',
        password='metabase',
        # host=db_host,
        # port=db_port
    )

cursor = connection.cursor()
    
    # Пример SQL-запроса: создание таблицы
create_table_query = '''
    CREATE TABLE IF NOT EXISTS example_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL
    );
    '''
print(create_table_query)
    
cursor.execute(create_table_query)
connection.commit()
print("Таблица создана успешно.")

    # Пример вставки данных
insert_query = '''
    INSERT INTO example_table (name, age) VALUES (%s, %s);
    '''
    
data_to_insert = ('Alice', 30)
cursor.execute(insert_query, data_to_insert)
connection.commit()
print("Данные вставлены успешно.")

    # Пример выборки данных
select_query = "SELECT * FROM example_table;"
cursor.execute(select_query)
records = cursor.fetchall()
    
print("Выборка данных:")
for row in records:
    print(row)

if cursor:
    cursor.close()
if connection:
    connection.close()
    print("Соединение с PostgreSQL закрыто.")
