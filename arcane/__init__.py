from pyrogram import Client
import os
"""
ARCANEUSER = os.environ.get("ARCANEUSER", None)
SESSION = os.environ.get("SESSION", None)
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
"""

ARCANEUSER = 

SESSION = "BQBfjU9QslW-Z1rvir9yrCxWnSXNL0vdLI8iyyvkyKuBV43H6p2BsYXST3sl36MApkqCTmU1eZ6TqUqjG1mHFuv81RIxXN1aqBU1AVakogF1dk-HbZAr_1SH_qyGx3Uw9yHqDpH2db-lOzRmCpsC869ua-3Z_VfrnIsmvMnwRlVbmg3ndvUCKUyorFRckrp8vFm2iISB7peGCIujL4dJJURtlZcj8VLTY0Qpik-LKnBUMWe7PfU7-F9DZLyeelm-uAOBhrhpYjnVGVJBbHvW5xc8b5aYCRzogZ-D8GQe1R8NHIQEOM9Bo5KvDCLAAZKE2lppklBP62sJLnYeLcaq0hWNAAAAATNo8-oA"
API_ID = "10725796"
API_HASH = "4aac8a59da4dc6aabc6953be26640497"



bot = Client(session_name=SESSION,
             api_id=API_ID,
             api_hash=API_HASH,
             plugins=dict(root="{}/plugins".format(__name__)))

