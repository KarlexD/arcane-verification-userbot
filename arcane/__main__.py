"""
ldb.create_db()
"""

from . import bot
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
    # app.run()


if __name__ == "__main__":
    main()
