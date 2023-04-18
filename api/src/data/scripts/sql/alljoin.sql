-- SELECT ROW_NUMBER() OVER(ORDER BY umbinaam.umbinaam DESC) AS rk, nba.player_id, nba.player_name, nba.team_abbreviation, umbinaam.umbinaam, nbaa.net_rating, nbaa.pie, bbref.per, bbref.ws_per_48, bbref.bpm, bbref.vorp, epm.epm, epm.e_wins, lebron.lebron, lebron.bbi_war, rpm.rpm, rpm.rpm_wins, wpa.wpa, wpa.k_wpa, raptor.raptor, raptor.raptor_war, fic.ts, fic.fic, dpm.dpm
-- FROM nba_main AS nba
-- LEFT JOIN nba_advanced AS nbaa ON nbaa.player_name=nba.player_name
-- LEFT JOIN bbref ON bbref.player_name=nba.player_name
-- LEFT JOIN epm ON epm.player_name=nba.player_name
-- LEFT JOIN lebron ON lebron.player_name=nba.player_name
-- LEFT JOIN rpm ON rpm.player_name=nba.player_name
-- LEFT JOIN wpa ON wpa.player_name=nba.player_name
-- LEFT JOIN raptor ON raptor.player_name=nba.player_name
-- LEFT JOIN fic ON fic.player_name=nba.player_name
-- LEFT JOIN dpm ON dpm.player_name=nba.player_name
-- LEFT JOIN umbinaam ON umbinaam.player_name=nba.player_name
-- WHERE nba.min > 1100;

-- SELECT ROW_NUMBER() OVER(ORDER BY umbinaam DESC) AS rk, umbinaam.player_name AS Name, nba_main.min AS MP, umbinaam.umbinaam
-- FROM umbinaam
-- JOIN nba_main ON (nba_main.player_name=umbinaam.player_name)
-- WHERE nba_main.min > 100;

SELECT * FROM main_view;

-- SELECT * FROM raptor


