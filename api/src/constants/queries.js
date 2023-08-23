const SELECT_ALL_MAIN_VIEW = "SELECT * FROM main_view";

const SELECT_ALL_RANK_VIEW = "SELECT * FROM main_view";

const FIND_PLAYER_BY_ID = "SELECT player_id, player_name FROM nba_main WHERE player_id=?";

const FIND_PLAYER_BY_NAME = "SELECT player_id, player_name FROM nba_main WHERE player_name=?";

module.exports = {
    SELECT_ALL_MAIN_VIEW,
    SELECT_ALL_RANK_VIEW,
    FIND_PLAYER_BY_ID,
    FIND_PLAYER_BY_NAME
}