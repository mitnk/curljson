import fileinput
import json
import subprocess
import sys


def get_cmd_output(cmd):
    return subprocess.check_output(
        cmd,
        stderr=subprocess.PIPE,
    )


def main():
    cmd = ['curl'] + sys.argv[1:]
    if len(cmd) == 1:
        stream_func = fileinput.input
        stream_args = []
    else:
        for opt in ('-s', '-S', '-L'):
            if opt not in cmd:
                cmd.append(opt)
        try:
            output = get_cmd_output(cmd)
            output = output.decode(errors='replace')
        except subprocess.CalledProcessError as e:
            try:
                print(e.stderr.decode(errors='replace').strip())
            except AttributeError:
                # e.stderr only available in PY3
                print('{}'.format(e))
            exit(e.returncode)
        stream_func = output.strip().split
        stream_args = ['\n', ]

    header_lines = []
    body_str = ''
    body_lines = []
    http_version_found = False

    for line in stream_func(*stream_args):
        line = line.strip()
        if line.startswith(r'HTTP/'):
            http_version_found = True

        if http_version_found and not line.replace('\r', ''):
            header_lines.append('\n')
            http_version_found = False

        if http_version_found:
            header_lines.append(line)
        else:
            body_str += line
            body_lines.append(line)

    if header_lines:
        headers = '\n'.join(header_lines).replace('\n\n', '\n')
        print(headers)

    try:
        result = json.loads(body_str)
    except ValueError:
        body = '\n'.join(body_lines)
        print(body.strip())
    else:
        print(json.dumps(result, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
