import uvicorn
from fastapi import FastAPI
from workspace.controllers.check_controller import check_controller
from workspace.controllers.greet_controller import greet_controller
from starlette.middleware.cors import CORSMiddleware

workspace = FastAPI()
workspace.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

workspace.include_router(check_controller, prefix="/")
workspace.include_router(greet_controller, prefix="/")

# start the server using python main.py to enable live reload
if __name__ == "__main__":
    uvicorn.run("main:workspace", host="0.0.0.0", port=8080, reload=True)
