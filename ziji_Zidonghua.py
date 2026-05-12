import requests
#登录b站
def test_bilibili_login():
    """
    B站 登录状态自动化测试
    """
    # 接口地址
    url = "https://api.bilibili.com/x/web-interface/nav"

    # 你自己的 SESSDATA（保持你之前复制的不变）
    cookie_sessdata = "a9333e01%2C1792561898%2C5b5a2%2A41CjCW1WBKH3TKPR2LS3J_Weq4CWvhc0pEngvYEH5B4yD1TYP_NxG_Qsli9H9awG9_ILkSVkxOX3lSVlhpVlBKc3ozSmJQY0d3S2FXNE1EME5DYWtGLWk0bk4xUEVFaWFmNWZNXy1CanlucUd2LTZvcjYzekNJTGg1VzVBZUlnR0VoX0FCVHQzZWd3IIEC"

    # 请求头（标准格式）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": f"SESSDATA={cookie_sessdata}"
    }

    try:
        # 发送请求
        res = requests.get(url, headers=headers, timeout=10)
        json_data = res.json()

        # 断言：判断是否登录成功（自动化测试核心！）
        assert res.status_code == 200, "❌ 请求失败"
        assert json_data["code"] == 0, "❌ 接口返回错误"
        assert json_data["data"]["isLogin"] is True, "❌ 未登录成功"

        # 打印信息
        print("=" * 50)
        print("✅ B站接口自动化测试 通过！")
        print(f"👤 用户名：{json_data['data']['uname']}")
        print(f"🆔 UID：{json_data['data']['mid']}")
        print("=" * 50)

    except Exception as e:
        print("❌ 测试失败：", e)

# 运行测试
if __name__ == "__main__":
    test_bilibili_login()