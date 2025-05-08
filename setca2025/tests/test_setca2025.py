"""
Unit and regression test for the setca2025 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import setca2025


def test_setca2025_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "setca2025" in sys.modules
