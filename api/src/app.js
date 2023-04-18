require("dotenv").config();
const fastify = require("fastify")({ logger: true });
const dataRoute = require("./routes/data/all/get");
const playerRoute = require("./routes/data/player/get")

const buildServer = async () => {
  try {
    await fastify.register(require("@fastify/mysql"), {
      promise: true,
      connectionString: process.env.MYSQL_CONNECTION_STRING || "",
    });
    console.log("DB connection successful!");
  } catch (error) {
    console.log(error);
  }

  await fastify.register(dataRoute)
  await fastify.register(playerRoute)
  return fastify;
};

module.exports = { buildServer }
