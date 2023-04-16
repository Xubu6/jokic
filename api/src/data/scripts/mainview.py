import os
import mysql.connector

update_view_query = """
CREATE OR REPLACE VIEW main_view AS
SELECT ROW_NUMBER() OVER(ORDER BY umbinaam.umbinaam DESC) AS rk, nba.player_name, nba.team_abbreviation, nba.min, umbinaam.umbinaam, nbaa.net_rating, nbaa.pie, bbref.per, bbref.ws_per_48, bbref.bpm, bbref.vorp, epm.epm, epm.e_wins, lebron.lebron, lebron.bbi_war, rpm.rpm, rpm.rpm_wins, wpa.wpa, wpa.k_wpa, raptor.raptor, raptor.raptor_war, fic.fic, dpm.dpm
FROM nba_main AS nba
LEFT JOIN nba_advanced AS nbaa ON nbaa.player_name=nba.player_name
LEFT JOIN bbref ON bbref.player_name=nba.player_name
LEFT JOIN epm ON epm.player_name=nba.player_name
LEFT JOIN lebron ON lebron.player_name=nba.player_name
LEFT JOIN rpm ON rpm.player_name=nba.player_name
LEFT JOIN wpa ON wpa.player_name=nba.player_name
LEFT JOIN raptor ON raptor.player_name=nba.player_name
LEFT JOIN fic ON fic.player_name=nba.player_name
LEFT JOIN dpm ON dpm.player_name=nba.player_name
LEFT JOIN umbinaam ON umbinaam.player_name=nba.player_name
WHERE nba.min > 100
"""

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
# Create main_view view if needed
try:
    cursor.execute(update_view_query)
    print('Successfully updated main_view!')
except mysql.connector.Error as e:
    print('Could not execute query:', e)

connection.close()

