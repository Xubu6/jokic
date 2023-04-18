const { getAllData } = require('../data/getAllData');

const routes = async (fastify) => {
  fastify.get("/", async (req, reply) => {
    const connection = await fastify.mysql.getConnection();
    const data = await getAllData(connection);
    return data;
  });
};

module.exports = routes;
