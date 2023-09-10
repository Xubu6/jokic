import os
from bs4 import BeautifulSoup
from selenium import webdriver
import mysql.connector
from selenium.webdriver.chrome.service import Service
from ast import literal_eval
import time

def convert(val):
    try:
        return literal_eval(val)
    except:
        return val

def format_row(row_str):
    formatted_row = []
    split_row = row_str.split('|')
    for field in split_row:
        formatted_row.append(convert(field))
    del formatted_row[1:3]
    return formatted_row

player_data = []

URL = 'http://www.espn.com/nba/statistics/rpm'

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless");
driver = webdriver.Chrome(service=service, options=options)

driver.get(URL)

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

pages = soup.find("div", class_="page-numbers").text

max_page = convert(pages.split(' ')[-1])
print(f'We will be scraping {max_page} pages.')

time.sleep(3)
print('Beginning rpm scrapeage...\n_________________________________________')

page = None
cur_page = 1
while cur_page <= max_page:
    URL = 'http://www.espn.com/nba/statistics/rpm' if cur_page == 1 else 'http://www.espn.com/nba/statistics/rpm/_/page/{}'.format(cur_page)
    driver.get(URL)
    page = driver.page_source
    print('Onto page ', cur_page)
    time.sleep(2)
    if not page:
        print('invalid URL passed:', URL)
        print('Not sure why but heres what the page looks like: ', page)
        continue
    soup = BeautifulSoup(page, "html.parser")
    table = soup.find("table")
    table_rows = table.find_all("tr")
    row_num = 1
    for row in table_rows:
        # skip header row
        if row_num != 1:
            player_name = row.find("a").text
            fields = row.find_all("td", {"style": "text-align:right;"})
            row_str = player_name
            for field in fields:
                row_str = row_str + '|' + field.text
            formatted_row = format_row(row_str)
            player_data.append(formatted_row)
        row_num+=1
    cur_page+=1
    
# Query
insert_player_data_query = """
INSERT INTO rpm 
    (PLAYER_NAME,
    O_RPM,
    D_RPM,
    RPM,
    RPM_WINS) VALUES (%s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    O_RPM=VALUES(O_RPM),
    D_RPM=VALUES(D_RPM),
    RPM=VALUES(RPM),
    RPM_WINS=VALUES(RPM_WINS)
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

# Update rpm table
try:
    cursor.executemany(insert_player_data_query, player_data)
    connection.commit()
    print('Inserted data into rpm successfully', player_data)
except mysql.connector.Error as e:
    print('Could not insert player data into rpm:', e)

connection.close()