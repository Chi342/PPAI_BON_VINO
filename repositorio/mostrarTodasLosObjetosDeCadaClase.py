from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib
# repositorio/queryAll.py
import sys
import os
import connection

# Añadir el directorio base al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dominio.TodasLasClases import Bodega, Pais, Provincia, RegionVitivinicola, Resenia, Varietal, Vino

# Define the connection string
params = urllib.parse.quote_plus(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MAIN;'
    'DATABASE=Bon_vino;'
    'Trusted_Connection=yes;'
)

# Create the SQLAlchemy engine
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
Session = sessionmaker(bind=engine)
session = Session()

# Display objects for each class
try:
    print("Bodegas:")
    bodegas = session.query(Bodega).all()
    for bodega in bodegas:
        print(bodega.__dict__)
        
    print("\nPaises:")
    paises = session.query(Pais).all()
    for pais in paises:
        print(pais.__dict__)

    print("\nProvincias:")
    provincias = session.query(Provincia).all()
    for provincia in provincias:
        print(provincia.__dict__)

    print("\nRegiones Vitivinícolas:")
    regiones = session.query(RegionVitivinicola).all()
    for region in regiones:
        print(region.__dict__)

    print("\nResenias:")
    resenias = session.query(Resenia).all()
    for resenia in resenias:
        print(resenia.__dict__)

    print("\nVarietales:")
    varietales = session.query(Varietal).all()
    for varietal in varietales:
        print(varietal.__dict__)

    print("\nVinos:")
    vinos = session.query(Vino).all()
    for vino in vinos:
        print(vino.__dict__)

except Exception as e:
    print(f"Error querying database: {e}")
finally:
    session.close()
