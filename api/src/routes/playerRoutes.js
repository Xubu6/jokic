const { getPlayerById, getPlayerByName } = require('../data/getPlayerData')

const routes = async (fastify) => {
  fastify.get("/id/:playerId", async (request, reply) => {
    const connection = await fastify.mysql.getConnection();
    const data = await getPlayerById(request.params.playerId, connection);
    return data;
  });
  fastify.get("/name/:playerName", async (request, reply) => {
    const connection = await fastify.mysql.getConnection();
    const decodedPlayerName = request.params.playerName.replace('%20', ' ').replace('+', ' ');
    const data = await getPlayerByName(decodedPlayerName, connection);
    return data;
  });
};

module.exports = routes;
