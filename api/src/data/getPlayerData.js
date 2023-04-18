const {
  FIND_PLAYER_BY_ID,
  FIND_PLAYER_BY_NAME,
} = require("../constants/queries");

async function getPlayerById(id, connection) {
  const data = await connection.query(FIND_PLAYER_BY_ID, id);
  const rows = data[0];
  if (rows) {
    return rows[0];
  } else {
    return { "No Player With ID": id };
  }
}

async function getPlayerByName(name, connection) {
  const data = await connection.query(FIND_PLAYER_BY_NAME, name);
  const rows = data[0];
  if (rows) {
    return rows[0];
  } else {
    return { "No Player With Name": name };
  }
}

module.exports = {
  getPlayerById,
  getPlayerByName,
};
