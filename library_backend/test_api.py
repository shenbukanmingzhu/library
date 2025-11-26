import requests

BASE_URL = 'http://localhost:5000/api'

def test_add_category():
    print("测试创建分类")
    res = requests.post(f'{BASE_URL}/categories', json={
        'name': '小说',
        'description': '虚构文学'
    })
    print(f"状态码：{res.status_code}")  # 打印状态码（201成功，404路径错，500服务器错）
    print(f"原始响应：{res.text}")  # 打印原始内容（看是否是HTML或错误信息）
    # 仅在状态码为200/201时解析JSON
    if res.status_code in [200, 201]:
        print(res.json())

def test_user_register():
    print("测试用户注册")
    res = requests.post(f'{BASE_URL}/users/register', json={
        'username': 'test_user',
        'password': '123456'
    })
    print(res.json())

def test_add_category():
    print("测试创建分类")
    res = requests.post(f'{BASE_URL}/categories', json={
        'name': '小说',
        'description': '虚构文学'
    })
    print(res.json())

def test_add_book():
    print("测试新增图书")
    res = requests.post(f'{BASE_URL}/books', json={
        'title': '活着',
        'author': '余华',
        'isbn': '9787506332808',
        'stock': 10,
        'category_id': 1  # 假设分类ID=1
    })
    print(res.json())

def test_borrow_book():
    print("测试借书")
    res = requests.post(f'{BASE_URL}/borrows/borrow', json={
        'user_id': 1,  # 假设用户ID=1
        'book_id': 1   # 假设图书ID=1
    })
    print(res.json())

def test_search_books():
    print("测试搜索图书")
    res = requests.get(f'{BASE_URL}/search/books?keyword=余华')
    print(res.json())

if __name__ == '__main__':
    test_user_register()
    test_add_category()
    test_add_book()
    test_borrow_book()
    test_search_books()