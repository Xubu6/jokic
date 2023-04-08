const fastify = require("fastify")({ logger: true });
const routes = require("./routes/routes");

fastify.register(routes);

fastify.listen({ port: 3000, host: "0.0.0.0" }, (error) => {
  if (error) {
    fastify.log.error("App failed to initialize: ", error);
    process.exit(1);
  }
});
