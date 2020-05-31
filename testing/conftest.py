#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest


def pytest_collection_modifyitems(session, config, items: list):
    for item in items:
        # 添加标记
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif "sub" in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif "mul" in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif "div" in item.nodeid:
            item.add_marker(pytest.mark.div)