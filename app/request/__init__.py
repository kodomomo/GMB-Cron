from requests import put

from app.config import SEC_CODE, SERVER_URL


def send_to_server(page_token: str):
    put(
        url=SERVER_URL,
        json={
            'v': page_token + SEC_CODE
        }
    )