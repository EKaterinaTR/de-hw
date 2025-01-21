import  psycopg
import os

# Получите параметры подключения из переменных окружения
db_name =  os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = 'localhost'
db_port = 5552

db_name =  'metabase' #os.getenv('DB_NAME')
db_user = 'metabase' #os.getenv('DB_USER')
db_password = 'metabase' #os.getenv('DB_PASSWORD')
db_host = 'localhost'  # или используйте IP-адрес вашего хоста
db_port = 5552

# Установите соединение с базой данных
connection = psycopg.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        port = db_port
    )


cursor = connection.cursor()
    
create_table_query = '''
    CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);


-- Создание основной таблицы произведений
CREATE TABLE stories (
    id Bigint PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    date_last_version TIMESTAMP NOT NULL,
    short_description TEXT,
    last_month_readed INT DEFAULT 0,
    all_readed INT DEFAULT 0,
    likes INT DEFAULT 0,
    dislikes INT DEFAULT 0,
    part_count INT DEFAULT 0,
    end_count INT DEFAULT 0,
    music VARCHAR(255)
);
-- Создание промежуточной таблицы для связи произведений и жанров
CREATE TABLE story_genres (
    story_id INT REFERENCES stories(id) ON DELETE CASCADE,
    genre_id INT REFERENCES genres(id) ON DELETE CASCADE,
    PRIMARY KEY (story_id, genre_id)
);
    '''
print(create_table_query)
    
cursor.execute(create_table_query)
connection.commit()
print("Таблица создана успешно.")

