from app.app import index


def test_index():
    response = index()
    content, status_code = response
    assert '<h1>Jojo do DevOps</h1>' in content
    assert status_code == 200