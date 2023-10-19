from game_data import data
import random
import os
import time
score=0
count=0
def printinfo(n):
  global count
  count+=1
  dict1=dict(data[n])
  name=dict1['name']
  desc=dict1['description']
  country=dict1['country']
  fol_count=dict1['follower_count']
  print(count,". Name: ",name,"\nDescription: ",desc,"\nCountry: ",country,"\n\n")
  return fol_count


def if_correct(n1,n2):
  dict1=dict(data[n1])
  dict2=dict(data[n2])
  name1=dict1['name']
  desc1=dict1['description']
  country1=dict1['country']
  fol_count1=dict1['follower_count']
  print("Name: ",name1,"\n\nNumbers of followers they have are\033[1m",fol_count1," \033[0m\n\n\t\tVS\n")
  name2=dict2['name']
  desc2=dict2['description']
  country2=dict2['country']
  fol_count2=dict2['follower_count']
  print("Name: ",name2,"\n\nNumbers of followers they have are\033[1m",fol_count2,"\033[0m\n\n")



def randomgen(n=-1):
  x=random.randint(0,50)
  return x if x!=n else randomgen(n)


def mainfunc(n1=0,n2=0):
  n1=randomgen() if n1==0 else n1
  fc1=printinfo(n1)
  n2=randomgen(n1)
  fc2=printinfo(n2)
  maxi=max(fc1,fc2)
  x=int(input("Enter your choice: "))
  if x==count-1:
    choice= fc1
  elif x==count:
    choice= fc2
  else:
    print("\t\n\nWrong input taking default as  1\n")
    choice= fc1
  n3=n1 if x==count-1 else n2
  n4=n2 if x==count-1 else n1
  if choice==maxi:
    print("\n\nGreat you got it Correct!!\n\n")
    if_correct(n3,n4)
    mainfunc(n3)
    
  else :
    print("\n\nBetter luck next time\n\n")
    if_correct(n3,n4)

if __name__ == '__main__':
  mainfunc()

  