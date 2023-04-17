import os

from dotenv import load_dotenv

import temp_logger.__main__ as tl

load_dotenv()
os.environ.setdefault("PL_TEST_MODE", str(True))


class TestMain:
    def test_check_hub(self):
        assert tl.Main.get_hub().devices is not None
