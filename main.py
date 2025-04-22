from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://surambaw.github.io"],  # Restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoBase(BaseModel):
    title: str
    completed: bool = False

class Todo(TodoBase):
    id: int

todos: List[Todo] = []
next_id = 1

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/filter/{completed}")
def filter_todos(completed: bool):
    return [todo for todo in todos if todo.completed == completed]

@app.post("/todos")
def create_todo(todo: TodoBase):
    global next_id
    new_todo = Todo(id=next_id, title=todo.title, completed=todo.completed)
    todos.append(new_todo)
    next_id += 1
    return new_todo

@app.put("/todos/{id}")
def update_todo(id: int, updated: Todo):
    for idx, t in enumerate(todos):
        if t.id == id:
            todos[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{id}")
def delete_todo(id: int):
    global todos
    todos = [t for t in todos if t.id != id]
    return Response(status_code=204)
