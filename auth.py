def authenticate_user(username, password):
    """用户认证函数"""
    if not username or not password:
        return False
    if username == "admin" and password == "123456":
        return True
    return False
