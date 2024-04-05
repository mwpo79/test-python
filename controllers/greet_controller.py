from fastapi import APIRouter
from models.say_hello_response import SayHelloResponse

greet_controller = APIRouter()

@greet_controller.get("/sayHello")
async def say_hello(name: str):
    return SayHelloResponse(message=f"Hello, {name}!")

