import os
import time
import mysql.connector
from nba_api.stats.endpoints import playercareerstats, playerdashboardbyyearoveryear
from nba_api.stats.static import players

season_stats = []
season_advanced_stats = []

print('Beginning nba scrapeage...\n_________________________________________')

# Fetch player data for current season
players = players.get_players()
for player in players:
    if player['is_active']:
        id = player['id']
        full_name = player['full_name']
        print('Season stats for', full_name, 'with ID:', id)
        player_stats = playercareerstats.PlayerCareerStats(
            player_id=id).get_dict()['resultSets'][0]
        player_season_stats = player_stats['rowSet']
        player_advanced_stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(
            player_id=id, measure_type_detailed='Advanced').get_dict()['resultSets'][1]
        player_season_advanced_stats = player_advanced_stats['rowSet']
        # no season data for active player (edge case)
        if not player_season_stats:
            continue
        player_current_season_stats = player_season_stats[-1]
        player_current_season_stats.insert(1, full_name)
        season_stats.append(player_current_season_stats)
        # no season advanced data for player (edge case)
        if not player_season_advanced_stats:
            continue
        player_current_season_advanced_stats = player_season_advanced_stats[0]
        player_current_season_advanced_stats.insert(0, id)
        player_current_season_advanced_stats.insert(1, full_name)
        # remove rank clumns (bad data)
        player_current_season_advanced_stats = player_current_season_advanced_stats[: len(
            player_current_season_advanced_stats) - 35]
        season_advanced_stats.append(player_current_season_advanced_stats)
        # print(season_stats)
        time.sleep(.600)

# Populate Database
# Queries
insert_player_data_query = """
INSERT INTO nba_main
    (PLAYER_ID,
    PLAYER_NAME,
    SEASON_ID,
    LEAGUE_ID,
    TEAM_ID,
    TEAM_ABBREVIATION,
    PLAYER_AGE,
    GP,
    GS,
    MIN,
    FGM,
    FGA,
    FG_PCT,
    FG3M,
    FG3A,
    FG3_PCT,
    FTM,
    FTA,
    FT_PCT,
    OREB,
    DREB,
    REB,
    AST,
    STL,
    BLK,
    TOV,
    PF,
    PTS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    PLAYER_ID=VALUES(PLAYER_ID),
    PLAYER_NAME=VALUES(PLAYER_NAME),
    SEASON_ID=VALUES(SEASON_ID),
    LEAGUE_ID=VALUES(LEAGUE_ID),
    TEAM_ID=VALUES(TEAM_ID),
    TEAM_ABBREVIATION=VALUES(TEAM_ABBREVIATION),
    PLAYER_AGE=VALUES(PLAYER_AGE),
    GP=VALUES(GP),
    GS=VALUES(GS),
    MIN=VALUES(MIN),
    FGM=VALUES(FGM),
    FGA=VALUES(FGA),
    FG_PCT=VALUES(FG_PCT),
    FG3M=VALUES(FG3M),
    FG3A=VALUES(FG3A),
    FG3_PCT=VALUES(FG3_PCT),
    FTM=VALUES(FTM),
    FTA=VALUES(FTA),
    FT_PCT=VALUES(FT_PCT),
    OREB=VALUES(OREB),
    DREB=VALUES(DREB),
    REB=VALUES(REB),
    AST=VALUES(AST),
    STL=VALUES(STL),
    BLK=VALUES(BLK),
    TOV=VALUES(TOV),
    PF=VALUES(PF),
    PTS=VALUES(PTS)
"""

insert_player_advanced_data_query = """
INSERT INTO nba_advanced 
    (PLAYER_ID,
    PLAYER_NAME,
    GROUP_SET,
    GROUP_VALUE,
    TEAM_ID,
    TEAM_ABBREVIATION,
    MAX_GAME_DATE,
    GP,
    W,
    L,
    W_PCT,
    MIN,
    E_OFF_RATING,
    OFF_RATING,
    sp_work_OFF_RATING,
    E_DEF_RATING,
    DEF_RATING,
    sp_work_DEF_RATING,
    E_NET_RATING,
    NET_RATING,
    sp_work_NET_RATING,
    AST_PCT,
    AST_TO,
    AST_RATIO,
    OREB_PCT,
    DREB_PCT,
    REB_PCT,
    TM_TOV_PCT,
    E_TOV_PCT,
    EFG_PCT,
    TS_PCT,
    USG_PCT,
    E_USG_PCT,
    E_PACE,
    PACE,
    PACE_PER40,
    sp_work_PACE,
    PIE,
    POSS,
    FGM,
    FGA,
    FGM_PG,
    FGA_PG,
    FG_PCT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    PLAYER_ID=VALUES(PLAYER_ID),
    PLAYER_NAME=VALUES(PLAYER_NAME),
    GROUP_SET=VALUES(GROUP_SET),
    GROUP_VALUE=VALUES(GROUP_VALUE),
    TEAM_ID=VALUES(TEAM_ID),
    TEAM_ABBREVIATION=VALUES(TEAM_ABBREVIATION),
    MAX_GAME_DATE=VALUES(MAX_GAME_DATE),
    GP=VALUES(GP),
    W=VALUES(W),
    L=VALUES(L),
    W_PCT=VALUES(W_PCT),
    MIN=VALUES(MIN),
    E_OFF_RATING=VALUES(E_OFF_RATING),
    OFF_RATING=VALUES(OFF_RATING),
    sp_work_OFF_RATING=VALUES(sp_work_OFF_RATING),
    E_DEF_RATING=VALUES(E_DEF_RATING),
    DEF_RATING=VALUES(DEF_RATING),
    sp_work_DEF_RATING=VALUES(sp_work_DEF_RATING),
    E_NET_RATING=VALUES(E_NET_RATING),
    NET_RATING=VALUES(NET_RATING),
    sp_work_NET_RATING=VALUES(sp_work_NET_RATING),
    AST_PCT=VALUES(AST_PCT),
    AST_TO=VALUES(AST_TO),
    AST_RATIO=VALUES(AST_RATIO),
    OREB_PCT=VALUES(OREB_PCT),
    DREB_PCT=VALUES(DREB_PCT),
    REB_PCT=VALUES(REB_PCT),
    TM_TOV_PCT=VALUES(TM_TOV_PCT),
    E_TOV_PCT=VALUES(E_TOV_PCT),
    EFG_PCT=VALUES(EFG_PCT),
    TS_PCT=VALUES(TS_PCT),
    USG_PCT=VALUES(USG_PCT),
    E_USG_PCT=VALUES(E_USG_PCT),
    E_PACE=VALUES(E_PACE),
    PACE=VALUES(PACE),
    PACE_PER40=VALUES(PACE_PER40),
    sp_work_PACE=VALUES(sp_work_PACE),
    PIE=VALUES(PIE),
    POSS=VALUES(POSS),
    FGM=VALUES(FGM),
    FGA=VALUES(FGA),
    FGM_PG=VALUES(FGM_PG),
    FGA_PG=VALUES(FGA_PG),
    FG_PCT=VALUES(FG_PCT)
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

# Update nba_main table
try:
    cursor.executemany(insert_player_data_query, season_stats)
    connection.commit()
    print('Inserted data into nba_main successfully', season_stats)
except mysql.connector.Error as e:
    print('Could not insert player data:', e)
    
# Update nba_advanced table
try:
    cursor.executemany(insert_player_advanced_data_query, season_advanced_stats)
    connection.commit()
    print('Inserted data into nba_advanced successfully', season_advanced_stats)
except mysql.connector.Error as e:
    print('Could not insert player data into nba_advanced:', e)

connection.close()
