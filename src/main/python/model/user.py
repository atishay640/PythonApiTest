import json


class User:
    def __init__(self, id, email, first_name, last_name, avatar):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    @classmethod
    def from_json_or_dict(cls, user_json):
        if type(user_json) == dict:
            return cls(**user_json)
        else:
            user_dict = json.loads(user_json)
            return cls(**user_dict)