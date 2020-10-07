import yaml
#操作yaml
yamlDir = "../data/test.yaml"
#创建文件对象,读操作
# fo = open(yamlDir,"r",encoding="utf-8")
# res = yaml.load(fo,Loader=yaml.FullLoader)#获取数据
# print(res)

# 2组数据---可迭代对象
fo = open(yamlDir,"r",encoding="utf-8")
res=yaml.load_all(fo,Loader=yaml.FullLoader)
print(res)
for one in res:
    print(one)

#yaml写操作
fo = open(yamlDir,"w",encoding="utf-8")
data1={"name":"tom","age":20}#写入字典
data2=[10,20,30,{"name":"tom","age":20}]
yaml.dump(data1,fo)#写一组数据
yaml.dump_all([data1,data2],fo)#写多个数据

fo.close()#关闭文件
