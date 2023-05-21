from tests.questions import constants_question as const


def test_first_post(client):
    """Добавление первого вопроса в БД."""
    response = client.post(f'/question/?questions_num={const.COUNT}')

    assert response.status_code == 200
    assert response.json()['question'] is None


def test_second_post(client):
    """Добавление второго и последующих вопросов в БД."""
    response = client.post(f'/question/?questions_num={const.COUNT}')

    assert response.status_code == 200
    assert response.json()['question'] is not None
