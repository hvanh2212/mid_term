from unicodedata import category
from fastapi import FastAPI
from sql_management import CURD_function
from pydantic import BaseModel
import uuid
# from pydantic import BaseModel as CategoryName
# from pydantic import BaseModel as DeleteID
# from pydantic import BaseModel as OwnerName
import json
from typing import Union

class Ticket_input(BaseModel):
    ticket_name : str
    ticket_description : str
    status_name : str
    assignee_id : str
    assigneer_id : str
    category_name : str
    priority_name : str


app = FastAPI()

@app.get("/owner")
async def owner():
    return CURD_function.select_owner()

@app.get("/ticket")
async def ticket():
    return CURD_function.select_ticket()

@app.post("/ticket")
async def create_ticket(ticket: Ticket_input):
    return CURD_function.create_ticket(ticket)

# class filter_ticket_category(BaseModel):
#     category_name: str
# @app.post("/ticket/{category_name}")
# async def filter_ticket_by_category(ticket_filter_category: filter_ticket_category):
#     return CURD_function.filter_ticket_by_category(ticket_filter_category.category_name)


# # class Item(BaseModel):
# #     __root__: Union [filter_ticket_name, filter_ticket, delete_ticket]

# class filter_ticket_name(BaseModel):
#     ticket_name: str
# @app.post("/ticket/{ticket_name}")
# async def filter_ticket_by_name(ticket_name_filter: filter_ticket_name):
#     return CURD_function.filter_ticket(ticket_name_filter.ticket_name)

class Ticket_update(Ticket_input):
    ticket_id : str

@app.put("/ticket/{ticket_id}")
async def update_ticket(ticket: Ticket_update):
    return CURD_function.update_ticket(ticket)

class delete_ticket(BaseModel):
    tickets_id: list
@app.delete("/ticket/{ticket_id}")
async def delete_ticket_id(ticket_filter: delete_ticket):
    return CURD_function.delete_ticket(ticket_filter.tickets_id)
