#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pytest
import yaml
from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.run(order=2)
    # @pytest.mark.add
    @pytest.mark.parametrize('a, b, expected', yaml.safe_load(open("../data/calc_add.yaml")))
    def calc_add(self, a, b, expected):
        try:
            actual_result = self.calc.add(a, b)
            assert round(actual_result, 2) == expected
        except TypeError:
            print("请输入数字")

    @pytest.mark.run(order=1)
    # @pytest.mark.sub
    @pytest.mark.parametrize('a, b, expected', yaml.safe_load(open("../data/calc_sub.yaml")))
    def calc_sub(self, a, b, expected):
        try:
            actual_result = self.calc.sub(a, b)
            assert round(actual_result, 2) == expected
        except TypeError:
            print("请输入数字")

    @pytest.mark.run(order=3)
    # @pytest.mark.div
    @pytest.mark.parametrize('a, b, expected', yaml.safe_load(open("../data/calc_div.yaml")))
    def calc_div(self, a, b, expected):
        try:
            if b == 0:
                print("除数不能为0")
            else:
                actual_result = self.calc.div(a, b)
                assert round(actual_result, 2) == expected
        except TypeError:
            print("请输入数字")

    @pytest.mark.run(order=4)
    # @pytest.mark.div
    @pytest.mark.parametrize('a, b, expected', yaml.safe_load(open("../data/calc_mul.yaml")))
    def calc_div(self, a, b, expected):
        try:
            actual_result = self.calc.mul(a, b)
            assert round(actual_result, 2) == expected
        except TypeError:
            print("请输入数字")


# if __name__ == '__main__':
    # pytest.main(["-m", "test_calc.py::TestCalc::div"])
