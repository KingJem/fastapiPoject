import orjson
from fastapi import APIRouter
from starlette.responses import JSONResponse

from apps.todoList.models import todoListPydantic, TodoList
from fastapi import status

todo = APIRouter()
app = todo


@app.post('/create', response_model=todoListPydantic, status_code=status.HTTP_201_CREATED)
async def create_todo(content: todoListPydantic) -> todoListPydantic:
    content_dict = orjson.loads(content.json())
    instance = await TodoList.create(**content_dict)
    return await todoListPydantic.from_tortoise_orm(instance)
