'''
def startLog(logName):
  logName = open(logName, "w")
  logName.write("")
  logName.close()
  global log
  log is True
  return logName

def openLog(logName):
  logName = open(logName, "a")
  logName.write("")
  logName.close()
  global log
  log is True
  return logName

def log(msg, logName):
    if log is True:
      print(msg)
      if logName is not None:
        logName = open(logName, "a")
        logName.write(msg)
        logName.close()
'''

def binaryToDenary(binary):
  binary = str(binary)
  binary = binary.strip()
  binaryList = []
  denary = 0
  denaryValue = 1
  global letter
  for letter in binary:
      binaryList.append(letter)          
  for currentBinary in reversed(binaryList):
      if currentBinary == "1":
          denary = denary + denaryValue
          denaryValue = denaryValue * 2
      elif  currentBinary == "0":
          denaryValue = denaryValue * 2
      else:
          exit("Invalid binary code.")
  return denary

def denaryToBinary(denary):
  if denary is float:
    exit("Invalid input, input must be a whole number")
  denary = int(denary)
  denaryList = []
  denaryValue = 1
  while True:
    if denaryValue >= denary:
      denaryList.append(denaryValue)
      break
    else:
      denaryList.append(denaryValue)
      denaryValue = denaryValue * 2
  binaryList = []
  for number in reversed(denaryList):
    if number <= denary:
      denary = denary - number
      binaryList.append(1)
      denaryList.remove(number)
    else:
      binaryList.append(0)
      denaryList.remove(number)
    if denary == 0:
      for position in reversed(denaryList):
        binaryList.append(0)
      binaryList = str(binaryList)
      binary = binaryList.replace(",","").replace(" ", "")
      binary = binary.replace("[", "").replace("]", "").replace("]", "")
      return binary
      break

def addBinary(binary1, binary2):
  return denaryToBinary(binaryToDenary(int(binary1)) + binaryToDenary(int(binary2)))
def subtractBinary(binary1, binary2):
  return denaryToBinary(binaryToDenary(int(binary1)) - binaryToDenary(int(binary2)))
def multiplyBinary(binary1, binary2):
  return denaryToBinary(binaryToDenary(int(binary1)) * binaryToDenary(int(binary2)))
def divideBinary(binary1, binary2):
  return denaryToBinary(binaryToDenary(int(binary1)) / binaryToDenary(int(binary2)))
