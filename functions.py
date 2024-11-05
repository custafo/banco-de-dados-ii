
from sqlalchemy import create_engine, text, URL



def execute_from_file(engine, path: str):

    
    with open(path, 'r') as file:
        sql_script = file.read()

    
    
    with engine.connect() as connection:


        statements = sql_script.split(';')

        for statement in statements:
            connection.execute(text(statement))

def drop_database(engine):

    with engine.connect() as connection:

            connection.execute(text("drop database restaurante"))


def create_database(engine):
     
    execute_from_file(engine, 'scripts/restaurantedatabase.sql')

    execute_from_file(engine, 'scripts/insertions.sql')

    execute_from_file(engine, 'scripts/users.sql')



    