const { SELECT_ALL_RANK_VIEW } = require('../constants/queries');

async function getRankData(connection) {
    const data = await connection.query(SELECT_ALL_RANK_VIEW);
    return data;
}

module.exports = { getRankData }