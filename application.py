
from sqlalchemy import create_engine, text, URL
from sqlalchemy.exc import SQLAlchemyError, ProgrammingError

from functions import drop_database, create_database
from selects_inserts import *
from menu import main_menu

#checar se banco existe com root engine, inicializar o banco caso não exista
#sistema possuirá funcionalidades descritas no requerimento de projeto
#demais funcionalidades serão criadas para demonstração dos requisitos

url_object = URL.create(
    "mysql+mysqlconnector",
    username="root",
    password="Usuario123",
    host="localhost"
)


engine = create_engine(url_object)



try:
    create_database(engine)

except SQLAlchemyError as e:
    pass

else:
    print("base de dados restaurante não encontrado, criando database.")


main_menu(engine)