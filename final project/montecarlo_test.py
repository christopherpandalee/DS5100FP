import pandas as pd
import numpy as np
import unittest
from montecarlosim.montecarlo import CreateDice, GamePlay, AnalyzePlay


class MCTestSuite(unittest.TestCase):
    
    def test_1_change_weights(self):
        testDice1 = CreateDice(np.array(["H", "T"]))
        expected_weights = [1, 6]
        testDice1.change_weights("T", 6)
        test_assert1 = all(expected_weights == testDice1.show_current_state().weights)
        self.assertTrue(test_assert1)
        
    def test_2_change_weights(self):
        testDice2 = CreateDice(np.array([1,2,3,4,5,6]))
        expected_weights = [1,1,1,6,1,1]
        testDice2.change_weights(4,6)
        test_assert2 = all(expected_weights == testDice2.show_current_state().weights)
        self.assertTrue(test_assert2)
        
    def test_3_roll_dice(self):
        testDice3 = CreateDice(np.array(["H", "T"]))
        expected_rolls = 10
        self.assertEqual(expected_rolls, len(testDice3.roll_dice(10)))

    def test_4_show_current_state(self):
        testDice4 = CreateDice(np.array(["H", "T"]))
        expected_index = ["H", "T"]
        test_assert4 = all(expected_index == testDice4.show_current_state().index)
        self.assertTrue(test_assert4)
        
    def test_5_show_current_state(self):
        testDice5 = CreateDice(np.array(["H", "T"]))
        expected_len = 2
        self.assertEqual(expected_len, len(testDice5.show_current_state()))
        
    def test_6_show_current_state(self):
        testDice6 = CreateDice(np.array(["H", "T"]))
        expected_weights = [1,1]
        test_assert6 = all(expected_weights == testDice6.show_current_state().weights)
        self.assertTrue(test_assert6)
        
    def test_7_play_dice(self):
        testDice7 = CreateDice(np.array(["H", "T"]))
        testGame7 = GamePlay([testDice7, testDice7, testDice7])
        testGame7.play_dice(10)
        expected_num_rolls = 10
        self.assertEqual(expected_num_rolls, len(testGame7.show_results().index))
        
    def test_8_play_dice(self):
        testDice8 = CreateDice(np.array(["H", "T"]))
        testGame8 = GamePlay([testDice8, testDice8, testDice8])
        testGame8.play_dice(5)
        expected_columns = 3
        self.assertEqual(expected_columns, len(testGame8.show_results().columns))
        
    def test_9_show_results(self):
        testDice9 = CreateDice(np.array(["H", "T"]))
        testGame9 = GamePlay([testDice9, testDice9, testDice9])
        testGame9.play_dice(5)
        expected_num_rolls = 5
        expected_columns = 3
        test_assert9_1 = expected_num_rolls == len(testGame9.show_results().index)
        test_assert9_2 = expected_columns == len(testGame9.show_results().columns)
        self.assertTrue(test_assert9_1 & test_assert9_2)
        
    def test_10_find_jackpots(self):
        testDice10 = CreateDice(np.array([1]))
        testGame10 = GamePlay([testDice10, testDice10, testDice10])
        testGame10.play_dice(10)
        testAnalyze10 = AnalyzePlay(testGame10)
        expected_jackpots = 10
        self.assertEqual(expected_jackpots, testAnalyze10.find_jackpots())
        
    def test_11_find_face_counts(self):
        testDice11 = CreateDice(np.array(["H", "T"]))
        testGame11 = GamePlay([testDice11, testDice11, testDice11])
        testGame11.play_dice(5)
        testAnalyze11 = AnalyzePlay(testGame11)
        expected_count = len(testGame11.show_results().columns)
        test_count = testAnalyze11.find_face_counts().sum(axis=1)[0]
        self.assertEqual(expected_count, test_count)
        
    def test_12_count_combo(self):
        pass
    
    def test_13_count_perm(self):
        pass
    
    def test_14_roll_dice(self):
        testDice14 = CreateDice(np.array(["H", "T"]))
        self.assertIsInstance(testDice14.roll_dice(1), list)
        
    def test_15_show_current_state(self):
        testDice15 = CreateDice(np.array(["H", "T"]))
        self.assertIsInstance(testDice15.show_current_state(), pd.DataFrame)
        
    def test_16_show_results(self):
        testDice16 = CreateDice(np.array(["H", "T"]))
        testGame16 = GamePlay([testDice16, testDice16, testDice16])
        testGame16.play_dice(5)
        self.assertIsInstance(testGame16.show_results(), pd.DataFrame)
        
    def test_17_find_jackpots(self):
        testDice17 = CreateDice(np.array(["H", "T"]))
        testGame17 = GamePlay([testDice17, testDice17, testDice17])
        testGame17.play_dice(5)
        testAnalyze17 = AnalyzePlay(testGame17)
        self.assertIsInstance(testAnalyze17.find_jackpots(), int)
            
    def test_18_find_face_counts(self):
        testDice18 = CreateDice(np.array(["H", "T"]))
        testGame18 = GamePlay([testDice18, testDice18, testDice18])
        testGame18.play_dice(5)
        testAnalyze18 = AnalyzePlay(testGame18)
        self.assertIsInstance(testAnalyze18.find_face_counts(), pd.DataFrame)

    def test_19_count_combo(self):
        testDice19 = CreateDice(np.array(["H", "T"]))
        testGame19 = GamePlay([testDice19, testDice19, testDice19])
        testGame19.play_dice(5)
        testAnalyze19 = AnalyzePlay(testGame19)
        self.assertIsInstance(testAnalyze19.count_combo(), pd.DataFrame)
    
    def test_20_count_perm(self):
        testDice20 = CreateDice(np.array(["H", "T"]))
        testGame20 = GamePlay([testDice20, testDice20, testDice20])
        testGame20.play_dice(5)
        testAnalyze20 = AnalyzePlay(testGame20)
        self.assertIsInstance(testAnalyze20.count_perm(), pd.DataFrame)

    

if __name__ == '__main__':
    unittest.main(verbosity = 3)