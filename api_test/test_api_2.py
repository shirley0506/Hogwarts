#!/usr/bin/python3
# -*- coding: UTF8 -*-
import random
import re

import pytest
import requests
from filelock import FileLock


@pytest.fixture(scope='session')
def test_token():
    with FileLock("session.lock"):
        corpid = 'wwb9dd59b36dfb3ab0'
        corpsecret = 'Bg-l59yCtimW-H8rBSiRC_IWDsF07awtF0UGTtb3KuU'
        req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    # print("test_token")
    return req.json()['access_token']


def test_create(userid, name, mobile, test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
                        json=data
                        )
    return req.json()
    # print(req.json())


def test_get(userid, test_token):
    # userid = "zhangsan"
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
    # print(req.json())
    return req.json()


def test_update(userid, name, mobile, test_token):
    data = {
        "userid": userid,
        "mobile": mobile,
        "name": name
    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",
                        json=data
                        )
    return req.json()


def test_delete(userid, test_token):
    # userid = "zhangsan"
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    # print(req.json())
    return req.json()


def test_creat_data():
    data = [("zhangsan" + str(x),
             "张三",
             "138%08d" % x) for x in range(10)]
    # print(data)
    return data


@pytest.mark.parametrize("userid, name, mobile", test_creat_data())
def test_all(userid, name, mobile, test_token):
    try:
        assert "created" == test_create(userid, name, mobile, test_token)['errmsg']
    except AssertionError as e:
        # 如果用户手机号被使用，找到手机号的userid，并删除
        if "mobile existed" in e.__str__():
            re_userid = re.findall(":(.*)$", e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid = re_userid[:-1]
            assert "deleted" == test_delete(re_userid, test_token)['errmsg']
            assert 60111 == test_get(re_userid, test_token)['errcode']
            assert "created" == test_create(userid, name, mobile, test_token)['errmsg']
    assert name == test_get(userid, test_token)['name']
    assert "updated" == test_update(userid, "测试", mobile, test_token)['errmsg']
    assert "测试" == test_get(userid, test_token)['name']
    assert "deleted" == test_delete(userid, test_token)['errmsg']
    assert 60111 == test_get(userid, test_token)['errcode']



