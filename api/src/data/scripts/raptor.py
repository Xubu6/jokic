import os
from bs4 import BeautifulSoup
from selenium import webdriver
import mysql.connector
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from ast import literal_eval

# UTILITY FUNCTIONS
def convert(val):
    try:
        return literal_eval(val)
    except:
        return val

def filter_neg(val):
    filtered_str = val.replace('−', '-')
    return filtered_str

URL = "https://projects.fivethirtyeight.com/nba-player-ratings/"

# install latest chrome driver if not already installed
chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get(URL)

slider = driver.find_element(By.CLASS_NAME, 'slider')
ActionChains(driver).click_and_hold(slider).move_by_offset(-300, 0).perform()
# expands table
driver.find_element(By.XPATH, '//*[@id="table"]/thead/tr[2]/th[2]').click()

# Start to build scraped player data
player_data = []

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
table = soup.find("table", { "id": "table"})
tbody = table.find("tbody")
table_rows = tbody.find_all("tr")

for row in table_rows:
    fields_list = []
    player_name = row.find("td", class_="name").text
    fields_list.append(player_name.split("'")[0])
    num_fields = row.find_all("td", class_="num")
    for field in num_fields:
        fields_list.append(convert(filter_neg(field.text)))
    # remove mp
    del fields_list[1:8]
    player_data.append(fields_list)
    
# Query
insert_player_data_query = """
INSERT INTO raptor 
    (PLAYER_NAME,
    O_RAPTOR,
    D_RAPTOR,
    RAPTOR,
    RAPTOR_WAR) VALUES (%s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    O_RAPTOR=VALUES(O_RAPTOR),
    D_RAPTOR=VALUES(D_RAPTOR),
    RAPTOR=VALUES(RAPTOR),
    RAPTOR_WAR=VALUES(RAPTOR_WAR)
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