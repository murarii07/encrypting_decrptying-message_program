import random as rd


def encoding(message):
  '''
      y=rd.choice(l) this will select charactors ramdomly
      #y = alphabets[rd.randrange(0, 26)] this is same as y=rd.choice(l)
      dd is used add 3 characters at start and end of message
  '''
  alphabets = "abcdefghijklmnopqrstuvwxyz"
  dd = ""
  x = len(message)
  if (x > 2):
    for i in range(0, 6):
      y = rd.choice(alphabets)
      dd += y
    encode_mess = dd[:3] + message[-1] + message[1:-1] + message[0] + dd[3:]
    print(f"encoded message:  {encode_mess}")

  else:
    print(f"encoded message:  {message[::-1]}")


def decoding(mess):

  if (len(mess) > 2):
    decode_mess = mess[-4] + mess[4:-4] + mess[3]
    print(f"decoded message:  {decode_mess}")

  else:
    print(f"decoded message:  {mess[::-1]}")


while True:
  message = input("enter a message  ")
  if message == "":
    print("the message is empty")
  else:
    op = input("enter a encoding or decoding  ")

    if op == 'e':
      encoding(message)

    elif op == 'd':
      decoding(message)

  ex = input("do you want to quit or not[y/n]:  ")
  if ex == 'y':
    break
  else:
    pass

