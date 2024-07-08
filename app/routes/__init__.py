from pydantic import BaseModel
from fastapi.responses import JSONResponse


class SuccessResponse(BaseModel):
    success: bool = True
    data: dict | list | None
    msg: str = "Action Successful"
    status_code: int = 200

    def to_response(self):
        return JSONResponse(status_code=self.status_code, content={
            "success": self.success,
            "data": self.data,
            "message": self.msg
        })


class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    msg: str = "Server Error"
    status_code: int = 500

    def to_response(self):
        return JSONResponse(status_code=self.status_code, content={
            "success": self.success,
            "error": self.error,
            "message": self.msg
        })
