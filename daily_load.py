
import psycopg
drop_sql = """DROP TABLE IF EXISTS story_genres CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS stories CASCADE;"""

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
    
print(drop_sql)
    
cursor.execute(drop_sql)
connection.commit()
print("Таблица удалены успешно.")