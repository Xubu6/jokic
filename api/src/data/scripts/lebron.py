import os
from selenium import webdriver
import mysql.connector
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from ast import literal_eval

def convert(val):
    try:
        return literal_eval(val)
    except:
        return val

def format_row(field_list):
    formatted_row = []
    for field in field_list:
        formatted_row.append(convert(field))
    return formatted_row
    

URL = "https://www.bball-index.com/lebron-database/"

from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless");
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)

# filter for current season
season_filter = driver.find_element(By.ID, "table_1_2_filter")
season_filter_input = season_filter.find_element(By.TAG_NAME, "input")
season_filter_input.send_keys('2023-24') # DOES NOT YET EXIST

# select all entries from dropdown
dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_value('-1')

table = driver.find_element(By.TAG_NAME, "tbody")
rows = table.find_elements(By.TAG_NAME, "tr")

player_data = []

print('Beginning lebron scrapeage...\n_________________________________________')

for row in rows:
    fields = row.find_elements(By.TAG_NAME, "td")
    field_num = 1
    field_list = []
    for field in fields:
        if (field_num == 1 or field_num > 7) and field_num != 12:
            field_list.append(field.text.replace('−', '-'))
        field_num+=1
    print('field data:', field_list)
    formatted_field_list = format_row(field_list)
    player_data.append(formatted_field_list)
    # print('PLAYER_DATA:', player_data)

# Query
insert_player_data_query = """
INSERT INTO lebron_2024 
    (PLAYER_NAME,
    LEBRON,
    O_LEBRON,
    D_LEBRON,
    BBI_WAR,
    BOX_LEBRON,
    BOX_O_LEBRON,
    BOX_D_LEBRON) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    LEBRON=VALUES(LEBRON),
    O_LEBRON=VALUES(O_LEBRON),
    D_LEBRON=VALUES(D_LEBRON),
    BBI_WAR=VALUES(BBI_WAR),
    BOX_LEBRON=VALUES(BOX_LEBRON),
    BOX_O_LEBRON=VALUES(BOX_O_LEBRON),
    BOX_D_LEBRON=VALUES(BOX_D_LEBRON)
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

# Update lebron table
try:
    cursor.executemany(insert_player_data_query, player_data)
    connection.commit()
    print('Inserted data into lebron successfully', player_data)
except mysql.connector.Error as e:
    print('Could not insert player data into lebron:', e)

connection.close()
    
    
