import json 
import os
import shutil

sourcename = 'G:/Hyperspectral/slice/json1/d7_.json'#被复制的源json文件
sv_path = "G:/Hyperspectral/slice/json_D7_triple_band/"  # 修改后的json文件存放路径
img_path='G:/Hyperspectral/slice/D7_triple_band/'    #图片集存放路径
n=0
def batchcopy():
    imgs=os.listdir(img_path) # 读取图片集路径下所有文件名
    for name in imgs:
        imgname=name.split('.')[0]
        # print (imgname) #
        targetfile=os.path.join(sv_path,str(imgname)+'.json')
        if os.path.exists(targetfile):
            continue
        shutil.copyfile(sourcename, targetfile)
         # print (imgname) #显示复制的文件名

def batch_generate_json():
    global n
    files=os.listdir(sv_path)
    for filename in files:

        filepath=sv_path+filename
        after = []
        # 打开文件取出数据并修改，然后存入变量
        with open(filepath, 'r') as f:
            data = json.load(f)
            data['imagePath']=filename
            data[]
            after = data

        # 打开文件并覆盖写入修改后内容
        with open(filepath, 'w') as f:
            data = json.dump(after, f)
        n+=1    
        print (filename+' 已生成。\n')
    print('总共生成了%d个json文件！'%(n))


batchcopy()

batch_generate_json()

print("well done")            