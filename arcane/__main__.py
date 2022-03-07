
from . import bot
from app import idb
import logging


logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)



def main():
    bot.run()
    ldb.create_db()
    # app.run()


if __name__ == "__main__":
    main()
