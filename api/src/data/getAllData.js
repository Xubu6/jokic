const { SELECT_ALL_MAIN_VIEW } = require('../constants/queries');

async function getAllData(connection) {
    const data = await connection.query(SELECT_ALL_MAIN_VIEW);
    return data;
}

module.exports = { getAllData }