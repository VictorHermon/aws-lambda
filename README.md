# aws-lambda

Estudo de deploy contínuo de uma função **AWS Lambda** em Python com **GitHub Actions**.

## Como funciona

- `lambda_function.py`: handler que registra o evento recebido, lê a variável de ambiente `AMBIENTE` e responde com status 200.
- `logs.py`: função auxiliar de log.
- [`main.yml`](.github/workflows/main.yml): a cada push, o workflow compacta os arquivos `.py` e atualiza o código da função na AWS.

## Configuração

O workflow usa estes secrets do repositório:

| Secret | Uso |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | Credencial de acesso à AWS |
| `AWS_SECRET_ACCESS_KEY` | Credencial de acesso à AWS |
| `AWS_REGION` | Região da função |

A função na AWS precisa da variável de ambiente `AMBIENTE` (por exemplo, `dev` ou `prod`).

## Tecnologias

Python · AWS Lambda · GitHub Actions
