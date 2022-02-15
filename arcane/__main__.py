from . import bot
import logging
from python-idb import ldb
import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)



def main():
    ldb.create_db()
    bot.run()
    # app.run()


if __name__ == "__main__":
    main()
