import numpy as np
import pytest

from simple_functions import pi


class TestPi:

    def test_pi(self):
        assert pi(2) == pytest.approx(np.pi, abs=1e-12)
