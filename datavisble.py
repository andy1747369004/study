import matplotlib
import pandas as pd
import matplotlib.pylab as plt
matplotlib.rcParams[u'font.sans-serif'] = ['simhei']
matplotlib.rcParams['axes.unicode_minus'] = False

#------------------
#将json文件转化为pandas
with open("./labels/AgriculturalDisease_train_annotations.json") as datafile1:
    trainDataFram=pd.read_json(datafile1,orient='records')
with open("./labels/AgriculturalDisease_validation_annotations.json") as datafile2: #first check if it's a valid json file or not
    validateDataFram =pd.read_json(datafile2,orient='records')    

with open("./labels/combination.json") as datafile: #first check if it's a valid json file or not
    combineDataFram =pd.read_json(datafile,orient='records') 


#------------------
#查看数据中Null的分布情况
# total=trainDataFram.isnull().sum().sort_values(ascending=False)
# percent=(trainDataFram.isnull().sum())/(trainDataFram.isnull().count()).sort_values(ascending = False)
# missing_validation_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'],sort=False)
# missing_validation_data.head()



#------------------
#按类别序号依次显示训练集的分布情况

# dataDistribute=trainDataFram.groupby(by=['disease_class']).size()
# plt.figure(figsize=(50,20),dpi=100)
# plt.xticks(range(len(dataDistribute)),dataDistribute.index.tolist(),fontsize=10)
# plt.yticks(fontsize=10)
# bar=plt.bar(dataDistribute.index.tolist(), dataDistribute.tolist(),width=0.7)
 
# for b in bar:
#     h=b.get_height()
#     plt.text(b.get_x()+b.get_width()/2,h,int(h),ha='center',fontsize=10)
# plt.show()




#------------------
#按类别序号依次显示验证集的分布情况

# dataDistribute=validateDataFram.groupby(by=['disease_class']).size()
# plt.figure(figsize=(50,20),dpi=100)
# plt.xticks(range(len(dataDistribute)),dataDistribute.index.tolist(),fontsize=10)
# plt.yticks(fontsize=10)
# bar=plt.bar(dataDistribute.index.tolist(), dataDistribute.tolist(),width=0.7)
 
# for b in bar:
#     h=b.get_height()
#     plt.text(b.get_x()+b.get_width()/2,h,int(h),ha='center',fontsize=10)
# plt.show()




#------------------
#显示Number of Training Examples Versus Class

#trainDataFram['disease_class'].value_counts().plot(kind='bar',figsize=(60,30),fontsize =10,title="Number of Training Examples Versus Class").title.set_size(20)
#plt.show()





#-------------------------
#将训练集从大到小排序，并可视化显示
# dataDistribute=trainDataFram['disease_class'].value_counts()
# plt.figure(figsize=(50,20),dpi=100)
# plt.xticks(range(len(dataDistribute)),dataDistribute.index.tolist(),fontsize=10) #第一个参数是在哪些位置需要放置坐标值  第二个参数是放置的坐标值大小
# plt.yticks(fontsize=10)
# bar=plt.bar(range(len(dataDistribute)),dataDistribute.tolist(),width=0.6)
# for b in bar:
#     h=b.get_height()
#     plt.text(b.get_x()+b.get_width()/2,h,int(h),ha='center',fontsize=10)
# plt.show()


#-------------------------
#将验证集从大到小排序，并可视化显示
# dataDistribute=validateDataFram['disease_class'].value_counts()
# plt.figure(figsize=(50,20),dpi=100)
# plt.xticks(range(len(dataDistribute)),dataDistribute.index.tolist(),fontsize=10) #第一个参数是在哪些位置需要放置坐标值  第二个参数是放置的坐标值大小
# plt.yticks(fontsize=10)
# bar=plt.bar(range(len(dataDistribute)),dataDistribute.tolist(),width=0.6)
# for b in bar:
#     h=b.get_height()
#     plt.text(b.get_x()+b.get_width()/2,h,int(h),ha='center',fontsize=10)
# plt.show()







#------------------
#按类别序号依次显示合并集的数据分布情况
# def show1(it):
    dataDistribute=it.groupby(by=['disease_class']).size()
    plt.figure(figsize=(50,20),dpi=100)
    plt.xticks(range(len(dataDistribute)),dataDistribute.index.tolist(),fontsize=10)
    plt.yticks(fontsize=10)
    bar=plt.bar(dataDistribute.index.tolist(), dataDistribute.tolist(),width=0.7)
    
    for b in bar:
        h=b.get_height()
        plt.text(b.get_x()+b.get_width()/2,h,int(h),ha='center',fontsize=10)
    plt.show()

show1(combineDataFram)


#-------------------------
#将合并集从大到小排序，并可视化显示
# def show2(it):
#     dataDistribute=it['disease_class'].value_counts()
#     plt.figure(figsize=(50,20),dpi=100)
#     plt.xticks(range(len(dataDistribute)),dataDistribute.index.tolist(),fontsize=10) #第一个参数是在哪些位置需要放置坐标值  第二个参数是放置的坐标值大小
#     plt.yticks(fontsize=10)
#     bar=plt.bar(range(len(dataDistribute)),dataDistribute.tolist(),width=0.6)
#     for b in bar:
#         h=b.get_height()
#         plt.text(b.get_x()+b.get_width()/2,h,int(h),ha='center',fontsize=10)
#     plt.show()

# show2(combineDataFram)    



#-------------------------
#查看trainDataSet和Validate DataSet数据分布
# f,(ax0,ax1)=plt.subplots(1,2,sharey=True,figsize=(15,5))
# ax0.hist(trainDataFram['disease_class'].value_counts())
# ax0.set_xlabel("# images per class")
# ax0.set_ylabel("# classes")
# ax0.set_title('Class distribution for Train')

# ax1.hist(validateDataFram['disease_class'].value_counts())
# ax1.set_xlabel("# images per class")
# ax1.set_title('Class distribution for Validation')
# plt.show()