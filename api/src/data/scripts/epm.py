import requests
import os
from selenium import webdriver
import mysql.connector
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from ast import literal_eval


URL = "https://www.dunksandthrees.com/epm"

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless");
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)

# UTILITY FUNCTIONS
def convert(val):
    try:
        return literal_eval(val)
    except:
        return val

def filter_row(row_str):
    filtered_str = row_str.replace(' · ', '\n').replace('\n', '|').replace('−', '-')
    return filtered_str

def create_list_from_str(row_str):
    data_list = []
    str_list = row_str.split('|')
    for field in str_list:
        converted = convert(field)
        data_list.append(converted)
    return data_list

# Only for player metadata (e.g. pid, name, team_id, etc.)
def get_player_high_level_data():
    site_data = requests.get("https://wwwdunksandthrees.com/site-data").json()
    player_data = site_data["players"]
    return player_data

def prune_values(row_vals):
    pruned_values = []
    pruned_values.append(row_vals[0]) # full_name
    pruned_values.append(row_vals[10]) # Estimated Offensive +/-
    pruned_values.append(row_vals[12]) # Estimated Defensive +/-
    pruned_values.append(row_vals[14]) # EPM
    pruned_values.append(row_vals[16]) # Estimated Wins
    return pruned_values

# Start to build scraped player data
player_data = []

rows = driver.find_elements(By.XPATH, '/html/body/div/main/div/div[2]/div[1]/div[3]/table/tbody/tr')
num_rows = len(rows)

print('Beginning epm scrapeage...\n_________________________________________')

rows_remaining = True
row = 1
while rows_remaining:
    # exit if all table rows have been fetched
    if row > num_rows:
        rows_remaining = False
        break
    # click on table for scrolling purposes
    driver.find_element(By.XPATH, '/html/body/div/main/div/div[2]/div[1]/div[3]/table/thead/tr[3]/th[1]').click()
    player_row = driver.find_element(By.XPATH, '/html/body/div/main/div/div[2]/div[1]/div[3]/table/tbody/tr[' + str(row) +']').text
    if not player_row:
        # try scrolling
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        player_row = driver.find_element(By.XPATH, '/html/body/div/main/div/div[2]/div[1]/div[3]/table/tbody/tr[' + str(row) +']').text
    row+=1
    filtered_row = filter_row(player_row)
    filtered_row_with_types = create_list_from_str(filtered_row)
    if len(filtered_row_with_types) > 1:
        pruned_row = prune_values(filtered_row_with_types)
        player_data.append(pruned_row)
    
# Query
insert_player_data_query = """
INSERT INTO epm_2024 
    (PLAYER_NAME,
    E_OFF_PLUS_MINUS,
    E_DEF_PLUS_MINUS,
    EPM,
    E_WINS) VALUES (%s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    E_OFF_PLUS_MINUS=VALUES(E_OFF_PLUS_MINUS),
    E_DEF_PLUS_MINUS=VALUES(E_DEF_PLUS_MINUS),
    EPM=VALUES(EPM),
    E_WINS=VALUES(E_WINS)
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
    print('Inserted data into epm successfully', player_data)
except mysql.connector.Error as e:
    print('Could not insert player data into epm:', e)

connection.close()