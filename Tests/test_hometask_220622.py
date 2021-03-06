import unittest
from parameterized import parameterized

import modified_app
from modified_app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf
from modified_app import add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf
from modified_app import show_document_info, show_all_docs_info, add_new_doc, secretary_program_start


class TestApp(unittest.TestCase):
    #test function 1 (unittest)
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

    #test function 2 (unittest)
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

    #test function 3 (unittest)
    @parameterized.expand(
        [
            ("Василий Гупкин", {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}),
            ("Геннадий Покемонов", {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}),
            ("Аристарх Павлов", {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})
        ]
    )
    def test_function_3(self, user, dict_user):
        dict_user = get_all_doc_owners_names()
        self.assertIn(user, dict_user)

    @parameterized.expand(
        [
            ("", {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}),
            ("757556", {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}),
            ("!+_/", {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})
        ]
    )

    def test_function_3(self, user, dict_user):
        dict_user = get_all_doc_owners_names()
        self.assertNotIn(user, dict_user)

    # test function 4 (unittest) - successfully
    @parameterized.expand(
        [
            ('1', ['2207 876234', '11-2', '5455 028765']),
            ('2', ['10006']),
            ('3', [])
        ]
    )
    def test_function_4(self, doc_number, doc_list):
        remove_doc_from_shelf(doc_number)
        self.assertNotIn(doc_number, doc_list)


    #test function 5 (unittest) - successfully
    @parameterized.expand(
        [
            ("1", True, True),
            ("2", True, True),
            ("3", True, True),
            ("4", True, True),
            ("888", True, True)
        ]
    )

    def test_function_5(self, shelf_number, bool_res, bool_result):
        self.assertEqual(add_new_shelf(shelf_number, bool_res), (shelf_number, bool_result))
        

    #test function 6 (unittest) - successfully
    @parameterized.expand(
        [
            ("123", '1'),
            ("456-s", '2'),
            ("23_57-ds", '3'),
            ("987654321", '4'),
            ("dfg-6868-24", '59')
        ]
    )

    def test_function_6(self, doc_number, shelf_number):
        dict_dir = append_doc_to_shelf(doc_number, shelf_number)
        self.assertIn(doc_number, dict_dir[shelf_number])

    # test function 7 (unittest) - successfully
    @parameterized.expand(
        [
            ('11-2', '1'),
            ('10006', '2'),
            ('2207 876234', '1')
        ]
    )

    def test_function_7(self, user_doc_number, shelf_number):
        dict_dir = delete_doc(user_doc_number)
        self.assertNotIn(user_doc_number, dict_dir[shelf_number])

    #test function 8 (unittest)
    @parameterized.expand(
        [
            ('11-2', '1'),
            ('10006', '2'),
            ('2207 876234', '1')
        ]
    )

    def test_function_8(self, user_doc_number, shelf_number):
        dir_num, dict_dir = get_doc_shelf(user_doc_number)
        self.assertIn(user_doc_number, dict_dir[shelf_number])


    #function 9 (composite function) - already tested in function 4 and function 6.

    #test function 10 (unittest)
    def test_function_10(self, type="type", number="number", name="name"):
        doc_list = modified_app.documents
        for doc in doc_list:
            self.assertEqual(show_document_info(doc), f'"{doc[type]}" "{doc[number]}" "{doc[name]}"')

    #test function 11 (unittest)
    def test_function_11(self):
        self.assertEqual(modified_app.documents[0]['type'], "passport")
        self.assertEqual(modified_app.documents[0]['number'], "2207 876234")
        self.assertEqual(modified_app.documents[0]['name'], "Василий Гупкин")
        self.assertEqual(modified_app.documents[1]['type'], "invoice")
        self.assertEqual(modified_app.documents[1]['number'], "11-2")
        self.assertEqual(modified_app.documents[1]['name'], "Геннадий Покемонов")
        self.assertEqual(modified_app.documents[2]['type'], "insurance")
        self.assertEqual(modified_app.documents[2]['number'], "10006")
        self.assertEqual(modified_app.documents[2]['name'], "Аристарх Павлов")

    #test function 12 (unittest)
    def test_function_12(self):
        add_new_doc('order', '8888/2022', 'Petrov', '4')
        self.assertTrue(modified_app.documents[3]['type'])
        self.assertEqual(modified_app.documents[3]['type'], 'order')
        self.assertTrue(modified_app.documents[3]['number'])
        self.assertEqual(modified_app.documents[3]['number'], '8888/2022')
        self.assertTrue(modified_app.documents[3]['name'])
        self.assertEqual(modified_app.documents[3]['name'], 'Petrov')
        self.assertEqual(modified_app.directories['4'], ['8888/2022'])