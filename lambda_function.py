from app.request.auth import AutoLogin


def handler_event(event, context):
    auth = AutoLogin()
    auth.execute()