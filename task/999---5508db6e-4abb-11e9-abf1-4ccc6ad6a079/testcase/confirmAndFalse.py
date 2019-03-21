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
class confirmAndFalse(unittest.TestCase):
    '''修改告警状态'''
    @classmethod
    def setUpClass(cls):
        cls.transferlogname=Transferlogname()
        cls.transferip_db=Transferip_db()
        cls.transfermongodb = Transferip_mongodb()
        cls.transferfunction = Transferfunction()
        api="/back/event/confirmAndFalse"
        cls.url=cls.transferip_db.ip+api
        pass

    @classmethod
    def tearDownClass(cls):
        pass



    def test_修改告警状态(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''globalId需要从246用例的返回值中获取，userID要保持和246获取到的一致'''
        step_name="修改告警状态"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'userId', 'sql': 'select userId from t_user where level =1 and valid=1   limit 1', 'db': '1', 'db_remark': '157-sanhua'}]
        nosqlDatalist=[]
        api_dependency={"globalId":{"查询告警信息不传必填项":"['globalId']"}}
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
        
        params='''{"timestamp":"${__get_today_Timestamp()}","conAndFal": 3,"userId": "${userId}","globalId": "${globalId}","content":"test"}'''
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
    def test_修改告警状态不传时间戳(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''globalId需要从246用例的返回值中获取，userID要保持和246获取到的一致'''
        step_name="修改告警状态不传时间戳"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'userId', 'sql': 'select userId from t_user where level =1 and valid=1   limit 1', 'db': '1', 'db_remark': '157-sanhua'}]
        nosqlDatalist=[]
        api_dependency={"globalId":{"查询告警信息不传必填项":"['globalId']"}}
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
        
        params='''{"conAndFal": 3,"userId": "${userId}","globalId": "${globalId}","content":"test"}'''
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
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"验证时间戳不得为空"}}
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
    def test_修改告警状态不传userId(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''globalId需要从246用例的返回值中获取'''
        step_name="修改告警状态不传userId"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={"globalId":{"查询告警信息不传必填项":"['globalId']"}}
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
        
        params='''{"timestamp":"${__get_today_Timestamp()}","conAndFal": 3,"globalId": "${globalId}","content":"test"}'''
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
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"用户id不得为空"}}
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
    def test_修改告警状态不传globalId(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''userID要保持和246获取到的一致'''
        step_name="修改告警状态不传globalId"
        newVariableObj = {}
        sqlDatalist=[{'sql_condition': 0, 'is_select': True, 'variable': 'userId', 'sql': 'select userId from t_user where level =1 and valid=1   limit 1', 'db': '1', 'db_remark': '157-sanhua'}]
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
        
        params='''{"timestamp":"${__get_today_Timestamp()}","conAndFal": 3,"userId": "${userId}","content":"test"}'''
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
        
        assert_response={"status_code":{"assertEqual":"200"},"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"事件标记不得为空"}}
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
