from src.main import main
import pytest

class TestMain:
    @pytest.mark.it("test that main function successfully brings ETL together")
    def test_main():
        pass
class TestErrorHandling:
    @pytest.mark.it("test expected failures halt script")
    def test_error():
        pass