# You can later connect this to a real database
fake_user = {
    "username": "ankul",
    "password": "12345",
    "user_id": 1
}

def get_user_by_username(username):
    if username == fake_user["username"]:
        return fake_user
    return None
