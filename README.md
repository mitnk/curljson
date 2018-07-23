# curljson

curl with pretty JSON outputs.

## Install

```
$ pip install curljson
```

## Usages

Use as `curl`:

```
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
```

Use as `python2 -m json.tool`:

```
$ echo '{"bin": "curl", "lang": "Python"}' | curljson
{
    "lang": "Python",
    "bin": "curl"
}
```
