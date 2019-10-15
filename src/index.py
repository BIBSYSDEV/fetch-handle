import datetime
import json
import uuid

import validators


def handler(event, context):
    url = json.loads(event['body']).get('url')
    if url is None:
        raise ValueError("No value was passed for URL")
    if not validators.url(url):
        raise ValueError('Value passed as URL is not a URL')

    data = {
        'uuid': uuid.uuid4().__str__(),
        'inputUrl': url,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }

    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {'Content-Type': 'application/json'}
    }
