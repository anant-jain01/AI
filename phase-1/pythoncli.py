import json
import random
import os
print("1.Add\n2.QUIZ\n")
userInput=int(input("Choice:"))
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'questions.json')
data=open(file_path,'r')
database=json.load(data)


if userInput==1:
  obj={}
  obj["question"]=input("question:")
  obj["answer"]=input("answer:")
  obj["topic"]=input("Topic:")
  obj["difficulty"]=input("Diffculty:")
  database.append(obj)
  with open(file_path,'w') as openFile:
    json.dump(database,openFile)
  data.close()
  print("FINISHED")


elif userInput==2:
  curr=0
  score=0
  random.shuffle(database)

  while curr<len(database):
    print('[',database[curr]['difficulty'],']',database[curr]['question'])
    ans=input("ANSWER:")
    if ans.lower()==database[curr]['answer'].lower() or ans.lower() in database[curr]['answer'].lower():
      print('CORRECT')
      curr+=1
      score+=1
    elif ans.lower()=='score':
      print(score)
      continue
    elif ans.lower()=='end':
      print(score)
      break
    else: 
      print('wrong')
      print(database[curr]['answer'])
      curr+=1


else:print("ONLY 2 OPTIONS!!!!!")