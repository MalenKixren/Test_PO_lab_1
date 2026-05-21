from app.history_service import HistoryService


# Проверка сохранения одной записи
def test_save_record():

    history = HistoryService()

    history.save_record("Привет", "Ответ")

    result = history.get_history()

    assert len(result) == 1
    assert result[0]["request"] == "Привет"
    assert result[0]["response"] == "Ответ"


# Проверка пустой истории
def test_empty_history():

    history = HistoryService()

    result = history.get_history()

    assert result == []


# Проверка нескольких записей
def test_multiple_records():

    history = HistoryService()

    history.save_record("Q1", "A1")
    history.save_record("Q2", "A2")

    result = history.get_history()

    assert len(result) == 2


# Проверка порядка сохранения записей
def test_history_order():

    history = HistoryService()

    history.save_record("Первый", "Ответ1")
    history.save_record("Второй", "Ответ2")

    result = history.get_history()

    assert result[0]["request"] == "Первый"
    assert result[1]["request"] == "Второй"


# Проверка структуры записи
def test_history_structure():

    history = HistoryService()

    history.save_record("Test", "Response")

    record = history.get_history()[0]

    assert "request" in record
    assert "response" in record
