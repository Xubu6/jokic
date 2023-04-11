import requests
import os
from bs4 import BeautifulSoup
from ast import literal_eval
import mysql.connector

def convert(val):
    try:
        return literal_eval(val)
    except:
        return val
    
keep_indices = [1, 4, 5, 15]

def format_row(row_list):
    formatted_row = [convert(row_list[index]) for index in keep_indices]
    return formatted_row
    
# get group (page) urls
URL = 'https://stats.inpredictable.com/nba/ssnPlayer.php'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
filter_group = soup.find("div", class_="slbl")
groups = filter_group.find_all("a", href=True)
group_urls = [URL]
for group in groups:
    url = group['href']
    group_urls.append(url)
    
player_data = []
    
for group_url in group_urls:
    print('Scraping', group_url, '...')
    page = requests.get(group_url)
    if not page:
        print('Something went wrong getting page', group_url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("table")
    tbody = table.find("tbody")
    table_rows = tbody.find_all("tr")
    for row in table_rows:
        player_fields = []
        fields_list = row.find_all("td")
        # non-header rows
        if len(fields_list) > 2:
            counter = 1
            for field in fields_list:
                if counter > 16:
                    break
                player_fields.append(field.text.replace('−', '-'))
                counter+=1
            player_data.append(format_row(player_fields))

# Query
insert_player_data_query = """
INSERT INTO wpa 
    (PLAYER_NAME,
    WPA,
    E_WPA,
    K_WPA) VALUES (%s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    WPA=VALUES(WPA),
    E_WPA=VALUES(E_WPA),
    K_WPA=VALUES(K_WPA)
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

# Update epm table
try:
    cursor.executemany(insert_player_data_query, player_data)
    connection.commit()
    print('Inserted data into rpm successfully', player_data)
except mysql.connector.Error as e:
    print('Could not insert player data:', e)

connection.close()