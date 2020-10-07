import xlrd
import copy
def get_excelData(sheetName,startRow,endRow,bodyCol,repsCol):
   excelDir='../data/松勤-教管系统接口测试用例-v1.4.xls'
   workBook = xlrd.open_workbook(excelDir, formatting_info=True)
   workSheet = workBook.sheet_by_name(sheetName)
   dataList=[]
#    # for cnt in range(1,5):
#    #     cellData=workSheet.cell_value(cnt,6)#请求体，字符串类型
#    #     repsCellData=workSheet.cell_value(cnt,8)#预期结果，字符串类型
#    #     dataList.append((cellData,repsCellData))#两个数据用元祖,把用户名密码单元格取出的值当成一个字符串,把预期结果的取出的字符串值当做一个字符串,加入列表名为c c=[(a,b),(c,d),(e,f)]
#    # return dataList
#
   for cnt in range(startRow-1,endRow):
       cellData=workSheet.cell_value(cnt,bodyCol)#请求体，字符串类型
       repsCellData=workSheet.cell_value(cnt,repsCol)#预期结果，字符串类型
       dataList.append((cellData,repsCellData))#两个数据用元祖,把用户名密码单元格取出的值当成一个字符串,把预期结果的取出的字符串值当做一个字符串,加入列表名为c c=[(a,b),(c,d),(e,f)]
   return dataList


#1- 读取excel数据  [(),(),()]
# def get_excelData(sheetName,startRow,endRow,body=6,repsData=8):
#     resList = []
#     excelDir = '../data/松勤-教管系统接口测试用例-v1.4.xls'
#     workBook = xlrd.open_workbook(excelDir)#打开excel文件
#     # sheets = workBook.sheet_names()
#     #2- 取对应的sheet来操作
#     workSheet = workBook.sheet_by_name(sheetName)
#     #获取单元格
#     # print(workSheet.cell(1,6).value)#请求的body
#     # print(workSheet.cell(1, 8).value)  # 请求的body
#     # print(workSheet.nrows)
#
#     for one in range(startRow-1,endRow):#[(),(),()]
#         resList.append((workSheet.cell(one,body).value,workSheet.cell(one,repsData).value))
#     return  resList
