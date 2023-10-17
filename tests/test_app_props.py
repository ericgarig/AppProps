import unittest

from src.app_props import AppProps


class TestAppProps(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.filepath = "mocks/configuration.yml"

    def test_singleton_pattern(self):
        first = AppProps("", self.filepath)
        second = AppProps()
        self.assertEqual(first, second)

    def test_top_level_property(self):
        self.assertEqual(AppProps("another", self.filepath), "test value")

    def test_nests_property(self):
        self.assertEqual(
            AppProps("the.quick.brown.fox.jumps.over", self.filepath), "the lazy dog"
        )

    def test_invalid_top_level_config(self):
        with self.assertRaises(KeyError):
            AppProps("nope", self.filepath)

    def test_invalid_nested_config(self):
        with self.assertRaises(KeyError):
            AppProps("fake.path", self.filepath)

    def test_empty_value(self):
        with self.assertRaises(KeyError):
            AppProps("empty_value", self.filepath)
