#!/usr/bin/python
#-*- encoding:UTF-8 -*-

from public.request import *
from public.sqldb import *
from public.log import *
from public.run import *
from public.sqldb import Transferip_db
from public.mongodb import Transferip_mongodb
from public.carryfunction import Transferfunction
from public.script_function import *
from django.db.models import F
import unittest,re,json,jsonpath
class inOrUpcustom(unittest.TestCase):
    '''电耗结构自定义月设置'''
    @classmethod
    def setUpClass(cls):
        cls.transferlogname=Transferlogname()
        cls.transferip_db=Transferip_db()
        cls.transfermongodb = Transferip_mongodb()
        cls.transferfunction = Transferfunction()
        api="/back/energy/inOrUpcustom"
        cls.url=cls.transferip_db.ip+api
        pass

    @classmethod
    def tearDownClass(cls):
        pass



    def test_自定义月新增之本月1号默认显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之本月1号默认显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":1,"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之本月30号默认显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之本月30号默认显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":30,"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之本月当天默认显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之本月当天默认显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":${__get_today()},"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之本月前一天默认显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之本月前一天默认显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":${__get_yestoday()},"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之本月明天默认显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之本月明天默认显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":${__get_tomorrow()},"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之上月1号默认不显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之上月1号默认不显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":1,"monthFlag":0,"isDefault":false}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之上月30号默认不显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之上月30号默认不显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":30,"monthFlag":0,"isDefault":false}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之上月当天默认显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之上月当天默认显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":${__get_today()},"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之上月前一天默认显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之上月前一天默认显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":${__get_yestoday()},"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月新增之上月明天默认显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月新增之上月明天默认显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":${__get_tomorrow()},"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月之不传isDefault(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''isDefault可选'''
        step_name="自定义月之不传isDefault"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":20,"monthFlag":1}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月之不传siteid(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''siteid必填'''
        step_name="自定义月之不传siteid"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","day":30,"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"参数错误1"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月之不传day(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''day必填'''
        step_name="自定义月之不传day"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"参数错误1"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月之不传monthFlag(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''monthFlag必填'''
        step_name="自定义月之不传monthFlag"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":28,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"参数错误1"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月之传入32号(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''日期输入不合法'''
        step_name="自定义月之传入32号"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":32,"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"参数错误1"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月之monthFlag传入2(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''不是正确输入，只有0，1'''
        step_name="自定义月之monthFlag传入2"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select s.site_id from  t_site s left join t_power_consume_config  p on  s.site_id = p.siteId where p.siteId is null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":1,"monthFlag":2,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"参数错误1"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_给同一站点重复添加自定义月(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="给同一站点重复添加自定义月"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select p.siteId from t_power_consume_config  p left join t_site s on s.site_id = p.siteId where p.siteId is not null limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"add","siteId":"${siteId}","day":1,"monthFlag":1,"isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"此站点已有自定义月"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之默认成不显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''查询出默认显示的设置'''
        step_name="自定义月修改之默认成不显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId,day,monthFlag', 'sql': 'select siteId,day,monthFlag from t_power_consume_config where isDefault ="true" order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"${siteId}","day":"${day}","monthFlag":"${monthFlag}","isDefault":false}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之默认成显示(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之默认成显示"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId,day,monthFlag', 'sql': 'select siteId,day,monthFlag from t_power_consume_config where isDefault ="false" order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"${siteId}","day":"${day}","monthFlag":"${monthFlag}","isDefault":true}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之本月改成上月(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之本月改成上月"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId,day,isDefault', 'sql': 'select siteId,day,isDefault from t_power_consume_config where monthFlag = 1 order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"${siteId}","day":"${day}","monthFlag":0,"isDefault":"${isDefault}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之上月改成本月(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之上月改成本月"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId,day,isDefault', 'sql': 'select siteId,day,isDefault from t_power_consume_config where monthFlag = 0 order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"${siteId}","day":"${day}","monthFlag":1,"isDefault":"${isDefault}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之修改日期(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之修改日期"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId,monthFlag,isDefault', 'sql': 'select siteId,monthFlag,isDefault from t_power_consume_config  order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"${siteId}","day":13,"monthFlag":"${monthFlag}","isDefault":"${isDefault}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之修改站点(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之修改站点"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'day,monthFlag,isDefault', 'sql': 'select day,monthFlag,isDefault from t_power_consume_config  order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"site_00000999","day":"${day}","monthFlag":"${monthFlag}","isDefault":"${isDefault}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之不传参数(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之不传参数"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"参数错误3"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之不传isDefault(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之不传isDefault"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId,day,monthFlag', 'sql': 'select siteId,day,monthFlag from t_power_consume_config  order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"${siteId}","day":"${day}","monthFlag":"${monthFlag}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之不传siteid(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之不传siteid"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'day,monthFlag,isDefault', 'sql': 'select day,monthFlag,isDefault from t_power_consume_config  order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","day":"${day}","monthFlag":"${monthFlag}","isDefault":"${isDefault}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"参数错误3"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之不传day(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之不传day"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId,monthFlag,isDefault', 'sql': 'select siteId,monthFlag,isDefault from t_power_consume_config  order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"${siteId}","monthFlag":"${monthFlag}","isDefault":"${isDefault}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_自定义月修改之不传monthFlag(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="自定义月修改之不传monthFlag"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId,day,isDefault', 'sql': 'select siteId,day,isDefault from t_power_consume_config order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"update","siteId":"${siteId}","day":"${day}","isDefault":"${isDefault}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_删除自定义月(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="删除自定义月"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'siteId', 'sql': 'select siteId from t_power_consume_config order by siteId desc limit 1', 'db': '1', 'db_remark': 'sanhua'}]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"del","siteId":"${siteId}"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_删除一个不存在的自定义月设置(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="删除一个不存在的自定义月设置"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"del","siteId":"site_00000998"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_删除自定义月之不传站点(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        ''''''
        step_name="删除自定义月之不传站点"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"operation":"del"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=postbody(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"参数错误3"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="postbody"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferfunction,sqlDatalist, 2,newVariableObj)
