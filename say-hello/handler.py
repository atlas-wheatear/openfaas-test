def handle(event, context):
    return {
        'body': {
            'hello': 'world'
        },
        'statusCode': 400
    }
