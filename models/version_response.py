from pydantic import BaseModel

class VersionResponse(BaseModel):
    version: str | None = None

