import json
from logs import log
from os import environ

def lambda_handler(event, context):
    # TODO implement
    log('Inicio de registro de evento')
    log(f"ENV: {environ['AMBIENTE']}")
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Fim')
    }
