from decimal import Decimal
import os
import mysql.connector
import time

fetch_all_query = """
SELECT nba.player_id, nba.player_name, nbaa.net_rating, nbaa.pie, bbref.per,
    bbref.ws_per_48, bbref.bpm, bbref.vorp, epm.epm, epm.e_wins, lebron.lebron, lebron.bbi_war, 
    rpm.rpm, rpm.rpm_wins, wpa.wpa, raptor.raptor, raptor.raptor_war, fic.fic, dpm.dpm
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
"""

get_sd_mean_query = """
SELECT STDDEV(nbaa.net_rating), AVG(nbaa.net_rating), STDDEV(nbaa.pie), AVG(nbaa.pie), STDDEV(bbref.per), AVG(bbref.per), STDDEV(bbref.ws_per_48), AVG(bbref.ws_per_48), STDDEV(bbref.bpm), AVG(bbref.bpm),
    STDDEV(bbref.bpm), AVG(bbref.bpm), STDDEV(bbref.vorp), AVG(bbref.vorp), STDDEV(epm.epm), AVG(epm.epm), STDDEV(epm.e_wins), AVG(epm.e_wins), STDDEV(lebron.lebron),
    AVG(lebron.lebron), STDDEV(lebron.bbi_war), AVG(lebron.bbi_war), STDDEV(rpm.rpm), AVG(rpm.rpm), STDDEV(rpm.rpm_wins), AVG(rpm.rpm_wins), 
    STDDEV(wpa.wpa), AVG(wpa.wpa), STDDEV(raptor.raptor), AVG(raptor.raptor), STDDEV(raptor.raptor_war), AVG(raptor.raptor_war), STDDEV(fic.fic), AVG(fic.fic), STDDEV(dpm.dpm), AVG(dpm.dpm)
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
WHERE nba.min > 850;
"""


def calculate_z_score(stat, std, avg):
    if not stat or not std or not avg:
        return Decimal(0.0)
    return (stat - avg) / std

# UMBINAAM = Ultimately Meaningless But Interesting Nonetheless All-in-One Advanced Metric


def calculate_umbinaam(player_stats, analytics):
    _, _, net_rating, pie, per, ws_per_48, bpm, vorp, epm, e_wins, lebron, bbi_war, rpm, rpm_wins, wpa, raptor, raptor_war, fic, dpm = player_stats
    net_rating_z_score = calculate_z_score(
        net_rating, Decimal(analytics[0]), analytics[1])
    pie_z_score = calculate_z_score(pie, Decimal(analytics[2]), analytics[3])
    per_z_score = calculate_z_score(per, Decimal(analytics[4]), analytics[5])
    ws_per_48_z_score = calculate_z_score(
        ws_per_48, Decimal(analytics[6]), analytics[7])
    net_rating_z_score = calculate_z_score(
        net_rating, Decimal(analytics[8]), analytics[9])
    bpm_z_score = calculate_z_score(bpm, Decimal(analytics[10]), analytics[11])
    vorp_z_score = calculate_z_score(
        vorp, Decimal(analytics[12]), analytics[13])
    epm_z_score = calculate_z_score(epm, Decimal(analytics[14]), analytics[15])
    e_wins_z_score = calculate_z_score(
        e_wins, Decimal(analytics[16]), analytics[17])
    lebron_z_score = calculate_z_score(
        lebron, Decimal(analytics[18]), analytics[19])
    bbi_war_z_score = calculate_z_score(
        bbi_war, Decimal(analytics[20]), analytics[21])
    rpm_z_score = calculate_z_score(rpm, Decimal(analytics[22]), analytics[23])
    rpm_wins_z_score = calculate_z_score(
        rpm_wins, Decimal(analytics[24]), analytics[25])
    wpa_z_score = calculate_z_score(wpa, Decimal(analytics[26]), analytics[27])
    raptor_z_score = calculate_z_score(
        raptor, Decimal(analytics[28]), analytics[29])
    raptor_war_z_score = calculate_z_score(
        raptor_war, Decimal(analytics[30]), analytics[31])
    fic_z_score = calculate_z_score(fic, Decimal(analytics[32]), analytics[33])
    dpm_z_score = calculate_z_score(dpm, Decimal(analytics[34]), analytics[35])

    umbinaam = ((net_rating_z_score * Decimal(0.15)) + pie_z_score + (per_z_score * Decimal(0.30)) + (ws_per_48_z_score * Decimal(0.30)) + (bpm_z_score * Decimal(0.75))
                + (vorp_z_score * Decimal(0.75)) + epm_z_score + (e_wins_z_score * Decimal(0.50)) + lebron_z_score + (bbi_war_z_score * Decimal(0.50))
                + rpm_z_score + (rpm_wins_z_score * Decimal(0.50)) + wpa_z_score + raptor_z_score + (raptor_war_z_score * Decimal(0.50))
                + fic_z_score + (dpm_z_score * Decimal(0.75))) / Decimal(12.0)
    return umbinaam


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

try:
    cursor.execute(get_sd_mean_query)
    analytics = cursor.fetchone()
except mysql.connector.Error as e:
    print('Could not execute query:', e)

data = []

try:
    cursor.execute(fetch_all_query)
    data = cursor.fetchall()
    print('Data fetched')
except mysql.connector.Error as e:
    print('Could not execute query:', e)

umbinaam_data = []

for row in data:
    player_data = []
    umbinaam = calculate_umbinaam(row, analytics)
    player_name = row[1]
    player_data.append(player_name)
    player_data.append(umbinaam)
    umbinaam_data.append(player_data)

connection.close()

# inserting data
# Query
insert_player_data_query = """
INSERT INTO umbinaam 
    (PLAYER_NAME,
    UMBINAAM) VALUES (%s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_NAME=VALUES(PLAYER_NAME),
    UMBINAAM=VALUES(UMBINAAM)
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

# Update umbinaam table
try:
    cursor.executemany(insert_player_data_query, umbinaam_data)
    connection.commit()
    print('Inserted data into umbinaam successfully', umbinaam_data)
except mysql.connector.Error as e:
    print('Could not insert player data:', e)

connection.close()
