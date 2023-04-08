const getAllData = require('../data/getAllData');

async function fetchAllStats(request, reply) {
    try {
        return await getAllData();
    } catch (error) {
        reply.code(error.statusCode || 500);
        return { resuls : error.message || 'getAllData call failed'};
    }
};

module.exports = fetchAllStats;


