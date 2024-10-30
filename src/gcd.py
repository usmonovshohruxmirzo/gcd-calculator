import json

def gdc(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

def get_api_key_from_config():
    with open('config.json') as f:
        config = json.load(f)
        return config['api_key']

api_key = get_api_key_from_env()