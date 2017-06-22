# -*- coding: utf-8 -*-


def hello():
    return 'hello'


def double_space_split(in_str):
    return [res.strip() for res in in_str.split('  ') if res]


def parse_virsh_list_output(in_text, columns_count):

    # print('>>>>> in_text: {0}'.format(in_text))
    # print('>>>>>')

    lines = in_text.strip().splitlines()
    lines_count = len(lines)

    # print('>>>>> lines: {0}'.format(lines))
    # print('>>>>>')

    if lines_count < 2:
        # FIXME: change Exception type
        raise Exception
    elif lines_count == 2:
        result = []
    else:
        headers = double_space_split(lines[0])

        assert len(headers) == columns_count

        result = []

        for line in lines[2:]:

            # print('>> line: {0}'.format(line))
            # print('>>')

            values = double_space_split(line)

            # print('>> values: {0}'.format(values))
            # print('>>')

            assert len(values) == columns_count

            item = dict(zip(headers, values))
            result.append(item)

    return result
