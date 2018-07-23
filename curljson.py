import subprocess
import json
import sys
import fileinput


def get_cmd_output(cmd):
    return subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
    ).decode()


def main():
    cmd = ['curl'] + sys.argv[1:]
    if len(cmd) == 1:
        stream_func = fileinput.input
        stream_args = []
    else:
        if '-s' not in cmd:
            cmd.append('-s')
        if '-L' not in cmd:
            cmd.append('-L')
        try:
            output = get_cmd_output(cmd)
        except subprocess.CalledProcessError as e:
            print('CalledProcessError: {}'.format(e))
            exit(e.returncode)
        stream_func = output.strip().split
        stream_args = ['\n', ]

    response_spliter_found = False
    raw_lines = []
    json_str = ''

    for line in stream_func(*stream_args):
        line = line.strip()
        if len(line.replace('\r', '')) == 0:
            response_spliter_found = True
            raw_lines.append('\n')
        elif line.startswith(r'HTTP/'):
            response_spliter_found = False

        if response_spliter_found:
            json_str += line
        else:
            raw_lines.append(line)

    if response_spliter_found:
        for line in raw_lines:
            if line == '\n':
                print('')
            else:
                print(line)
    else:
        json_str = '\n'.join(raw_lines)

    try:
        result = json.loads(json_str)
    except ValueError:
        print(json_str)
    else:
        print(json.dumps(result, indent=4))


if __name__ == '__main__':
    main()
