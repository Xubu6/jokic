const fastify = require("fastify")({ logger: true });
const dataRoute = require("./routes/data");

fastify.register(dataRoute);

fastify.listen({ port: 3000, host: "0.0.0.0" }, (error) => {
  if (error) {
    fastify.log.error(error);
    process.exit(1);
  }
});
