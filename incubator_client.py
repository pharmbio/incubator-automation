#!/usr/bin/env python3
import sys
import logging
from Incubator import Incubator

if __name__ == "__main__":

    # Init logging
    logging.basicConfig(level=logging.DEBUG)

    if len(sys.argv) > 1:

      incu = Incubator()

      if sys.argv[1] == "open":
        retval = incu.open()
        logging.info(retval)
      if sys.argv[1] == "close":
        retval = incu.close()
        logging.info(retval)
      if sys.argv[1] == "is_open":
        retval = incu.is_open()
        logging.info(retval)
      if sys.argv[1] == "is_closed":
        retval = incu.is_closed()
        logging.info(retval)
      if sys.argv[1] == "get":
        feedback = incu.get_position()
        logging.info("Feedback:" + str(feedback))
      if sys.argv[1] == "set":
        incu.set_position(int(sys.argv[2]))
