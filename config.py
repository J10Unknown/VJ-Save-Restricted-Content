import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24874103"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f14cc27d3ae5fbe0e26417f917246814")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://unknown987person:SDwmnmgjgrDoOTx9@cluster0.31390.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
