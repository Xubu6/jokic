// for getAllData call – force response to return only this schema
const schemaOptions = {
    schema: {
        response: {
            200: {
                type: 'array',
                data: {
                    type: 'object',
                    properties: {
                        id: { type: 'integer' },
                        name: { type: 'string' },
                        team: { type: 'string' },
                        age: { type: 'integer' },
                    }
                }
            }
        }
    }
}

module.exports = schemaOptions;