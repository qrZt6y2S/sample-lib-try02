# -*- coding: utf-8 -*-


def hello():
    return 'hello'


def parse_virsh_list_output(input_text):
    out = input_text.strip()
    lines = out.splitlines()
    headers = lines[0].split()
    result = []
    if len(lines) > 2:
        for line in lines[2:]:
            values = line.split()
            item = dict(zip(headers, values))
            result.append(item)

    return {res_dict['Name']: res_dict for res_dict in result}
