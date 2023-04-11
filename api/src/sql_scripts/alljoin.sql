SELECT nba.player_id, nba.player_name, nba.team_abbreviation, nbaa.net_rating, nbaa.pie, bbref.per, bbref.ws_per_48, bbref.bpm, bbref.vorp, epm.epm, epm.e_wins, lebron.lebron, lebron.bbi_war, rpm.rpm, rpm.rpm_wins, wpa.wpa, wpa.k_wpa, raptor.raptor, raptor.raptor_war
FROM nba_main AS nba
LEFT JOIN nba_advanced AS nbaa ON nbaa.player_name=nba.player_name
LEFT JOIN bbref ON bbref.player_name=nba.player_name
LEFT JOIN epm ON epm.player_name=nba.player_name
LEFT JOIN lebron ON lebron.player_name=nba.player_name
LEFT JOIN rpm ON rpm.player_name=nba.player_name
LEFT JOIN wpa ON wpa.player_name=nba.player_name
LEFT JOIN raptor ON raptor.player_name=nba.player_name
-- WHERE nba.min > 300
ORDER BY bpm DESC;

-- SELECT * FROM raptor
-- Robert Williams III
-- Robert Williams III
-- Robert Williams III
-- Robert Williams III
-- Robert Williams (bbref)


