# -*- coding: utf-8 -*-

from sample_cli.sample_cli import hello, parse_virsh_list_output


def test_hello():
    assert hello() == 'hello'


out_1 = ("""
Id    Name                           State
----------------------------------------------------
 3     instance-000003db              running
 4     instance-0000047a              running
""")


out_2 = ("""
Id    Name                           State
----------------------------------------------------
 3     instance-000003db              running
 4     instance-0000047a              running
 28    instance-000009f3              running
 29    instance-00000a0b              running
 30    instance-000009f6              running
 31    instance-00000a02              running
 -     instance-00000015              shut off
""")


def test_parse_virsh_list_output():
    res_dict = {
        'instance-000003db': {
            'Id': '3',
            'Name': 'instance-000003db',
            'State': 'running',
        },
        'instance-0000047a': {
            'Id': '4',
            'Name': 'instance-0000047a',
            'State': 'running',
        },
    }

    assert parse_virsh_list_output(out_1) == res_dict
