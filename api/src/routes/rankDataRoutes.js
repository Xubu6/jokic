const { getRankData } = require('../data/getRankData');

const routes = async (fastify) => {
  fastify.get("/", async (req, reply) => {
    const connection = await fastify.mysql.getConnection();
    const data = await getRankData(connection);
    return data;
  });
};

module.exports = routes;
