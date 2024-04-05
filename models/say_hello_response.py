from pydantic import BaseModel

class SayHelloResponse(BaseModel):
    message: str | None = None

