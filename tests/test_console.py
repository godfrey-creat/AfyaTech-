#!/usr/bin/python3
"""
The class TestConsoleDocs
"""

import console
import inspect
import pep8
import unittest
AfyaTechCommand = console.AfyaTechCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_AfyaTechCommand_class_docstring(self):
        """Test for the AfyaTechCommand class docstring"""
        self.assertIsNot(AfyaTechCommand.__doc__, None,
                         "AfyaTechCommand class needs a docstring")
        self.assertTrue(len(AfyaTechCommand.__doc__) >= 1,
                        "AfyaTechCommand class needs a docstring")