require('dotenv').config();
const fastify = require("fastify")({ logger: true });
const dataRoute = require("./routes/data");

try {
  fastify.register(
    require("@fastify/mysql"),
    {
      promise: true,
      connectionString: process.env.MYSQL_CONNECTION_STRING || '',
    }
  );
  console.log('DB connection successful!')
} catch (error) {
  console.log(error)
}

fastify.register(dataRoute);

fastify.listen({ port: 3000, host: "0.0.0.0" }, (error) => {
  if (error) {
    fastify.log.error(error);
    process.exit(1);
  }
});
