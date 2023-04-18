const routes = async (fastify) => {
  fastify.get("/data/player/id/:playerId", async (request, reply) => {
    const connection = await fastify.mysql.getConnection();
    const data = await connection.query(
      "SELECT player_id, player_name FROM nba_main WHERE player_id=?",
      request.params.playerId
    );
    const rows = data[0];
    if (rows) {
      return rows[0];
    } else {
      return `No Player With ID: ${request.params.playerId}`
    }
  });
  fastify.get("/data/player/name/:playerName", async (request, reply) => {
    const connection = await fastify.mysql.getConnection();
    const decodedPlayerName = request.params.playerName.replace('%20', ' ').replace('+', ' ');
    const data = await connection.query(
      "SELECT player_id, player_name FROM nba_main WHERE player_name=?",
      decodedPlayerName
    );
    const rows = data[0];
    if (rows) {
      return rows[0];
    } else {
      return `No Player With Name: ${decodedPlayerName}`
    }
  });
};

module.exports = routes;
