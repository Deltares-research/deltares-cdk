from unittest import TestCase
from unittest.mock import patch, MagicMock

from aws_cdk.core import Stack

from deltarescdk.utils import get_kwargs_from_context

class TestUtils(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_get_kwargs_from_context(self) -> None:
        mock = MagicMock()
        def mock_context(value):
            values = {"a": 1, "b": 2}
            return values.get(value, None)
        mock.node.try_get_context.side_effect = mock_context

        kwargs = get_kwargs_from_context(["a", "b", "c", "d"], mock)
        assert kwargs == {
            "a": 1,
            "b": 2,
            "c": None,
            "d": None
        }
