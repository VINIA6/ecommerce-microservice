# Banco de dados em memória
fake_users_db = {
    "john": {
        "username": "john",
        "password": "hashedpassword",  # Isso deve ser um hash seguro
    }
}

def get_user(db, username: str):
    if username in db:
        return db[username]
    return None
