import requests
from io import BytesIO
from PIL import Image
import json

from urllib3 import request


def seed_request():
    """发送请求"""
    """get请求"""
    re = requests.request("get", "https://www.baidu.com")
    print(re.headers)
    print("=" * 30)
    """post请求"""
    re = requests.request("post", "https://www.baidu.com")
    print(re.headers)
    print("=" * 30)
    re = requests.request("put", "https://www.baidu.com")
    print(re.headers)
    print("=" * 30)
    re = requests.request("delete", "https://www.baidu.com")
    print(re.headers)
    print("=" * 30)
    re = requests.request("head", "https://www.baidu.com")
    print(re.headers)
    re = requests.request("get", "https//www.baidu.com")
    print("=" * 30)
    re = requests.request("options", "https://www.baidu.com")
    print(re.headers)
    print("=" * 30)


# seed_request()


def url_args():
    """传递url参数"""
    payload = {"key1": "value1", "key2": "value2"}
    re = requests.get("http://httpbin.org/get", params=payload)
    print(re.url)
    """值为None不会添加到url里"""
    payload = {"key1": "value1", "key2": None}
    re = requests.get("http://httpbin.org/get", params=payload)
    print(re.url)
    """也可将列表作为值传递"""
    payload = {"key1": "value1", "key2": ["value2", "value3"]}
    re = requests.get("http://httpbin.org/get", params=payload)
    print(re.url)


# url_args()


def response_text():
    """响应内容"""
    re = requests.request("get", "https://www.baidu.com")
    print(re.text)
    """响应头"""
    print(re.headers)
    """响应内容编码"""
    print(re.encoding)
    # re.encoding = "utf-8"
    print(re.encoding)
    print(re.text)
    # print(re.content)

    """二进制响应内容"""
    # print(re.content)
    # i = Image.open(BytesIO(re.content))  # 根据响应内容生成图片
    # print(i)

    """json响应内容"""
    re = requests.get("https://api.github.com/events")
    print(re.json())
    print(re.status_code)  # 响应状态码

    """
    原始响应内容
    在请求中设置stream=True
    """
    re = requests.get("https://api.github.com/events", stream=True)
    print(re.raw)
    print(re.raw.read(30))  # 读取前30个字节
    """将原始内容写入文件"""
    with open("content.txt", "wb") as fd:
        for chunk in re.iter_content(1):
            fd.write(chunk)


# response_text()


def customized_request():
    """定制请求头"""
    url = "https://api.github.com/some/endpoint"
    headers = {"user-agent": "my-app/0.01"}
    re = requests.request(method="get", url=url, headers=headers)
    print(re.text)

    """
    复杂的post请求
    想要发送一些编码为表单形式的数据，只需简单地传递一个字典给 data 参数
    """

    def post_request():
        payload = {"key1": "value1", "key2": "value2"}
        re = requests.post("http://httpbin.org/post", data=payload)
        print(re.text)

        """也可传入元组列表"""
        payload = (("key1", "value1"), ("key1", "value2"))
        re = requests.post("http://httpbin.org/post", data=payload)
        print(re.text)

        """也可接受json数据"""
        url = "https://api.github.com/some/endpoint"
        payload = {"some": "data"}
        re = requests.post(url, data=json.dumps(payload))
        print(re.text)

    post_request()


# customized_request()


def response_status_code():
    """响应状态码"""
    url = "https://www.baidu.com"
    re = requests.get(url=url)
    print(re.status_code)
    # print(re.status_code == requests.codes)

    """如果发送一个错误请求，可通过Response.raise_for_status()，来抛出异常"""
    url = "http://httpbin.org/status/404"
    re = requests.get(url=url)
    print(re.status_code)

    # re.raise_for_status()


# response_status_code()


def response_headers():
    """响应头"""
    url = "https://www.baidu.com"
    re = requests.request("get", url=url)
    print(re.headers)
    """headers大小写不敏感"""
    print(re.headers["content-type"])
    print(re.headers["coNtent-tyPe"])


# response_headers()


def cookie():
    """cookie内容"""
    url = "https://www.baidu.com"
    re = requests.get(url=url)
    print(re.cookies)


cookie()
