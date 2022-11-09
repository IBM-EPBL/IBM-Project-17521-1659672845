def validate(roles, data):
    if roles is None:
        return True
    for role in roles:
        print(role)
        print(data)
        print(role in data)
        if role not in data:
            return False
    return True
