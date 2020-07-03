#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

# 获取token
def test_token():
    corpid = 'wwb9dd59b36dfb3ab0'
    corpsecret = 'Bg-l59yCtimW-H8rBSiRC_IWDsF07awtF0UGTtb3KuU'
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return req.json()['access_token']


# 创建部门
def test_create_dep():
    data = {
        "name": "测试",
        "name_en": "Testing",
        "parentid": 1
    }

    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}",
                        json=data
                        )


# 修改部门信息
def test_edit_dep():
    data = {
        "id": 2,
        "name": "产品测试",
    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}",
                        json=data
                        )
    print(req.json())


# 获取部门列表
def test_get_dep():
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}")
    print(req.json())


# 删除部门
def test_del_dep():
    dep_id = 2
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id={dep_id}")
    print(req.json())

