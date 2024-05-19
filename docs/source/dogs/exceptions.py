from fastapi import HTTPException, status

class collar_collision(HTTPException):
	def __init__(self):
		super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Dog with this collar already registered")

class collar_not_found(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Collar doesn't exist")


class ip_collision(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Collar with this ip already registered")

class invalid_ip(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid IP")

class dog_not_found(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Dog doesn't exist")
