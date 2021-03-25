
import config

import datetime

import numpy
import pandas

from download import get_isciii_dframe
from spain_data import CA_PER_PROVINCE, POPULATIONS_PER_PROVINCE, POPULATIONS_PER_CA


def get_frame(sex=None, date_range=None):

    dframe = get_isciii_dframe()

    masks = []
    if sex is not None:
        this_mask = dframe[config.ORIG_SEX_COL] == sex
        masks.append(this_mask)
    if date_range is not None:
        masks.append(dframe[config.ORIG_DATE_COL] >= date_range[0])
        masks.append(dframe[config.ORIG_DATE_COL] < date_range[1])

    mask = None
    for one_mask in masks:
        if mask is None:
            mask = one_mask
        else:
            mask = numpy.logical_and(mask, one_mask)
        dframe = dframe.loc[mask, :]
    return dframe


def _check_by_param(by):
    if by not in (config.PROVINCE, config.COMMUNITY):
        msg = 'by should be by PROVINCE or by COMMUNITY'
        raise ValueError(msg)


def get_evolutions_by_region(by_week=False, by=config.PROVINCE, sex=None,
                             date_range=None, rate_by_100k=False):

    _check_by_param(by)

    dframe = get_frame(sex=sex, date_range=date_range)    

    if by == config.PROVINCE:
        dframes = {prov: prov_dframe for prov, prov_dframe in dframe.groupby(by=config.ORIG_PROVINCE_COL, as_index=False)}
    else:
        communities = numpy.array([CA_PER_PROVINCE.get(prov) for prov in dframe[config.ORIG_PROVINCE_COL]])
        dframes = {prov: prov_dframe for prov, prov_dframe in dframe.groupby(by=communities, as_index=False)}

    evolutions = {region: dframe.groupby(by=config.ORIG_DATE_COL).sum()  for region, dframe in dframes.items()}

    if by_week:
        evolutions = {region: evol.resample('7D').sum() for region, evol in evolutions.items()}

    if rate_by_100k:
        if by == config.PROVINCE:
            populations = POPULATIONS_PER_PROVINCE
        else:
            populations = POPULATIONS_PER_CA

        evolutions = {region: evol / populations[region] for region, evol in evolutions.items()}

    return evolutions


def get_evolutions_per_param(by=config.PROVINCE, sex=None, date_range=None,
                             rate_by_100k=False, by_week=False):
    _check_by_param(by)
    dframe = get_frame(sex=sex, date_range=date_range)    

    if by == config.PROVINCE:
        regions = dframe[config.ORIG_PROVINCE_COL].values
    else:
        regions = numpy.array([CA_PER_PROVINCE.get(prov) for prov in dframe[config.ORIG_PROVINCE_COL]])

    evolutions_by_param = {}
    for param in config.ORIG_COUNT_COLS:
        param = config.ORIG_CASES_COL
        dframe2 = pandas.DataFrame({by: regions,
                                    param: dframe[param].values,
                                    'date': dframe[config.ORIG_DATE_COL].values})
        evolutions_by_param[param] = dframe2.groupby(by=['date', by]).sum().unstack(level=1)
        evolutions_by_param[param].columns = evolutions_by_param[param].columns.to_frame().iloc[:, 1].values
    if by_week:
        evolutions_by_param = {param: evol.resample('7D').sum() for region, evol in evolutions_by_param.items()}

    if rate_by_100k:
        if by == config.PROVINCE:
            region_populations = POPULATIONS_PER_PROVINCE
        else:
            region_populations = POPULATIONS_PER_CA
        populations = numpy.array([region_populations[region] for region in evolutions_by_param[param].columns])
        evolutions_by_param = {param: evolution.div(populations, axis=1) for param, evolution in evolutions_by_param.items()}
    return evolutions_by_param


if __name__ == '__main__':
    last_day = datetime.datetime.now() - datetime.timedelta(days=7)
    first_day = last_day - datetime.timedelta(days=15)

    get_evolutions_by_region(by_week=True, sex=config.MALE,
                             date_range=(first_day, last_day),
                             by=config.COMMUNITY, rate_by_100k=True)

    get_evolutions_per_param(by_week=True, sex=config.MALE,
                             date_range=(first_day, last_day),
                             by=config.COMMUNITY, rate_by_100k=True)

    
    