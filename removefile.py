import os,shutil,time;
path = input("enter the path diaractory: ")
days = time.time()
isexist = os.path.exists(path)
def deletefile():
    ctime = os.stat(path).st_ctime
    res = ctime+days
    if(res>days):
        if(os.path.isfile(path)):
            os.remove(path) 
            print('junk file deleted!!!!!')
        else:
            shutil.rmtree()
        
if(isexist == True):
    deletefile()   
else:
    print('path not exists!')    


