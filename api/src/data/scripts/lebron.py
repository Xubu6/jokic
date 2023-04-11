import requests
import os
from selenium import webdriver
import mysql.connector
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

# install latest chrome driver if not already installed
chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get(URL)

# filter for current season
season_filter = driver.find_element(By.ID, "table_1_2_filter")
season_filter_input = season_filter.find_element(By.TAG_NAME, "input")
season_filter_input.send_keys('2022-23')

# select all entries from dropdown
dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_value('-1')

table = driver.find_element(By.TAG_NAME, "tbody")
rows = table.find_elements(By.TAG_NAME, "tr")

player_data = []

for row in rows:
    fields = row.find_elements(By.TAG_NAME, "td")
    field_num = 1
    field_list = []
    for field in fields:
        if field_num == 1 or field_num > 7:
            field_list.append(field.text.replace('−', '-'))
        field_num+=1
    print('field data:', field_list)
    formatted_field_list = format_row(field_list)
    player_data.append(formatted_field_list)

# Query
insert_player_data_query = """
INSERT INTO lebron 
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
    print('Could not insert player data:', e)

connection.close()
    
    
