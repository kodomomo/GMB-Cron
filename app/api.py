from fastapi import FastAPI

from app.config import STATE
from app.request import send_to_server
from app.request.token import get_token, get_page_token

app = FastAPI()


@app.get('/facebook/redirect')
def receive_code(code: str, state: str):

    assert STATE == state, 'STATE IS NOT MATCHED'

    user_token = get_token(code)['access_token']

    page_token = get_page_token(user_token)['access_token']

    send_to_server(page_token)