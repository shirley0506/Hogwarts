#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

import pytest
import requests


@pytest.fixture(scope='session')
def test_token():
    corpid = 'wwb9dd59b36dfb3ab0'
    corpsecret = 'Bg-l59yCtimW-H8rBSiRC_IWDsF07awtF0UGTtb3KuU'
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    print("test_token")
    return req.json()['access_token']


def test_create(userid, name, mobile):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": 1
    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
                        json=data
                        )
    return req.json()
    # print(req.json())


def test_get():
    userid = "zhangsan"
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
    # print(req.json())


def test_delete(userid):
    # userid = "zhangsan"
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return req.json()


@pytest.mark.parametrize("userid, name, mobile", [("zhangsan1", "张三1", "12345678902")])
def test_all(userid, name, mobile):
    try:
        assert "created" == test_create(userid, name, mobile)['errmsg']
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            re_userid = re.findall(":(.*)'$", e.__str__())[0]
            assert "deleted" == test_delete(userid)['errmsg']

