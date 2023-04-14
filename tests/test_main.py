import os

from dotenv import load_dotenv

import temp_logger.__main__ as pl

load_dotenv()
os.environ.setdefault("PL_TEST_MODE", str(True))


class TestMain:
    def test_check_hub(self):
        assert pl.check_hub().devices is not None
