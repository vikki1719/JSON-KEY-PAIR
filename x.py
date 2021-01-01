import json
import os
import sys
class JSONDATA:
        y={}
        def __init__(self):
                self.y={}
                if(os.path.exists('x.json')):
                        with open('x.json') as f:
                                self.y = json.load(f)
                else:
                        with open('./x.json', 'w') as json_file:
                                json.dump(self.y, json_file)
        def writedata(self):
                key=input("Enter Key: ")
                if(len(key)<32):
                        if key not in self.y:
                                val=input("Enter Value : ")
                                if(sys.getsizeof(val)<16384):
                                        self.y[key]=val
                                        with open('./x.json', 'w') as json_file:
                                                json.dump(self.y, json_file)                                        
                                else:
                                        printf("Sorry Value size is greater than 16 KB") 
                        else:
                                print("Sorry key already present") 
                else:
                        print("Sorry too much length size")
                                
                        
        def readdata(self):
                key=input("Pleae enter the Key : ")
                if(key in self.y):
                        print("The value is : ",self.y[key])
                else:
                        print("Sorry key is not present")
        def deletedata(self):
                key=input("Pleae enter the Key : ")
                if(key in self.y):
                        del self.y[key]
                        with open('./x.json', 'w') as json_file:
                                json.dump(self.y, json_file)      
                else:
                        print("Sorry key is not present")
opt=1
obj=JSONDATA()
while(opt<=3 and opt>0):
        
        print('Welcome')
        print('1. Add key')
        print('2. Read key')
        print('3. Delete key')
        print('4. Exit : ')
        opt=int(input("Enter Your Option : "))
        if(opt==1):
                obj.writedata()
        elif(opt==2):
                obj.readdata()
        elif(opt==3):
                obj.deletedata()
        else:
                break
        


