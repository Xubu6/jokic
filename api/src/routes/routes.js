const get = require('./get');
const getAllDataOptions = require('../data/schema');

const routes = async (fastify) =>{
    fastify.get('/data', getAllDataOptions, get)
}

module.exports = routes;