import os
import shutil

filename = 'G:/Hyperspectral/slice/json1/d7_.json'
filenum = eval(input('请输入复制的数量：'))
target = 'G:/Hyperspectral/slice/save'

print("copying")

def copyfile():
 for num in range(filenum):
  targetfile = os.path.join(target,'d7_'+str(num)+'.json')
  if os.path.exists(targetfile):
   continue
  shutil.copyfile(filename, targetfile)

copyfile()
print("well done")

