# mid_term
Objectives: Build backend for a ticket system using FastAPI and SQL Alchemy and SQLite3
Database schema:

#tickets:
|Field|Technical Detail|Type|
|ticket_id|Default value(uuid4) (primary key)|UUID4|
|ticket_name|Not Nullable|str|
|ticket_description|Not Nullable|str|
|created_time|Default value (datetime now)|datetime|
|updated_time|Default value (datetime now) (only use when edit)|datetime, None|
|status_name|Only New, On-going, Done|str|
|assignee_id|Foreign key with owner_id|UUID4|
|assigner_id |Foreign key with owner_id|UUID4|
|category_name|Nullable|str|
|priority_name|Only Low, Medium, High|str|
#owner:
owner_id|Default value(uuid4) (primary key)|UUID4|
owner_name|Not Nullable|str|
owner_mail|Not Nullable|str|



Specification:
- Create database using Sqlite3 and SQL Alchemy model
- CRUD using SQL Alchemy functions
- Create API using FastAPI for this function:
	+ Create tickets
	+ Get tickets (list all ticket if no filter parameter passed), if has, filter ticket by:
		- ticket_name: list all tickets which ticket_name contain an input string
		- owner: list all tickets which belong to this owner_name or owner_mail
		- category_name: list all tickets which has category_name equal to input string
		- API has ability to return records if 1 or all filters are selected.
	+ Update ticket details (change ticket info except ticket_id, and re-update the updated_time)
	+ Delete ticket: Delete a ticket by ID. Can delete multiple tickets at once if user pass a list to API. Ex: {“ticket_ids”: [“1”, “2”, “3”]}

Note: API Path name and method are optional. You can create any paths and methods if you find it’s suitable. Please write comments in your code and explain what this function/class does. All requests must be in JSON type.
