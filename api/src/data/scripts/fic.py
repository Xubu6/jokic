import requests
import os
import mysql.connector
from bs4 import BeautifulSoup
from ast import literal_eval

def convert(val):
    try:
        return literal_eval(val)
    except:
        return val
    
def prune_fields(player_fields):
    pruned_fields = []
    del player_fields[4:19]
    del player_fields[2]
    del player_fields[0]
    del player_fields[-1]
    i = 0
    for field in player_fields:
        pruned_fields.append(convert(field.replace(',', '')))
        i+=1
    return pruned_fields
    
player_data = []

print('Beginning fic scrapeage...\n_________________________________________')
    
page_num = 1
is_next_page_available = 0
current_year = 2024

while is_next_page_available == 0:
    URL = "https://basketball.realgm.com/nba/stats/{}/Advanced_Stats/All/fic/All/desc/{}/Regular_Season".format(current_year, page_num)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    next_page = soup.find("p", attrs={ "style": "text-align: center;" }).find_all("a")[-1].text if soup.find("p", attrs={ "style": "text-align: center;" }) else None
    is_next_page_available = next_page.find("Next Page") # flag for if a next page is available
    
    table = soup.find("table", attrs={ "data-tablesaw-mode": "swipe" })
    tbody = table.find("tbody")
    table_rows = tbody.find_all("tr")
    for row in table_rows:
        fields_list = row.find_all("td")
        player_fields = []
        for field in fields_list:
            player_fields.append(field.text)
        pruned_fields = prune_fields(player_fields)
        player_data.append(pruned_fields)
    page_num+=1

# Query
insert_player_data_query = """
INSERT INTO fic_2024
    (PLAYER_NAME,
    TS,
    FIC) VALUES (%s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    TS=VALUES(TS),
    FIC=VALUES(FIC)
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

# Update fic table
try:
    cursor.executemany(insert_player_data_query, player_data)
    connection.commit()
    print('Inserted data into fic successfully', player_data)
except mysql.connector.Error as e:
    print('Could not insert player data into fic:', e)

connection.close()
