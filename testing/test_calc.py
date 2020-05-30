#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pytest
import yaml
from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('a, b, expected', yaml.safe_load(open("../data/calc_add.yaml")))
    def test_add(self, a, b, expected):
        try:
            actual_result = self.calc.add(a, b)
            assert round(actual_result, 2) == expected
        except TypeError:
            print("请输入数字")

    @pytest.mark.parametrize('a, b, expected', yaml.safe_load(open("../data/calc_sub.yaml")))
    def test_sub(self, a, b, expected):
        try:
            actual_result = self.calc.sub(a, b)
            assert round(actual_result, 2) == expected
        except TypeError:
            print("请输入数字")

    @pytest.mark.parametrize('a, b, expected', yaml.safe_load(open("../data/calc_div.yaml")))
    def test_div(self, a, b, expected):
        try:
            if b == 0:
                print("除数不能为0")
            else:
                actual_result = self.calc.div(a, b)
                assert round(actual_result, 2) == expected
        except TypeError:
            print("请输入数字")

    @pytest.mark.parametrize('a, b, expected', yaml.safe_load(open("../data/calc_mul.yaml")))
    def test_mul(self, a, b, expected):
        try:
            actual_result = self.calc.mul(a, b)
            assert round(actual_result, 2) == expected
        except TypeError:
            print("请输入数字")







