const { buildServer } = require("./app");

const start = async () => {
  const server = await buildServer();

  // register routes
  server.register(require("./routes"), { prefix: "api" });
  try {
    server.listen({ port: 8080, host: "0.0.0.0" });
  } catch (error) {
    console.error(error);
    server.log.error(`Failed to start server ${error}`);
    process.exit(1);
  }
};
start();

module.exports = { start };
