"""This test suite includes a few basic test cases to verify your solution. However, passing these
tests does not guarantee that your solution is correct. The Project Asssistant test suite contains
many additional test cases that you must also pass to complete the project. You should write your
own additional test cases to cover any failed tests shown in the Project Assistant feedback.
"""
import unittest
import solution
from utils import *


class TestNakedTwins(unittest.TestCase):
    before_naked_twins_1 = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
                            'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
                            'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23', 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
                            'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'A4': '2357', 'A7': '27',
                            'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
                            'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2',
                            'F6': '125', 'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '379', 'F1': '6',
                            'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'E2': '37', 'F7': '35', 'F8': '9',
                            'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17', 'D3': '2379', 'B4': '27',
                            'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279',
                            'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
    possible_solutions_1 = [
        {'G7': '6', 'G6': '3', 'G5': '2', 'G4': '9', 'G3': '1', 'G2': '8', 'G1': '7', 'G9': '5', 'G8': '4', 'C9': '1',
         'C8': '5', 'C3': '8', 'C2': '237', 'C1': '23', 'C7': '9', 'C6': '6', 'C5': '37', 'A4': '2357', 'A9': '8',
         'A8': '6', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'F6': '125', 'F7': '35', 'F8': '9',
         'F9': '7', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'C4': '4',
         'B8': '3', 'B9': '4', 'I9': '9', 'I8': '7', 'I1': '23', 'I3': '23', 'I2': '6', 'I5': '5', 'I4': '8', 'I7': '1',
         'I6': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'E8': '1', 'A7': '27', 'A6': '257', 'E5': '347',
         'E4': '6', 'E7': '345', 'E6': '579', 'E1': '8', 'E3': '79', 'E2': '37', 'H8': '2', 'H9': '3', 'H2': '9',
         'H3': '5', 'H1': '4', 'H6': '17', 'H7': '8', 'H4': '17', 'H5': '6', 'D8': '8', 'D9': '6', 'D6': '279',
         'D7': '34', 'D4': '237', 'D5': '347', 'D2': '1', 'D3': '79', 'D1': '5'},
        {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8', 'H5': '6', 'F9': '7',
         'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8', 'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
         'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5', 'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9',
         'A4': '2357', 'A7': '27', 'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
         'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2', 'F6': '125',
         'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '79', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
         'F5': '8', 'E2': '3', 'F7': '35', 'F8': '9', 'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17',
         'D3': '79', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6',
         'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
        ]

    before_naked_twins_2 = {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
                            'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237',
                            'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5', 'C3': '1', 'C4': '23', 'C5': '379',
                            'C6': '2379', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8', 'D2': '17', 'D3': '9',
                            'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
                            'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9',
                            'F1': '4', 'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
                            'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345',
                            'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7', 'H2': '2', 'H3': '4', 'H4': '9',
                            'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3', 'I3': '5',
                            'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
    possible_solutions_2 = [
        {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9', 'A9': '1', 'B1': '6',
         'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237', 'B8': '5', 'B9': '237', 'C1': '23',
         'C2': '5', 'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
         'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
         'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9', 'F1': '4',
         'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6', 'F8': '8', 'F9': '257', 'G1': '1',
         'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
         'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3',
         'I3': '5', 'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'},
        {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9', 'A9': '1', 'B1': '6',
         'B2': '9', 'B3': '8', 'B4': '4', 'B5': '3', 'B6': '1', 'B7': '237', 'B8': '5', 'B9': '237', 'C1': '23',
         'C2': '5', 'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
         'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
         'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9', 'F1': '4',
         'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6', 'F8': '8', 'F9': '257', 'G1': '1',
         'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
         'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3',
         'I3': '5', 'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
    ]


    pa_case = {"H9": "4", "F5": "12358", "G1": "7", "F2": "12345789", "G9": "5689", "E4": "135689",
         "C9": "56", "F4": "123589", "I9": "578", "C2": "1245689", "A6": "2345689", "I6": "12458", "H3": "1",
         "G7": "1569", "C8": "3", "I8": "27", "F8": "6", "A4": "23456789", "E9": "2", "E7": "159",
         "H6": "23568", "F9": "3579", "B9": "567", "B8": "9", "G8": "15", "A5": "235678", "B2": "123456",
         "I2": "458", "G4": "134568", "H5": "235678", "D3": "3459", "D4": "123569", "H7": "25679", "A8": "4",
         "H4": "235678", "C5": "12568", "C6": "1245689", "B5": "123567", "I4": "124578", "H2": "3589", "D7": "14579",
         "A2": "2345689", "D9": "3579", "G5": "13568", "D8": "8", "F3": "34589", "H1": "3589", "C7": "2456", "D1": "1234569",
         "H8": "27", "D6": "123569", "B3": "345", "D2": "12345679", "A7": "24567", "B7": "8", "B4": "1234567",
         "G6": "134568", "G3": "2", "F1": "1234589", "E2": "135689", "E5": "4", "E1": "135689", "A9": "1",
         "C3": "7", "F7": "14579", "I1": "458", "B6": "123456", "A1": "2345689", "I3": "6", "A3": "34589",
         "E3": "3589", "G2": "34589", "C1": "1245689", "B1": "123456", "F6": "123589", "I7": "3", "E8": "15", "C4": "1245689",
         "D5": "12356", "E6": "7", "I5": "9"}


    pa_case_sol = {"F5": "12358", "F2": "12345789", "F4": "123589", "D2": "12345679", "C2": "1245689", "B2": "123456", "I6": "12458", "I8": "27", "H1": "3589",
     "D7": "14579", "F9": "3579", "B9": "567", "D9": "3579", "H6": "23568", "D4": "123569", "H7": "25679", "A7": "24567",
      "C6": "1245689", "H4": "235678", "H2": "3589", "D5": "12356", "G5": "13568", "I4": "124578", "C7": "2456", "H8": "27",
       "D6": "123569", "B7": "8", "B4": "1234567", "G3": "2", "I2": "458", "E2": "135689", "F7": "14579", "I1": "458", "C3": "7",
       "A1": "2345689", "I3": "6", "E3": "3589", "G2": "34589", "B1": "123456", "F6": "123589", "B6": "123456", "E6": "7",
        "I5": "9", "G1": "7", "G9": "5689", "E4": "135689", "I9": "58", "A9": "1", "A6": "2345689", "H3": "1", "C9": "56",
        "F8": "6", "A4": "23456789", "E9": "2", "E7": "159", "B8": "9", "A3": "34589", "A5": "235678", "G7": "1569",
        "G4": "134568", "H5": "235678", "D3": "3459", "C5": "12568", "G6": "134568", "B5": "123567", "F3": "34589",
        "A2": "2345689", "C8": "3", "D8": "8", "H9": "4", "D1": "1234569", "B3": "345", "G8": "15", "F1": "1234589",
         "E5": "4", "E1": "135689", "A8": "4", "C1": "1245689", "I7": "3", "E8": "15", "C4": "1245689"}


    grid_2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

    def test_naked_twins1(self):
        x = solution.naked_twins(self.pa_case)
        print('Old')
        display(self.pa_case)
        print('Solved')
        display(x)
        self.assertTrue(x in "", "The test just passed")

    # def test_get_twins_within_unit(self):
    #     self.assertTrue(solution.get_twins_within_unit('I1', 'I3') )

    # def test_naked_twins(self):
    #     x = solution.naked_twins(self.before_naked_twins_1)
    #     display(self.before_naked_twins_1)
    #     display(x)
    #     print()
    #     print('=======================Sol=1========================')
    #     print()
    #     display(self.possible_solutions_1[0])
    #     print()
    #     print('=======================Sol=2========================')
    #     print()
    #     display(self.possible_solutions_1[1])
    #     self.assertTrue(x in self.possible_solutions_1,
    #                     "Your naked_twins function produced an unexpected board.")

    #
    def test_naked_twins2(self):
        self.assertTrue(solution.naked_twins(self.before_naked_twins_2) in self.possible_solutions_2,
                        "Your naked_twins function produced an unexpected board.")
# class TestGetTwinsCommonPeers(unittest.TestCase):
#     def test_get_twins_common_peers(self):
#         self.assertTrue( in ,
#                         "")
# class TestEliminate(unittest.TestCase):
#     def test_eliminate(self):
#         self.assertTrue( in ,
#                         "")
# class TestsOnlyChoice(unittest.TestCase):
#     def test_only_choice(self):
#         self.assertTrue( in ,
#                         "")
# class TestReducePuzzle(unittest.TestCase):
#     def test_reduce_puzzle(self):
#         self.assertTrue( in ,
#                         "")
# class TestSearch(unittest.TestCase):
#     def test_search(self):
#         self.assertTrue( in ,
#                         "")
# class TestSolve(unittest.TestCase):
#     def test_solve(self):
#         self.assertTrue( in ,
#                         "")

class TestDiagonalSudoku(unittest.TestCase):
    diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    solved_diag_sudoku = {'G7': '8', 'G6': '9', 'G5': '7', 'G4': '3', 'G3': '2', 'G2': '4', 'G1': '6', 'G9': '5',
                          'G8': '1', 'C9': '6', 'C8': '7', 'C3': '1', 'C2': '9', 'C1': '4', 'C7': '5', 'C6': '3',
                          'C5': '2', 'C4': '8', 'E5': '9', 'E4': '1', 'F1': '1', 'F2': '2', 'F3': '9', 'F4': '6',
                          'F5': '5', 'F6': '7', 'F7': '4', 'F8': '3', 'F9': '8', 'B4': '7', 'B5': '1', 'B6': '6',
                          'B7': '2', 'B1': '8', 'B2': '5', 'B3': '3', 'B8': '4', 'B9': '9', 'I9': '3', 'I8': '2',
                          'I1': '7', 'I3': '8', 'I2': '1', 'I5': '6', 'I4': '5', 'I7': '9', 'I6': '4', 'A1': '2',
                          'A3': '7', 'A2': '6', 'E9': '7', 'A4': '9', 'A7': '3', 'A6': '5', 'A9': '1', 'A8': '8',
                          'E7': '6', 'E6': '2', 'E1': '3', 'E3': '4', 'E2': '8', 'E8': '5', 'A5': '4', 'H8': '6',
                          'H9': '4', 'H2': '3', 'H3': '5', 'H1': '9', 'H6': '1', 'H7': '7', 'H4': '2', 'H5': '8',
                          'D8': '9', 'D9': '2', 'D6': '8', 'D7': '1', 'D4': '4', 'D5': '3', 'D2': '7', 'D3': '6',
                          'D1': '5'}

    def test_solve(self):
        self.assertEqual(solution.solve(self.diagonal_grid), self.solved_diag_sudoku)

if __name__ == '__main__':
    unittest.main()