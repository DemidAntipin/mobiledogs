from fastapi import HTTPException, status

class task_not_found(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Task doesn't exist")

class response_not_found(HTTPException):
        def __init__(self):
                super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Response doesn't exist")

