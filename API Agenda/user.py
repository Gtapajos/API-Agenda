from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

USER = {
    "1000": {
        "user_name": "Caio Rolando da Rocha",
        "user_id": "1000",
        "timestamp": get_timestamp(),
        "events": []
    },
    "2000": {
        "user_name": "Jucimar Maia da Silva Jr",
        "user_id": "2000",
        "timestamp": get_timestamp(),
        "events": []
    },
    "3000": {
        "user_name": "Guilherme Correia Tapajos Araujo",
        "user_id": "3000",
        "timestamp": get_timestamp(),
        "events": []
    }
}

def read_all():
    return list(USER.values())

def create(user):
    if not user["user_id"] in USER:
        USER[user["user_id"]] = {
            "user_id": user["user_id"],
            "user_name": user["user_name"],
            "timestamp": get_timestamp(),
            "events": []
        }
    return list(USER.values())

def read_one(user_id):
    if user_id in USER:
        return USER[user_id]
    else:
        abort(
            404, f"Person with ID {user_id} not found"
        )

def delete(user_id):
    if user_id in USER:
        del USER[user_id]
        return make_response("", 204)
    else:
        abort(
            404, f"Person with ID {user_id} not found"
        )

