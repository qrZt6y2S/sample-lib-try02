# -*- coding: utf-8 -*-

from sample_cli.my_math import sample_sum


def test_sample_sum():
    assert sample_sum(123, 321) == 444
