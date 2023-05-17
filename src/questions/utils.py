import json

import requests
from fastapi import HTTPException


def get_response(questions_num: int) -> json:
    try:
        response = requests.get(
            f'https://jservice.io/api/random?count={questions_num}'
            ).json()
        return response
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503,
                            detail='ConnectionError')
