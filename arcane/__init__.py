from pyrogram import Client
import os


ARCANEUSER = [
    5086015489, 5086015489
]

SESSION = ""
API_ID = "1998138"
API_HASH = "13862d4eadf08465eef9f56470d1ba10"

bot = Client(session_name=SESSION,
             api_id=API_ID,
             api_hash=API_HASH,
             plugins=dict(root="{}/plugins".format(__name__)))

