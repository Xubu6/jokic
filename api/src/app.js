require("dotenv").config();
const fastify = require("fastify")({ logger: true });

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

  return fastify;
};

module.exports = { buildServer }
