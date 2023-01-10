phone_number_id = "100849862852277" # Phone number ID provided
access_token = "EAAJBCKybq6QBABHjmeQaPr0BkgFdMf2nCWZAi6di2e4mrrjXtF2ZCzzuHjuefD4pmjfBlz99Be6ovwxH6TO7q46ZC0zNOZAM6yUEkORxvpRsTWOgrxlG4GXqMT3zZC6i1a8osZBldiJWjIBFINffsov1k8JLRasYeICPeV9dz9zbHaKBc5yYN1alLoh9vDUuTLfL6U62zTAQRQPHsDniVt" # Your temporary access token
recipient_phone_number = "+6285342805673" # Your own phone number

url = f"https://graph.facebook.com/v13.0/{phone_number_id}/messages"
headers = {
    "Authorization": f"Bearer {access_token}",
    'Content-Type': 'application/json'
}
build_number = '2022.1'
build_author = 'Ben Keen'

msg_body_params = [
        {
            "type": "text",
            "text": build_number
        },
        {
            "type": "text",
            "text": build_author
        }
]
data = {
    'messaging_product': 'whatsapp',
    'to': recipient_phone_number,
    'type': 'template',
    'template': {
        'name': 'build_pipeline_failure',
        'language': {
            'code': 'en'
        },
        'components': [
            {
                'type': 'body',
                'parameters': msg_body_params
            }
                
        ]
    }
}

import json
import requests

response = requests.post(
    url,
    headers=headers,
    data=json.dumps(data)
)

print(response.ok)