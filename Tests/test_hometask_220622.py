import unittest
from parameterized import parameterized
from modified_app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf
from modified_app import add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf
from modified_app import show_document_info, show_all_docs_info, add_new_doc, secretary_program_start


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        print("SetUp method")

    def tearDown(self) -> None:
        print("TearDown method")

    @classmethod
    def setUpClass(cls) -> None:
        print('==> setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('==> tearDownClass')

    # Tests - function 1
    @parameterized.expand(
        [
            ("2207 876234", True),
            ("11-2", True),
            ("10006", True),
            (10006, False),
            ("5455 028765", False),
            ("000011", False),
            ("", False),
            ("****_", False),
        ]
    )

    def test_function_1(self, doc_number, bool_result):
        self.assertEqual(check_document_existance(doc_number), bool_result)

    # Tests - function 2
    @parameterized.expand(
        [
            ("2207 876234", "Василий Гупкин"),
            ("11-2", "Геннадий Покемонов"),
            ("10006", "Аристарх Павлов"),
            (None, None)
        ]
    )
    def test_function_2(self, user_doc_number, owner_name):
        self.assertEqual(get_doc_owner_name(user_doc_number), owner_name)

    @parameterized.expand(
        [
            (10006, "Аристарх Павлов"),
            ("", "Геннадий Покемонов"),
            ("2207 876234", ""),
            ("", ""),
            ("11-2", 6768688),
            ("11-2", None),
            (None, "Василий Гупкин")
        ]
    )
    def test_function_2(self, user_doc_number, owner_name):
        self.assertNotEqual(get_doc_owner_name(user_doc_number), owner_name)