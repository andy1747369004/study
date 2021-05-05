
# #使用spectral这个库
import spectral.io.envi as envi
import spectral

# 打开高光谱文件
# hsi_hdr_file_name 是高光谱文件名，包含.raw和.hdr文件
hsi_hdr_file_name=r'G:/Hyperspectral/data/D7.hdr'
HSI = envi.open(hsi_hdr_file_name)
# ls=[]
# for i in range(5,176,5):
#     ls.append(i)

#如果要保存[72,45,21]这三个波段合成RGB，就在save_rgb中输入这个向量
# for i in range(0,176,5):

#             ls.append(i)
#             ls.append(0)
#             ls.append(0)
            # Raster_data = HSI[:,:,:]
            # hsi_rgb_file_name = 'G:/Hyperspectral/slice/D7_double_band/d7_{}.jpg'.format(i)#要保存RGB图像的名称
            # spectral.save_rgb(hsi_rgb_file_name, Raster_data,ls)
#             ls.clear()
# print(len(ls))

a=[]
b=[]

for i in range(5,176,5):
    a.append(i)
for i in range(10,176,10):
    b.append(i)
def process1(index1,index2):
    global n
    l=[]
    print(a[index1],a[index2])
    l.append(a[index1])
    l.append(a[index2])
    l.append(0)
    n+=1
    Raster_data = HSI[:,:,:]
    hsi_rgb_file_name = 'G:/Hyperspectral/slice/D7_double_band/d7_{}_{}.jpg'.format(a[index1],a[index2])#要保存RGB图像的名称
    spectral.save_rgb(hsi_rgb_file_name, Raster_data,l)
    l.clear()

def process2(index1,index2,index3):
    global m
    l=[]
    print(b[index1],b[index2],b[index3])
    l.append(b[index1])
    l.append(b[index2])
    l.append(b[index3])
    m+=1
    Raster_data = HSI[:,:,:]
    hsi_rgb_file_name = 'G:/Hyperspectral/slice/D7_triple_band/d7_{}_{}_{}.jpg'.format(b[index1],b[index2],b[index3])#要保存RGB图像的名称
    spectral.save_rgb(hsi_rgb_file_name, Raster_data,l)
    l.clear()

def recursion1(index1,index2):

    process1(index1,index2)
    if index1==33:
        return 0
    elif index2<34:
        index2+=1
    elif index1<33:
        index1+=1
        index2=index1+1
    recursion1(index1,index2)

def recursion2(index1,index2,index3):
   
    process2(index1,index2,index3)
   
    if index1==14:
        return
    elif index3<16:
        index3+=1
    elif index2<15:
        index2+=1
        index3=index2+1
    elif index1<14:
        index1+=1
        index2=index1+1
        index3=index2+1
    recursion2(index1,index2,index3)

print("combination:\n")
n=0
m=0
# recursion1(0,1)
# print(n)

recursion2(0,1,2)
print(m)
