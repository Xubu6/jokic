module.exports = async function (fastify) {
    fastify.register(require('./allDataRoutes'), { prefix: '/data/all' });
    fastify.register(require('./playerRoutes'), { prefix: '/data/player' });
  };