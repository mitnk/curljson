from setuptools import setup

DESC = """
Home Page: https://github.com/mitnk/curljson

Install
-------

::

    $ pip install curljson

Usages
------

::

    $ curljson -i https://httpbin.org/get
    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: gunicorn/19.8.1
    Date: Mon, 23 Jul 2018 22:46:53 GMT
    Content-Type: application/json
    Content-Length: 166
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Credentials: true
    Via: 1.1 vegur

    {
        "headers": {
            "Accept": "*/*",
            "Host": "httpbin.org",
            "User-Agent": "curl/7.43.0",
            "Connection": "close"
        },
        "origin": "12.13.7.19",
        "args": {},
        "url": "https://httpbin.org/get"
    }

    $ echo '{"bin": "curl", "lang": "Python"}' | curljson
    {
        "lang": "Python",
        "bin": "curl"
    }
"""

setup(
    name='curljson',
    version='0.9.1',

    description='curl with pretty json outputs',
    long_description=DESC,

    url='https://github.com/mitnk/curljson',
    author='mitnk',
    author_email='w@mitnk.com',
    license='MIT',
    keywords='curl json pretty',
    py_modules=["curljson"],
    entry_points={
        'console_scripts': [
            'curljson=curljson:main',
        ],
    },
)
