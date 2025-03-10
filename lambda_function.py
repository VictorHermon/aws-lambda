import json
from logs import log

def lambda_handler(event, context):
    # TODO implement
    log('Inicio de registro de evento para validação')
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Fim')
    }
