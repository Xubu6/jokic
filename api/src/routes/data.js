require('dotenv').config();

const dataRoute = async (fastify) =>{
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
      
      fastify.get('/data', async (req, reply) => {
        const connection = await fastify.mysql.getConnection()
        const data = await connection.query(
          'SELECT * FROM main_view',
        )
        connection.release()
        return data
      })
}

module.exports = dataRoute;