#!/usr/bin/env python3
import lac
import sys

# 46mm/s (no load)

def set_position(position):
# 0 = 0, 1023 = 200mm 5 pos 1mm
  actu = lac.LAC()
  #actu.reset()
  #actu.set_retract_limit(23)
  #actu.set_extend_limit(1000)
  #actu.set_accuracy(10)
  #actu.set_accuracy(4)
  actu.set_position(position)

def set_speed(position):
  actu = lac.LAC()
  actu.set_retract_limit(position)

def set_retract_limit(position):
  actu = lac.LAC()
  actu.set_retract_limit(position)


  #actu = None
  #actu = lac.LAC()
  #print("Actu feedback:" + str(actu.get_feedback()))
  #actu = None
def get_position():
# 0 = 0, 1023 = 200mm 5 pos 1mm
  actu = lac.LAC()
  position = actu.get_feedback()
  return position

if __name__ == "__main__":

    print(sys.argv[1:])
    print(sys.argv[1])

    if len(sys.argv) > 1:
      if sys.argv[1] == "get":
        feedback = get_position()
        print("Feedback:" + str(feedback))
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
