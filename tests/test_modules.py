from src.calidad import WebServiceModule, DataProcessingModule
import pytest

def test_webservice_validate_and_docs():
    ws = WebServiceModule(name="TestAPI", owner="QA", base_url="/api/v1")
    ws.validate()
    ws.bump_version(minor=1)
    assert "Versión" in ws.generate_docs()

def test_dataproc_validation_bounds():
    with pytest.raises(ValueError):
        DataProcessingModule(name="Bad", owner="QA", batch_size=0).validate()
    good = DataProcessingModule(name="Good", owner="QA", batch_size=10)
    good.validate()
