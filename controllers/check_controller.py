import os
from fastapi import APIRouter, HTTPException
from workspace.models.version_response import VersionResponse
from workspace.models.health_response import HealthResponse

check_controller = APIRouter()

@check_controller.get("/getCurrVersion")
async def get_curr_version():
    version = os.getenv("VERSION")
    if version is None:
        version = "0.0.0.0"

    return VersionResponse(version=version)

@check_controller.get("/healthCheck")
async def health_check(type_check: str = "liveness"):
    env_key = f"HEALTHCHECK_{type_check.upper()}"
    health_check_env = os.getenv(env_key)

    status = 200
    default_message = "Status: SERVING"

    if health_check_env is not None:
        status = int(health_check_env)
        default_message = "Status: NOT_SERVING" if status != 200 else "Status: SERVING"

    if status != 200:
        raise HTTPException(status_code=status, detail=default_message)

    return HealthResponse(message=default_message)

