import os
import mysql.connector

create_nba_main_table_query = """
CREATE TABLE IF NOT EXISTS nba_main (
    player_id INT NOT NULL,
    player_name VARCHAR(45) NOT NULL,
    season_id VARCHAR(10) NULL,
    league_id VARCHAR(5) NULL,
    team_id INT NULL,
    team_abbreviation VARCHAR(10) NULL,
    player_age DECIMAL(10,3) NULL,
    gp INT NULL,
    gs INT NULL,
    min DECIMAL(10,3) NULL,
    fgm INT NULL,
    fga INT NULL,
    fg_pct DECIMAL(10,3) NULL,
    fg3m INT NULL,
    fg3a INT NULL,
    fg3_pct DECIMAL(10,3) NULL,
    ftm INT NULL,
    fta INT NULL,
    ft_pct DECIMAL(10,3) NULL,
    oreb INT NULL,
    dreb INT NULL,
    reb INT NULL,
    ast INT NULL,
    stl INT NULL,
    blk INT NULL,
    tov INT NULL,
    pf INT NULL,
    pts INT NULL,
    PRIMARY KEY (player_id),
    UNIQUE INDEX player_id_UNIQUE (player_id ASC) VISIBLE);
)
"""

create_nba_advanced_table_query = """
CREATE TABLE IF NOT EXISTS nba_advanced (
    player_id INT NOT NULL,
    player_name VARCHAR(45) NOT NULL,
    group_set VARCHAR(10) NULL,
    group_value VARCHAR(10) NULL,
    team_id INT NULL,
    team_abbreviation VARCHAR(10) NULL,
    max_game_date VARCHAR(45) NULL,
    gp INT NULL,
    w INT NULL,
    l INT NULL,
    w_pct DECIMAL(5,3) NULL,
    min DECIMAL(10,2) NULL,
    e_off_rating DECIMAL(10,2) NULL,
    off_rating DECIMAL(10,2) NULL,
    sp_work_off_rating DECIMAL(10,2) NULL,
    e_def_rating DECIMAL(10,2) NULL,
    def_rating DECIMAL(10,2) NULL,
    sp_work_def_rating DECIMAL(10,2) NULL,
    e_net_rating DECIMAL(10,2) NULL,
    net_rating DECIMAL(10,2) NULL,
    sp_work_net_rating DECIMAL(10,2) NULL,
    ast_pct DECIMAL(5,3) NULL,
    ast_to DECIMAL(5,3) NULL,
    ast_ratio DECIMAL(10,2) NULL,
    oreb_pct DECIMAL(5,3) NULL,
    dreb_pct DECIMAL(5,3) NULL,
    reb_pct DECIMAL(5,3) NULL,
    tm_tov_pct DECIMAL(10,2),
    e_tov_pct DECIMAL(10,2),
    efg_pct DECIMAL(5,3) NULL,
    ts_pct DECIMAL(5,3) NULL,
    usg_pct DECIMAL(5,3) NULL,
    e_usg_pct DECIMAL(5,3) NULL,
    e_pace DECIMAL(10,2) NULL,
    pace DECIMAL(10,2) NULL,
    pace_per40 DECIMAL(10,2) NULL,
    sp_work_pace DECIMAL(10,2) NULL,
    pie DECIMAL(10,3) NULL,
    poss INT NULL,
    fgm INT NULL,
    fga INT NULL,
    fgm_pg DECIMAL(6,2),
    fga_pg DECIMAL(6,2),
    fg_pct DECIMAL(5,3) NULL,
    PRIMARY KEY (player_id),
    UNIQUE INDEX player_id_UNIQUE (player_id ASC) VISIBLE);
)
"""

create_epm_table_query = """
CREATE TABLE IF NOT EXISTS epm (
    player_name VARCHAR(45) NOT NULL,
    e_off_plus_minus DECIMAL(10,2) NULL,
    e_def_plus_minus DECIMAL(10,2) NULL,
    epm DECIMAL(10,2) NULL,
    e_wins DECIMAL(10,2) NULL,
    PRIMARY KEY (player_name));
"""

create_bbref_table_query = """
CREATE TABLE IF NOT EXISTS bbref (
  player_name VARCHAR(45) NOT NULL,
  per DECIMAL(10,2) NULL,
  ows DECIMAL(10,2) NULL,
  dws DECIMAL(10,2) NULL,
  ws DECIMAL(10,2) NULL,
  ws_per_48 DECIMAL(10,2) NULL,
  obpm DECIMAL(10,2) NULL,
  dbpm DECIMAL(10,2) NULL,
  bpm DECIMAL(10,2) NULL,
  vorp DECIMAL(10,2) NULL,
  PRIMARY KEY (player_name));
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
# Create nba_main table if needed
try:
    cursor.execute(create_nba_main_table_query)
    print('nba_main table created! (or not)')
except mysql.connector.Error as e:
    print('Could not create nba_main table:', e)

connection.close()
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

# Create nba_advanced table if needed
try:
    cursor.execute(create_nba_advanced_table_query)
    print('nba_advanced table created! (or not)')
except mysql.connector.Error as e:
    print('Could not create nba_advanced table:', e)

connection.close()
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

# Create epm table if needed
try:
    cursor.execute(create_epm_table_query)
    print('epm table created! (or not)')
except mysql.connector.Error as e:
    print('Could not create epm table:', e)

connection.close()
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

# Create bbref table if needed
try:
    cursor.execute(create_bbref_table_query)
    print('bbref table created! (or not)')
except mysql.connector.Error as e:
    print('Could not create bbref table:', e)

connection.close()
