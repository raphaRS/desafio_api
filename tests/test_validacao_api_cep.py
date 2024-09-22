import requests

url="https://viacep.com.br/ws/06814010/json"

def test_valida_logradouro():
    req_url = requests.get(url)
    req_json = req_url.json()['logradouro']
    print(req_json)
    assert req_json == 'Estrada São Marcos'
    assert req_url.status_code == 200

def test_valida_ddd():
    req_url = requests.get(url)
    req_json = req_url.json()['ddd']
    assert req_json == '11'
    assert req_url.status_code == 200
    