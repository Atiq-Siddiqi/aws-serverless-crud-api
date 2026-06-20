import boto3
import json

print('Loading function')

def lambda_handler(event, context):
    """
    Dynamically maps operations to handle CRUD transactions over HTTP.
    Expected Payload format:
    {
        "operation": "create"|"read"|"update"|"delete"|"list"|"echo"|"ping",
        "tableName": "string",
        "payload": {}
    }
    """
    operation = event['operation']

    if 'tableName' in event:
        dynamo = boto3.resource('dynamodb').Table(event['tableName'])

    # Dynamic routing table
    operations = {
        'create': lambda x: dynamo.put_item(**x),
        'read': lambda x: dynamo.get_item(**x),
        'update': lambda x: dynamo.update_item(**x),
        'delete': lambda x: dynamo.delete_item(**x),
        'list': lambda x: dynamo.scan(**x),
        'echo': lambda x: x,
        'ping': lambda x: 'pong'
    }

    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError(f'Unrecognized operation "{operation}"')
