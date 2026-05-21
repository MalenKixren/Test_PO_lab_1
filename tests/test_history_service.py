from app.history_service import HistoryService


def test_save_record():

    history = HistoryService()

    history.save_record("Привет", "Ответ")

    result = history.get_history()

    assert len(result) == 1
    assert result[0]["request"] == "Привет"
    assert result[0]["response"] == "Ответ"