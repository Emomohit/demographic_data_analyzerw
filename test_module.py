import unittest
import demographic_data_analyzer
import pandas as pd

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(False)

    def test_race_count(self):
        expected = pd.Series(
            [27816, 3124, 1039, 311, 271],
            index=['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
        )
        pd.testing.assert_series_equal(self.data['race_count'], expected)

    def test_average_age_men(self):
        self.assertAlmostEqual(self.data['average_age_men'], 39.4)

    def test_percentage_bachelors(self):
        self.assertAlmostEqual(self.data['percentage_bachelors'], 16.4)

    def test_higher_education_rich(self):
        self.assertAlmostEqual(self.data['higher_education_rich'], 46.5)

    def test_lower_education_rich(self):
        self.assertAlmostEqual(self.data['lower_education_rich'], 17.4)

    def test_min_work_hours(self):
        self.assertEqual(self.data['min_work_hours'], 1)

    def test_rich_percentage(self):
        self.assertAlmostEqual(self.data['rich_percentage'], 10.0)

    def test_highest_earning_country(self):
        self.assertEqual(self.data['highest_earning_country'], 'Iran')

    def test_highest_earning_country_percentage(self):
        self.assertAlmostEqual(self.data['highest_earning_country_percentage'], 41.9)

    def test_top_IN_occupation(self):
        self.assertEqual(self.data['top_IN_occupation'], 'Prof-specialty')


if __name__ == "__main__":
    unittest.main()