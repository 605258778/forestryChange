import arcpy 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from arcpy import env
import os
import time
arcpy.AddMessage('程序开始：' + str(time.ctime()))  
def AddNewField(in_table,fieldname): 
    for fn in fieldname:
        fieldList = arcpy.ListFields(in_table)
        if fieldname not in fieldList:
            arcpy.AddField_management(in_table,fn,"TEXT",20,"","","","NULLABLE")
        
# Table that was produced by Check Geometry tool
table = arcpy.GetParameterAsText(0)# 二类小班
table1 = arcpy.GetParameterAsText(1)# 二类小班
env.workspace = table.split('mdb')[0]+r"mdb/林地年度变更数据"
union = "二类_变更_union"
arcpy.AddMessage('修复几何开始：' + str(time.ctime()))  
arcpy.RepairGeometry_management(table, "DELETE_NULL")
arcpy.RepairGeometry_management(table1, "DELETE_NULL")

fieldNameEd=["林地_二调","森林_二调"]
fieldNameBg = ["林地_变更","森林_变更"]
arcpy.AddMessage('新增字段开始：' + str(time.ctime())) 
AddNewField(table,fieldNameEd)
AddNewField(table1,fieldNameBg)
inFeatures = [table, table1]
arcpy.AddMessage('union开始：' + str(time.ctime())) 
arcpy.Union_analysis(inFeatures, union, "ALL", "", "GAPS")
fieldListUnion = arcpy.ListFields(union)
if '重新计算面积' not in fieldListUnion:
    arcpy.AddField_management(union,"重新计算面积","DOUBLE","","","","","NULLABLE")
arcpy.AddMessage('赋值开始：' + str(time.ctime())) 
arcpy.CalculateField_management(union, "重新计算面积","round((!Shape_Area!)/10000,2)","PYTHON_9.3")
expressionEdld = "getValue(!YDXZ!)"
codeblockEdld = """def getValue(YDXZ):
    if YDXZ == "100":
        return '林地'
    else:
        return '非林地'"""
arcpy.CalculateField_management(union, "林地_二调",expressionEdld,"PYTHON_9.3",codeblockEdld)
expressionEdsl = "getValue(!EDDL!)"
codeblockEdsl = """def getValue(EDDL):
    if (EDDL == "1110" or EDDL == "1310" or EDDL == "1130"):
        return '森林'
    else:
        return '非森林'"""
arcpy.CalculateField_management(union, "森林_二调",expressionEdsl,"PYTHON_9.3",codeblockEdsl)
expressionBgld = "getValue(!GLLX!)"
codeblockBgld = """def getValue(GLLX):
    if GLLX == "10":
        return '林地'
    else:
        return '非林地'"""
arcpy.CalculateField_management(union, "林地_变更",expressionBgld,"PYTHON_9.3",codeblockBgld)
expressionBgsl = "getValue(!DI_LEI!)"
codeblockBgsl = """def getValue(DI_LEI):
    if (DI_LEI == "0111" or DI_LEI == "0131" or DI_LEI == "0113"):
        return '森林'
    else:
        return '非森林'"""
arcpy.CalculateField_management(union, "森林_变更",expressionBgsl,"PYTHON_9.3",codeblockBgsl)

out_file = 'out_union'

# Create the necessary FieldMap and FieldMappings objects
fm = arcpy.FieldMap()
fm1 = arcpy.FieldMap()
fm2 = arcpy.FieldMap()
fm3 = arcpy.FieldMap()
fm4 = arcpy.FieldMap()
fm5 = arcpy.FieldMap()
fm6 = arcpy.FieldMap()
fm7 = arcpy.FieldMap()
fm8 = arcpy.FieldMap()
fm9 = arcpy.FieldMap()
fm10 = arcpy.FieldMap()
fm11 = arcpy.FieldMap()
fm12 = arcpy.FieldMap()
fm13 = arcpy.FieldMap()
fm14 = arcpy.FieldMap()
fm15 = arcpy.FieldMap()
fm16 = arcpy.FieldMap()
fm17 = arcpy.FieldMap()
fm18 = arcpy.FieldMap()
fms = arcpy.FieldMappings()
# Set properties of the output name.
fm.addInputField(union, "XIAN")
f_name = fm.outputField
f_name.name = 'XIAN_二调'
f_name.aliasName = "XIAN_二调"
fm.outputField = f_name
arcpy.AddMessage('fm完成：' + str(time.ctime())) 
# Add the intersection field to the second FieldMap object
fm1.addInputField(union, "XIANG")
f_name1 = fm1.outputField
f_name1.name = 'XIANG_二调'
f_name1.aliasName = "XIANG_二调"
fm1.outputField = f_name1

fm2.addInputField(union, "CUN")
f_name2 = fm2.outputField
f_name2.name = 'CUN_二调'
f_name2.aliasName = "CUN_二调"
fm2.outputField = f_name2

fm3.addInputField(union, "XBH")
f_name3 = fm3.outputField
f_name3.name = 'XBH_二调'
f_name3.aliasName = "XBH_二调"
fm3.outputField = f_name3

