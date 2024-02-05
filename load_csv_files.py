import pandas as pd
import sqlalchemy as sqlalchemy
import psycopg2


conn_string = 'postgresql://postgres:hovnocuc1@localhost/painting' ##Pomoci sqlalchemy se napojim na url me dtabase, postgresql://nazev databaze: heslo@kde bezi/nazev nove databaze
db = sqlalchemy.create_engine(conn_string)
conn = db.connect()


files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

for file in files:
    df = pd.read_csv(f"C:/Users/Sexyborec/Desktop/SQLProject/{file}.csv") ##nahrani csv od pythonu musi byt takto opacna lomitka #print(df.info)
    df.to_sql(file, con=conn, if_exists='replace', index=False) #nahrani csv do sql database, nyni muzu to udelat vickrat nebo for loop pro vsechny csv files v listu files

