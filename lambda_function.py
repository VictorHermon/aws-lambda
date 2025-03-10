import json
from logs import log

def lambda_handler(event, context):
    # TODO implement
    log('Inicio de registro de evento')
    log('Pra ver se tá indo o github actions')
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Fim')
    }
