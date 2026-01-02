from fastapi import FastAPI
import os
from dotenv import load_dotenv

from models import TicketCreate, Ticket
from services import AIService

load_dotenv()

# if os.getenv()

aiservice = AIService()


tickets_db=[]
app = FastAPI(title="AI APP")

@app.get("/health")
def health():
    return("msg":"Backend is running")

@app.post("/tickets")
def tickets(ticket; Ticket):
    tickets_id = len(tickets_db) + 1

    prompt=f"""
you are a support agent, given a problem by user you should answer it
politely, clearly and consisely.

    user query:
    title:(ticket.title)
    decription:(ticket.description)

"""
    response=aiservice.generate_reply(prompt)
    ticket=Ticket(
        title=ticket,title,
        description=ticket.description,
        id=tickets_id,
        ai_reply=response)
    return {
        "msg":"Ticket created successfully",
        "ticket":new_ticket
    }

@app.get("/tickets")
def tickects():
    return tickets_db      