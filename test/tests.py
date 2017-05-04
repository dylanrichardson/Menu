import unittest
from menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu([(None, lambda: None)])

    @unittest.expectedFailure
    def test_set_options_not_iterable(self):
        self.menu.set_options(None)

    @unittest.expectedFailure
    def test_add_option_not_tuple(self):
        self.menu.set_options([None])

    @unittest.expectedFailure
    def test_add_option_not_length_2(self):
        self.menu.set_options([(None,)])

    @unittest.expectedFailure
    def test_add_option_handler_not_callable(self):
        self.menu.set_options([(None, None)])

    def test_message_enabled(self):
        self.assertTrue(Menu([(None, lambda: None)], message="").is_message_enabled)
        self.assertFalse(Menu([(None, lambda: None)]).is_message_enabled)


if __name__ == '__main__':
    unittest.main()
