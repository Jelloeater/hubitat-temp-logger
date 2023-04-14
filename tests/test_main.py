import os

from dotenv import load_dotenv

import temp_logger.__main__ as pl

load_dotenv()
os.environ.setdefault("PL_TEST_MODE", str(True))  # To break out of color cycle loop


class TestPL:
    def test_check_hub(self):
        assert pl.check_hub().devices is not None