fm4.addInputField(union, "YDXZ")
f_name4 = fm4.outputField
f_name4.name = 'YDXZ_二调'
f_name4.aliasName = "YDXZ_二调"
fm4.outputField = f_name4

fm5.addInputField(union, "MIANJI")
f_name5 = fm5.outputField
f_name5.name = 'MIANJI_二调'
f_name5.aliasName = "MIANJI_二调"
fm5.outputField = f_name5

fm6.addInputField(union, "EDDL")
f_name6 = fm6.outputField
f_name6.name = 'EDDL_二调'
f_name6.aliasName = "EDDL_二调"
fm6.outputField = f_name6

fm7.addInputField(union, "林地_二调")
f_name7 = fm7.outputField
f_name7.name = '林地_二调'
f_name7.aliasName = "林地_二调"
fm7.outputField = f_name7

fm8.addInputField(union, "森林_二调")
f_name8 = fm8.outputField
f_name8.name = '森林_二调'
f_name8.aliasName = "森林_二调"
fm8.outputField = f_name8

fm9.addInputField(union, "XIAN_1")
f_name9 = fm9.outputField
f_name9.name = 'XIAN_变更'
f_name9.aliasName = "XIAN_变更"
fm9.outputField = f_name9

fm10.addInputField(union, "XIANG_1")
f_name10 = fm10.outputField
f_name10.name = 'XIANG_变更'
f_name10.aliasName = "XIANG_变更"
fm10.outputField = f_name10

fm11.addInputField(union, "CUN_1")
f_name11 = fm11.outputField
f_name11.name = 'CUN_变更'
f_name11.aliasName = "CUN_变更"
fm11.outputField = f_name11

fm12.addInputField(union, "XIAO_BAN")
f_name12 = fm12.outputField
f_name12.name = 'XIAO_BAN_变更'
f_name12.aliasName = "XIAO_BAN_变更"
fm12.outputField = f_name12

fm13.addInputField(union, "MIAN_JI")
f_name13 = fm13.outputField
f_name13.name = 'MIAN_JI_变更'
f_name13.aliasName = "MIAN_JI_变更"
fm13.outputField = f_name13

fm14.addInputField(union, "DI_LEI")
f_name14 = fm14.outputField
f_name14.name = 'DI_LEI_变更'
f_name14.aliasName = "DI_LEI_变更"
fm14.outputField = f_name14

fm15.addInputField(union, "GLLX")
f_name15 = fm15.outputField
f_name15.name = 'GLLX_变更'
f_name15.aliasName = "GLLX_变更"
fm15.outputField = f_name15

fm16.addInputField(union, "林地_变更")
f_name16 = fm16.outputField
f_name16.name = '林地_变更'
f_name16.aliasName = "林地_变更"
fm16.outputField = f_name16

fm17.addInputField(union, "森林_变更")
f_name17 = fm17.outputField
f_name17.name = '森林_变更'
f_name17.aliasName = "森林_变更"
fm17.outputField = f_name17

fm18.addInputField(union, "重新计算面积")
f_name18 = fm18.outputField
f_name18.name = '重新计算面积'
f_name18.aliasName = "重新计算面积"
fm18.outputField = f_name18
arcpy.AddMessage('FieldMap初始化完成：' + str(time.ctime())) 

# Add both FieldMaps to the FieldMappings Object
fms.addFieldMap(fm)
fms.addFieldMap(fm1)
fms.addFieldMap(fm2)
fms.addFieldMap(fm3)
fms.addFieldMap(fm4)
fms.addFieldMap(fm5)
fms.addFieldMap(fm6)
fms.addFieldMap(fm7)
fms.addFieldMap(fm8)
fms.addFieldMap(fm9)
fms.addFieldMap(fm10)
fms.addFieldMap(fm11)
fms.addFieldMap(fm12)
fms.addFieldMap(fm13)
fms.addFieldMap(fm14)
fms.addFieldMap(fm15)
fms.addFieldMap(fm16)
fms.addFieldMap(fm17)
fms.addFieldMap(fm18)
arcpy.AddMessage('输出删除字段后表：' + str(time.ctime())) 
# Create the output feature class, using the FieldMappings object
arcpy.FeatureClassToFeatureClass_conversion(
    union, arcpy.env.workspace, out_file, field_mapping=fms)

arcpy.AddMessage('导出开始：' + str(time.ctime())) 
arcpy.FeatureClassToFeatureClass_conversion(out_file,env.workspace,"二类_变更_林地",
    "林地_二调 <> 林地_变更 and Shape_Area>=667")
arcpy.FeatureClassToFeatureClass_conversion(out_file,env.workspace,"二类_变更_林地_小于667",
    "林地_二调 <> 林地_变更 and Shape_Area<667")
arcpy.FeatureClassToFeatureClass_conversion(out_file,env.workspace,"二类_变更_森林",
    "森林_二调 <> 森林_变更 and Shape_Area>=667")
arcpy.FeatureClassToFeatureClass_conversion(out_file,env.workspace,"二类_变更_森林_小于667",
    "森林_二调 <> 林地_变更 and Shape_Area<667")
arcpy.AddMessage('删除表：' + str(time.ctime()))
arcpy.Delete_management(out_file) 
arcpy.Delete_management(union) 
