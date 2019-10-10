import json
import datetime
import uuid


def handler(event, context):
    data = {
        'uuid': uuid.uuid4().__str__(),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
