from fastapi import HTTPException, status

class email_collision(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already registered")

class phone_collision(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this phone already registrated")


class name_collision(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this name already registrated")

class invalid_login(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect name or password")

class invalid_token(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")

class user_not_found(HTTPException):
	def __init__(self):
		super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="User doesn't exist")
