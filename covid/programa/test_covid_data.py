import config

import unittest
from datetime import datetime
import math

from covid_data import (
    get_isciii_dframe,
    get_evolutions_by_region,
    get_evolutions_per_param,
    get_evolutions_for_spain,
)


class CovidDataTest(unittest.TestCase):
    def test_get_dframe(self):
        covid_df = get_isciii_dframe()
        assert covid_df.shape[1] == 8

    def test_filter_by_sex(self):
        covid_df = get_isciii_dframe(sex=config.FEMALE)
        assert list(covid_df.loc[:, config.ORIG_SEX_COL].unique()) == ["M"]

    def test_filter_by_date_range(self):
        start = datetime(2020, 3, 1)
        end = datetime(2020, 12, 31)
        covid_df = get_isciii_dframe(date_range=(start, end))
        assert covid_df.iloc[-1, :].loc[config.ORIG_DATE_COL].year == 2020

    def test_filter_by_age_range(self):
        covid_df = get_isciii_dframe(age_ranges=["0-9"])
        assert list(covid_df.loc[:, config.ORIG_AGE_GROUP_COL].unique()) == ["0-9"]


class EvolutionsByRegionTest(unittest.TestCase):
    def test_get_evolutions(self):
        dframes_by_region = get_evolutions_by_region(by=config.PROVINCE)
        assert "V" in dframes_by_region

        dframes_by_region = get_evolutions_by_region(by=config.COMMUNITY)
        assert "VC" in dframes_by_region

        dframes_by_region = get_evolutions_by_region(
            by=config.PROVINCE, rate_by_100k=True
        )
        assert (
            dframes_by_region["V"].loc[:, config.ORIG_DEATHS_COL].dtype.kind.lower()
            == "f"
        )


class EvolutionsPerParamTest(unittest.TestCase):
    def test_get_evolutions(self):
        res = get_evolutions_per_param()
        assert config.ORIG_DEATHS_COL in res.keys()


class EvolutionsForSpainTest(unittest.TestCase):
    def test_get_evolutions(self):
        date_range = (datetime(2020, 1, 1), datetime(2020, 3, 1))
        num_cases = get_evolutions_for_spain(date_range=date_range).sum()[
            config.ORIG_CASES_COL
        ]
        assert num_cases == 84

        num_cases_per_day = get_evolutions_for_spain(
            date_range=date_range, rate_by_100k=True
        ).loc[:, config.ORIG_CASES_COL]
        assert math.isclose(num_cases_per_day.mean(), 0.00295042475)

        num_cases_per_week = get_evolutions_for_spain(
            date_range=date_range, rate_by_100k=True, by_week=True
        ).loc[:, config.ORIG_CASES_COL]
        assert math.isclose(num_cases_per_week.mean(), 0.0196694983368209)


if __name__ == "__main__":
    unittest.main()
