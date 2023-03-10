from requests import get

from app.config import APP_ID, APP_SECRET, REDIRECT_URI


def get_token(code: str):
    return get(
        url="https://graph.facebook.com/v16.0/oauth/access_token",
        params=dict(
            client_id=APP_ID,
            client_secret=APP_SECRET,
            redirect_uri=REDIRECT_URI,
            code=code
        )
    ).json()


def get_page_token(user_token):
    return get(
        f'https://graph.facebook.com/100828842473374?fields=access_token&access_token={user_token}'
    ).json()
