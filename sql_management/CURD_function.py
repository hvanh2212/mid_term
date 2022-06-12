from unicodedata import category
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json
import uuid

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owner'
    owner_id = Column(String, primary_key=True, autoincrement=True)
    owner_name = Column(String, nullable = False)
    owner_mail = Column(String, nullable = False)

    def dict(self):
        return{
            "owner_id" : self.owner_id,
            "owner_name" : self.owner_name,
            "owner_mail" : self.owner_mail
        }

class Ticket(Base):
    __tablename__ = 'tickets'
    ticket_id = Column(String, primary_key=True, autoincrement=True)
    ticket_name = Column(String, nullable = False)
    ticket_description = Column(String, nullable = False)
    created_time = Column(String, default = str(datetime.now()))
    update_time = Column(String, default = str(datetime.now()))
    status_name = Column(String)
    assignee_id = Column(String, ForeignKey('owner.owner_id'))
    assigneer_id = Column(String, ForeignKey('owner.owner_id'))
    category_name = Column(String, nullable = False)
    priority_name = Column(String)

    def dict(self):
        return{
            "ticket_id" : self.ticket_id,
            "ticket_name" : self.ticket_name,
            "ticket_description" : self.ticket_description,
            "created_time" : self.created_time,
            "update_time" : self.update_time,
            "status_name" : self.status_name,
            "assignee_id" : self.assignee_id,
            "assigneer_id" : self.assigneer_id,
            "category_name" : self.category_name,
            "priority_name" : self.priority_name
        }


def create_session():
    engine = create_engine('sqlite:///./models/ticket_system.db')
    # create session
    Session = sessionmaker(bind=engine)
    return Session()

def json_output(tickets):
    list_dict = []
    
    # add dict to the list
    for ticket in tickets:
        list_dict.append(dict(ticket.dict()))
    # convert a list to json
    string_json = json.dumps(list_dict)

    #print(string_json)

    # parse a valid JSON string and convert it to dict
    return json.loads(string_json) 

def create_owner():
    session = create_session()

    owner1 = Owner(owner_id=str(uuid.uuid4()), owner_name='Mary', owner_mail='mary@gmail.com')
    owner2 = Owner(owner_id=str(uuid.uuid4()), owner_name='Nick', owner_mail='nick@gmail.com')
    session.add(owner1)
    session.add(owner2)
    session.commit()


def create_ticket(ticket_json):
    session = create_session()

    ticket_created = Ticket(ticket_id = str(uuid.uuid4()),
                            ticket_name = ticket_json.ticket_name,
                            ticket_description = ticket_json.ticket_description,
                            update_time = "",
                            status_name = ticket_json.status_name,
                            assignee_id = ticket_json.assignee_id,
                            assigneer_id = ticket_json.assigneer_id,
                            category_name = ticket_json.category_name,
                            priority_name = ticket_json.priority_name)

    session.add(ticket_created)
    session.commit()

def select_owner():
    """
    select all customer from Customers
    """
    session = create_session()
    # SELECT * FROM Customers;
    owners = session.query(Owner).all()

    list_dict = []
    
    # add dict to the list
    for owner in owners:
        list_dict.append(dict(owner.dict()))
    # convert a list to json
    string_json = json.dumps(list_dict)

    # parse a valid JSON string and convert it to dict
    return json.loads(string_json) 

def select_ticket():
    """
    select all customer from Customers
    """
    session = create_session()
    # SELECT * FROM Customers;
    tickets = session.query(Ticket).all()

    return json_output(tickets)


def filter_ticket(ticket_name_filter):
    session = create_session()
    tickets = session.query(Ticket).filter(Ticket.ticket_name == ticket_name_filter).all()
    
    return json_output(tickets)

def filter_ticket_by_category(category_filter):
    session = create_session()
    tickets = session.query(Ticket).filter(Ticket.category_name == category_filter).all()

    return json_output(tickets)


def delete_ticket(tickets_id):
    session = create_session()
    # filter the customer has ticket_id 
    list_dict = []
    for ticket_id_filter in tickets_id:
        ticket = session.query(Ticket).filter(Ticket.ticket_id == ticket_id_filter).first()
        list_dict.append(dict(ticket.dict()))
        #delete the customer 
        session.delete(ticket)
        session.commit()
    string_json = json.dumps(list_dict)
    return json.loads(string_json) 

# def update_ticket(ticket_id_filter):
#     session = create_session()
#     # filter the customer has ticket_id 
#     list_dict = []
#     ticket = session.query(Ticket).filter(Ticket.ticket_id == ticket_id_filter).first()
#     list_dict.append(dict(ticket.dict()))
#         #delete the customer 
#     session.update({"status_name":"On-going"})
#     session.commit()
#     string_json = json.dumps(list_dict)
#     return json.loads(string_json) 

def update_ticket(ticket_json):
    session = create_session()
    list_dict = []

    ticket = session.query(Ticket).filter(Ticket.ticket_id == ticket_json.ticket_id).first()

    #ticket.dict().update(ticket_json)

    ticket.ticket_name = ticket_json.ticket_name
    ticket.ticket_description = ticket_json.ticket_description
    ticket.update_time = str(datetime.now())
    ticket.status_name = ticket_json.status_name
    ticket.assignee_id = ticket_json.assignee_id
    ticket.assigneer_id = ticket_json.assigneer_id
    ticket.category_name = ticket_json.category_name
    ticket.priority_name = ticket_json.priority_name

    session.commit()