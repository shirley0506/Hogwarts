#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest
import requests


# 获取token
from filelock import FileLock


@pytest.fixture(scope='session')
def test_token():
    with FileLock("session.lock"):
        corpid = 'wwb9dd59b36dfb3ab0'
        corpsecret = 'Bg-l59yCtimW-H8rBSiRC_IWDsF07awtF0UGTtb3KuU'
        req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return req.json()['access_token']


# 创建部门
# @pytest.mark.parametrize("name, name_en, ID", [('上海研发中心2', 'Develop2', 2)])
def test_create_dep(name, name_en, ID, test_token):
    data = {
        "name": name,
        "name_en": name_en,
        "parentid": 1,
        "id": ID
    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token}",
                        json=data
                        )
    return req.json()


# 修改部门信息
def test_edit_dep(ID, name, test_token):
    data = {
        "id": ID,
        "name": name,
    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token}",
                        json=data
                        )
    return req.json()


# 获取部门列表
def test_get_dep(ID, test_token):
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token}&id={ID}")
    # print(req.json())
    return req.json()


# 删除部门
def test_del_dep(ID, test_token):
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token}&id={ID}")
    # print(req.json())
    return req.json()


# 根据部门名称获取部门ID
# @pytest.mark.parametrize("name", ['上海研发中心'])
def test_get_DepID(name, test_token):
    get_all_deps = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token}")
    list_deps = get_all_deps.json()['department']
    for dep in list_deps:
        if name == dep['name']:
            del_id = dep['id']
            return del_id


# 准备测试数据
def test_create_data():
    data = [("上海研发中心" + str(i),
             "Develop" + str(i),
             i) for i in range(3, 10)]
    return data


# 测试用例
@pytest.mark.parametrize("name, name_en, ID", test_create_data())
def test_all(name, name_en, ID, test_token):
    try:
        assert "created" == test_create_dep(name, name_en, ID, test_token)['errmsg']
    except AssertionError as e:
        # 如果部门名称重复或者部门ID重复，找到同名的部门id并删除
        if "department existed" in e.__str__():
            del_id = test_get_DepID(name, test_token)
            if del_id != 'None':
                assert "deleted" == test_del_dep(del_id, test_token)['errmsg']
                assert "created" == test_create_dep(name, name_en, ID, test_token)['errmsg']
            else:
                assert "deleted" == test_del_dep(ID, test_token)['errmsg']
                assert "created" == test_create_dep(name, name_en, ID, test_token)['errmsg']
    assert name == test_get_dep(ID, test_token)['department'][0]['name']
    assert "updated" == test_edit_dep(ID, '北京研发中心', test_token)['errmsg']
    assert "北京研发中心" == test_get_dep(ID, test_token)['department'][0]['name']
    assert "deleted" == test_del_dep(ID, test_token)['errmsg']
    assert 60123 == test_del_dep(ID, test_token)['errcode']



