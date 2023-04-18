const routes = async (fastify) => {
  fastify.get("/data/all", async (req, reply) => {
    const connection = await fastify.mysql.getConnection();
    const data = await connection.query("SELECT * FROM main_view");
    connection.release();
    return data;
  });
};

module.exports = routes;
