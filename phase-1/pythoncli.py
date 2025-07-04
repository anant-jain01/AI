import random
print('\n',"1.Add\n2.QUIZ\n")
userInput=int(input("Choice:"))
if userInput==1:
  data=open('questions.json','w')
  obj={}
  obj["question"]=input("question:")
  obj["answer"]=input("answer:")
  obj["topic"]=input("Topic:")
  obj["difficulty"]=input("Diffculty:")
  data.write(obj)
elif userInput==2:
  score=0
  print("for score type score")
  data=open('questions.json','r')
  databse=data.read()
  while input()!="score":
  #random for int length0- json.length+1
  #if user inout matches the answer score+=1
  print(score)