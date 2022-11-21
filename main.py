from textblob import TextBlob
def sentiment(polarity):
     print("Polarity: " + str(blob.sentiment.polarity) + " Subjectivity: " + str(blob.subjectivity))
     if blob.sentiment.polarity <0:
         print("Negative")
     elif blob.sentiment.polarity > 0:
         print("Positive")
     else:
         print("Neutral")
     print()

with open('assignment 3 data.txt') as file:
    data = file.readlines()

for line in data:
    print(line,end = "")
    blob = TextBlob(line)
    sentiment(blob)