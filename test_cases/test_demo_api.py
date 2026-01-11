import pytest
import allure
from common.request_handler import request

@allure.story("测试JSONPlaceholder的API")
class TestDemoAPI:

    @allure.title("测试获取帖子列表")
    def test_get_post(self):
        resp = request.get("/posts")
        assert resp.status_code ==200
        data = resp.json()
        assert isinstance(data,list)
        assert len(data) > 0

    @allure.title("测试创建新帖子 - 参数化")
    @pytest.mark.parametrize("title,body,userId",[
        ("PyCharm Test 1","Body 1",1),
        ("PyCharm 测试 2","正文 2",99)
    ])
    def test_creat_post(self,title,body,userId):
        payload = {"title": title,"body":body,"userId":userId}
        resp =request.post("/posts",json=payload)
        assert resp.status_code == 201
        resp_data = resp.json()
        assert  resp_data['title'] == title
        assert  resp_data['userId'] ==userId
        assert 'id' in resp_data