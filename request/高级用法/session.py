from io import RawIOBase
import requests

"""
会话对象
"""


def session():
    """会跨请求保持session"""
    s = requests.session()

    s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
    r = s.get("http://httpbin.org/cookies")

    print(r.text)

    s.auth = ("user", "pass")

    """为请求方法提供缺省数据,该数据会跨请求保留"""
    s.headers.update({"x-test": "true"})
    r = s.get("http://httpbin.org/headers")
    print(r.text)

    r = s.get("http://httpbin.org/headers", headers={"x-test2": "true"})
    print(r.text)

    """但方法级别的数据不会被跨请求保留"""
    s = requests.session()
    r = s.get("http://httpbin.org/cookies", cookies={"my-cookies": "hahahah"})
    print(r.text)

    r = s.get("http://httpbin.org/cookies")
    print(r.text)


# session()


def request_and_response():
    """响应对象包含服务器返回的所有信息，也包含你原来创建的 Request 对象"""
    r = requests.get("https://bilibili.com")

    """获取响应头"""
    print(r.headers)
    """获取请求头"""
    print(r.request.headers)


# request_and_response()


def certificate():
    """SSL证书验证，默认开启"""
    # r = requests.get("https://requestb.in")
    # print(r)

    r = requests.get("https://github.com", verify=True)
    print(r)

    """也可忽略证书验证"""
    r = requests.get("https://requestb.in", verify=False)
    print(r)

    """也可输入CA证书路径"""
    # r = requests.get("https://github.com", verify="/path/to/certfile")
    print(r)

    """让CA证书保存在session中"""
    s = requests.Session()
    # s.verify = "/path/to/certfile"
    r = requests.get("https://github.com")
    print(r)

    """客户端证书"""
    s.cert = "/path/client.cert"
    # r = s.get("https://kennethreitz.org")
    print(r)


# certificate()


def response_text():
    """可推迟响应体下载，直到响应体访问content属性"""
    url = "https://github.com/kennethreitz/requests/tarball/master"
    """将stream设置为TRUE可推迟响应主体下载"""
    r = requests.get(url=url, stream=True)
    print(r.headers)

    """如果需要部分下载响应主体，可使用with上下文管理，下载下来的是未编码的原始内容"""
    with requests.get(url=url, stream=True) as re:
        content = re.content
        print(content)


# response_text()


def stream():
    """可流式上传文件数据"""
    with open("body.json", "br") as f:
        s = requests.Session()
        s.get("http://some.url/streamed", data=f)

    r = s.get("http://some.url/streamed")
    print(r.content)
