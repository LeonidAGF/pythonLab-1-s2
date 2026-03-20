from src.SourceFromWeb import SourceFromWeb


def test_source_from_web():
    """
        Тесты для SourceFromWeb
    """
    sff1:SourceFromWeb = SourceFromWeb("https://ru.wikipedia.org/wiki/Python",seed=555)
    sff2:SourceFromWeb = SourceFromWeb("https://ru.wikipedia.org/wiki/Python",seed=555)
    sff3:SourceFromWeb = SourceFromWeb("fcghvjbknjlm;")

    assert len(sff1.get_tasks())!=0
    assert len(sff2.get_tasks())!=0
    assert sff1.get_tasks()[0].id==sff2.get_tasks()[0].id
    assert sff3.get_tasks() is None
