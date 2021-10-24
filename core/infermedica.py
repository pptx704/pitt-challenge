import requests
import json
from os import path

with open(path.join(path.dirname(__file__), 'secrets.json'), 'r') as secret:
    data = json.loads(secret.read())
    headers = {
        'App-Id': data.get('App-Id'),
        'App-Key': data.get('App-Key'),
        'Content-Type': 'application/json',
    }


def init_req_to_inf(data_dict):
    response = requests.post(
        'https://api.infermedica.com/v3/parse', 
        headers=headers, 
        json=data_dict
    )

    return response.json()

def diagnosis_req_to_if(data_dict):
    data_dict['extras'] = {
        "disable_groups": True
    }

    print("Data going to diagnosis api", data_dict)

    response = requests.post(
        "https://api.infermedica.com/v3/diagnosis",
        headers=headers,
        json=data_dict
    )
    print("data coming from diagnosis api", response.json())
    return response.json()

def get_specialist(data_dict):
    print("Data going to specialist api", data_dict)
    response = requests.post(
        "https://api.infermedica.com/v3/recommend_specialist",
        headers=headers,
        json=data_dict
    )
    print("Specialist:", response.json())
    return response.json()

def init_inf(age, sex, text):
    data_dict = {
        "age": {
            "value": age
        },
        "sex": sex,
        "text": text
    }

    response = init_req_to_inf(data_dict)


    evidences = []
    for evidence in response['mentions']:
        evidences.append({
            'id': evidence['id'],
            'choice_id': evidence['choice_id'],
            'source': 'initial'
        })

    data_dict.pop("text")
    data_dict['evidence'] = evidences


    return data_dict


