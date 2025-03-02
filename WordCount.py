#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
    for l in line:
      letterCount = letterCount + 1
  
  print("Lines: ", lineCount)
  print("Words: ", wordCount)
  print("Characters: ", letterCount-lineCount)

if __name__ == '__main__':
  main()
