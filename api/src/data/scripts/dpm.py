import os
import time
from selenium import webdriver
import mysql.connector
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from ast import literal_eval

# UTILITY FUNCTIONS
def convert(val):
    try:
        return literal_eval(val)
    except:
        return val
    
def format_fields(fields):
    formatted_fields = []
    for field in fields:
        formatted_fields.append(convert(field))
    return formatted_fields

URL = "https://apanalytics.shinyapps.io/DARKO//"

# install latest chrome driver if not already installed
chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get(URL)

# navigate to dpm table
driver.find_element(By.XPATH, '/html/body/div[1]/nav/div/ul/li[2]/a').click()
time.sleep(4)

player_data = []

entries = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0_info"]').text
num_entries = convert(entries.split(' ')[-2])

while (len(player_data)) <= num_entries:
    table = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0"]/tbody')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        player_fields = []
        fields_list = row.find_elements(By.TAG_NAME, 'td')
        
        player_fields.append(fields_list[1].text) # name
        player_fields.append(fields_list[3].text) # dpm
        player_fields.append(fields_list[5].text) # o_dpm
        player_fields.append(fields_list[6].text) # d_dpm
        player_fields.append(fields_list[7].text) # box_dpm
        formatted_fields = format_fields(player_fields)
        player_data.append(formatted_fields)
    next_button = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0_next"]')
    next_button.click()
    time.sleep(0.5)

# Query
insert_player_data_query = """
INSERT INTO dpm 
    (PLAYER_NAME,
    DPM,
    O_DPM,
    D_DPM,
    BOX_DPM) VALUES (%s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    DPM=VALUES(DPM),
    O_DPM=VALUES(O_DPM),
    D_DPM=VALUES(D_DPM),
    BOX_DPM=VALUES(BOX_DPM)
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

# Update raptor table
try:
    cursor.executemany(insert_player_data_query, player_data)
    connection.commit()
    print('Inserted data into raptor successfully', player_data)
except mysql.connector.Error as e:
    print('Could not insert player data:', e)

connection.close()