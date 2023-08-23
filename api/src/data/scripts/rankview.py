# Rankings for each stat for each player

import os
import mysql.connector

update_rank_view_query = """
CREATE OR REPLACE VIEW rank_view AS
SELECT player_name,
       team_abbreviation,
       min_rank,
       umbinaam_rank,
       net_rating_rank,
       pie_rank,
       per_rank,
       ws_per_48_rank,
       bpm_rank,
       vorp_rank,
       epm_rank,
       e_wins_rank,
       lebron_rank,
       bbi_war_rank,
       rpm_rank,
       rpm_wins_rank,
       wpa_rank,
       k_wpa_rank,
       raptor_rank,
       raptor_war_rank,
       fic_rank,
       dpm_rank,
       (umbinaam_rank + net_rating_rank + pie_rank + per_rank + ws_per_48_rank + bpm_rank + vorp_rank + epm_rank + e_wins_rank + lebron_rank + bbi_war_rank + rpm_rank + rpm_wins_rank + wpa_rank + k_wpa_rank + raptor_rank + raptor_war_rank + fic_rank + dpm_rank) / 19 AS average_rank
FROM (
  SELECT player_name,
         team_abbreviation,
         RANK() OVER (ORDER BY min DESC) AS min_rank,
         RANK() OVER (ORDER BY umbinaam DESC) AS umbinaam_rank,
         RANK() OVER (ORDER BY net_rating DESC) AS net_rating_rank,
         RANK() OVER (ORDER BY pie DESC) AS pie_rank,
         RANK() OVER (ORDER BY per DESC) AS per_rank,
         RANK() OVER (ORDER BY ws_per_48 DESC) AS ws_per_48_rank,
         RANK() OVER (ORDER BY bpm DESC) AS bpm_rank,
         RANK() OVER (ORDER BY vorp DESC) AS vorp_rank,
         RANK() OVER (ORDER BY epm DESC) AS epm_rank,
         RANK() OVER (ORDER BY e_wins DESC) AS e_wins_rank,
         RANK() OVER (ORDER BY lebron DESC) AS lebron_rank,
         RANK() OVER (ORDER BY bbi_war DESC) AS bbi_war_rank,
         RANK() OVER (ORDER BY rpm DESC) AS rpm_rank,
         RANK() OVER (ORDER BY rpm_wins DESC) AS rpm_wins_rank,
         RANK() OVER (ORDER BY wpa DESC) AS wpa_rank,
         RANK() OVER (ORDER BY k_wpa DESC) AS k_wpa_rank,
         RANK() OVER (ORDER BY raptor DESC) AS raptor_rank,
         RANK() OVER (ORDER BY raptor_war DESC) AS raptor_war_rank,
         RANK() OVER (ORDER BY fic DESC) AS fic_rank,
         RANK() OVER (ORDER BY dpm DESC) AS dpm_rank
  FROM main_view
) AS ranks;
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
    cursor.execute(update_rank_view_query)
    print('Successfully updated rank_view!')
except mysql.connector.Error as e:
    print('Could not execute query:', e)

connection.close()
