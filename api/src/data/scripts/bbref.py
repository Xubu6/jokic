import requests
import os
from bs4 import BeautifulSoup
import datetime
from ast import literal_eval
import mysql.connector

def convert(val):
    try:
        return literal_eval(val)
    except:
        return val

current_year = datetime.date.today().year

URL = 'https://www.basketball-reference.com/leagues/NBA_{}_advanced.html'.format(
    current_year)
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("tbody")
table_rows = table.find_all("tr", class_="full_table")

player_data = []

print('Beginning bbref scrapeage...\n_________________________________________')

# Populate player data
for row in table_rows:
    player_name = row.find("a").text.strip()
    per = row.find("td", {"data-stat": "per"}).text
    ows = row.find("td", {"data-stat": "ows"}).text
    dws = row.find("td", {"data-stat": "dws"}).text
    ws = row.find("td", {"data-stat": "ws"}).text
    ws_per_48 = row.find("td", {"data-stat": "ws_per_48"}).text
    obpm = row.find("td", {"data-stat": "obpm"}).text
    dbpm = row.find("td", {"data-stat": "dbpm"}).text
    bpm = row.find("td", {"data-stat": "bpm"}).text
    vorp = row.find("td", {"data-stat": "vorp"}).text
    player_row = [player_name, convert(per), convert(ows), convert(dws), convert(
        ws), convert(ws_per_48), convert(obpm), convert(dbpm), convert(bpm), convert(vorp)]
    player_data.append(player_row)
    
# Query
insert_player_data_query = """
INSERT INTO bbref 
    (PLAYER_NAME,
    PER,
    OWS,
    DWS,
    WS,
    WS_PER_48,
    OBPM,
    DBPM,
    BPM,
    VORP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    PER=VALUES(PER),
    OWS=VALUES(OWS),
    DWS=VALUES(DWS),
    WS=VALUES(WS),
    WS_PER_48=VALUES(WS_PER_48),
    OBPM=VALUES(OBPM),
    DBPM=VALUES(DBPM),
    BPM=VALUES(BPM),
    VORP=VALUES(VORP)
"""    

# Establish MySQL DB Connection
try:
    connection = mysql.connector.connect(
        host="localhost",
        user=os.environ.get('MYSQL_DB_USER'),
        password=os.environ.get('MYSQL_DB_PASS'),
        database="jokic"
    )
except mysql.connector.Error as e:
    print(e)
cursor = connection.cursor()

# Update bbref table
try:
    cursor.executemany(insert_player_data_query, player_data)
    connection.commit()
    print('Inserted data into bbref successfully', player_data)
except mysql.connector.Error as e:
    print('Could not insert player data into bbref:', e)

connection.close()


