#-*- coding:utf-8 -*-

"""针对小学生的数学加减法随机出题"""
"""20201024提交到仓库"""
import sys
from random import *

argv = sys.argv

class Puls:
	def __init__(self,Leastsum=10,Totalquestion=30,Postion=2):
		self.Leastsum = Leastsum
		self.Totalquestion = Totalquestion
		self.Postion = Postion

	def Makequestion_plusanddiff2(self):
		Firstnumber = randint(1,self.Leastsum)
		Secondnumber = randint(1,self.Leastsum)
		if  Firstnumber + Secondnumber >= self.Leastsum:
			if Firstnumber < Secondnumber:
				return '%s %s %s ='%(Secondnumber,['+','-'][1],Firstnumber)
			else:return '%s %s %s ='%(Firstnumber,['+','-'][1],Secondnumber)
		if Firstnumber >= Secondnumber:
			return '%s %s %s ='%(Firstnumber,['+','-'][randint(0,1)],Secondnumber)
		if Firstnumber < Secondnumber:
			return '%s %s %s ='%(Secondnumber,['+','-'][randint(0,1)],Firstnumber)

	def Makequestion_plusanddiff3(self):
		Addnumlist = sorted(list(map(lambda x:randint(1,x) , [10,10,10])))
		if (Addnumlist[2])+(Addnumlist[1]) > p.Leastsum :
			return 	'%s %s %s %s %s ='%((Addnumlist[2]),'-',(Addnumlist[1]),'+',Addnumlist[0])
		else:
			while True:
				lst = '%s %s %s %s %s'%((Addnumlist[2]),['+','-'][randint(0,1)],(Addnumlist[0]),'-',Addnumlist[1])
				if eval(lst)>0:break 
			return lst + ' ='

if __name__ == '__main__':
	file = open('practise.txt','w')
	p = Puls(10,120,2)
	if p.Postion == 2: 
		serial_number = 1
		while True:
			if serial_number%6==0 :
				file.write(p.Makequestion_plusanddiff2()+'     \n'+'\n')
			else :file.write(p.Makequestion_plusanddiff2()+'      ')
			serial_number += 1
			if serial_number > p.Totalquestion:break
	if p.Postion == 3: 
		serial_number = 1
		while True:
			if serial_number%5==0 :
				file.write(p.Makequestion_plusanddiff3()+'    \n'+'\n')
			else :file.write(p.Makequestion_plusanddiff3()+'    ')
			serial_number += 1
			if serial_number > p.Totalquestion:break
	file.close()
			
     