/* eslint-disable no-unused-vars */
const getNBAStats = require('./getNBAStats');
const getBBRefStats = require('./getBBRefStats');
const formatAllData = require('./formatAllData');

const getAllData = async () => {
    let data;

    // retrieve stats from NBA.com

    // retrieve stats from BBRef.com

    data = await getNBAStats();
    return data;
}

module.exports = getAllData;