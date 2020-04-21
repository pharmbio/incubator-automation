#!/usr/bin/env python3
import lac
import sys
import logging

# 46mm/s (no load)

class Incubator:

    def open(self):
        self.set_position(1010)

    def close(self):
        self.set_position(5)

    def is_open(self):
        position = self.get_position()
        if(position > 1000):
            return True
        else:
            return False

    def is_closed(self):
        position = self.get_position()
        if(position < 10):
            return True
        else:
            return False

    def set_position(self, position):
        # 0 = 0, 1023 = 200mm 5 pos 1mm
        actu = lac.LAC()
        actu.set_position(position)

    def set_retract_limit(self, position):
        actu = lac.LAC()
        actu.set_retract_limit(position)

    def get_position(self):
        # 0 = 0, 1023 = 200mm 5 pos 1mm
        actu = lac.LAC()
        position = actu.get_feedback()
        return position

if __name__ == "__main__":

    # Init logging
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Before start server")

    logging.info(sys.argv[1:])
    logging.info(sys.argv[1])

    if len(sys.argv) > 1:

      incu = Incubator()

      if sys.argv[1] == "open":
        retval = open()
        logging.info(retval)
      if sys.argv[1] == "close":
        retval = close()
        logging.info(retval)
      if sys.argv[1] == "is_open":
        retval = is_open()
        logging.info(retval)
      if sys.argv[1] == "is_closed":
        retval = is_closed()
        logging.info(retval)
      if sys.argv[1] == "get":
        feedback = incu.get_position()
        logging.info("Feedback:" + str(feedback))
      if sys.argv[1] == "set":
        set_position(int(sys.argv[2]))
      if sys.argv[1] == "reset":
        actu = lac.LAC()
        actu.reset()
      if sys.argv[1] == "speed":
        actu = lac.LAC()
        actu.set_speed(int(sys.argv[2]))
      if sys.argv[1] == "acuracy":
        actu = lac.LAC()
        actu.set_accuracy(int(sys.argv[2]))
