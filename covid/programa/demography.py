
import config

import numpy
import pandas

import spain_data

NUM_PEOPLE_COL = 'Num. personas'

PROVINCE_MAP = {'Alicante/Alacant': 'Alicante',
                'Araba/Álava': 'Álava',
                'Balears, Illes': 'Baleares',
                'Bizkaia': 'Vizcaya',
                'Castellón/Castelló': 'Castellón',
                'Coruña, A': 'La Coruña',
                'Gipuzkoa': 'Guipúzcoa',
                'Girona': 'Gerona',
                'Lleida': 'Lérida',
                'Ourense': 'Orense',
                'Palmas, Las': 'Las Palmas',
                'Rioja, La': 'La Rioja',
                'Valencia/València': 'Valencia',
               }

AGE_GROUP_MAP = {'0-4 años': '0-9',
                 '5-9 años': '0-9',
                 '10-14 años': '10-19',
                 '15-19 años': '10-19',
                 '20-24 años': '20-29',
                 '25-29 años': '20-29',
                 '30-34 años': '30-39',
                 '35-39 años': '30-39',
                 '40-44 años': '40-49',
                 '45-49 años': '40-49',
                 '50-54 años': '50-59',
                 '55-59 años': '50-59',
                 '60-64 años': '60-69',
                 '65-69 años': '60-69',
                 '70-74 años': '70-79',
                 '75-79 años': '70-79',
                 '80-84 años': '80+',
                 '85-89 años': '80+',
                 '90-94 años': '80+',
                 '95-99 años': '80+',
                 '100 años y más': '80+',
}


def get_demographic_data_by_province(age_ranges=None, sex=None):
    dframe = pandas.read_csv(config.DEMOGRAPHIC_CSV, delimiter='\t')

    provinces = [spain_data.PROVINCE_ISO_PER_NAME[PROVINCE_MAP.get(prov_iso, prov_iso)] for prov_iso in dframe['Provincias']]
    ages = [AGE_GROUP_MAP[age] for age in dframe['Edad (grupos quinquenales)']]
    sex_ = [sex[0] for sex in dframe['Sexo']]
    data = {config.ORIG_AGE_GROUP_COL: ages,
            config.ORIG_PROVINCE_COL: provinces,
            config.ORIG_SEX_COL: sex_,
            NUM_PEOPLE_COL: dframe['Total']}
    dframe = pandas.DataFrame(data)

    masks = []
    if sex is not None:
        this_mask = dframe[config.ORIG_SEX_COL] == sex
        masks.append(this_mask)

    if age_ranges is None:
        age_ranges = []
    age_masks = []
    for age_range in age_ranges:
        this_mask = dframe[config.ORIG_AGE_GROUP_COL] == age_range
        age_masks.append(this_mask)
    this_mask = None
    if age_masks:
        for age_mask in age_masks:
            if this_mask is None:
                this_mask = age_mask
            else:
                this_mask = numpy.logical_or(age_mask, this_mask)
    if this_mask is not None:
        masks.append(this_mask)

    mask = None
    for one_mask in masks:
        if mask is None:
            mask = one_mask
        else:
            mask = numpy.logical_and(mask, one_mask)

    if mask is not None:
        dframe = dframe.loc[mask, :]

    return dframe.groupby(by=config.ORIG_PROVINCE_COL).sum()[NUM_PEOPLE_COL]


def get_demographic_data_by_community(age_ranges=None, sex=None):

    by_province = get_demographic_data_by_province(age_ranges=age_ranges, sex=sex)

    ccaa = [spain_data.CA_PER_PROVINCE[prov_iso] for prov_iso in by_province.index]
    return by_province.groupby(by=ccaa).sum()


def get_demographic_data_for_spain(age_ranges=None, sex=None):
    by_province = get_demographic_data_by_province(age_ranges=age_ranges, sex=sex)
    return by_province.sum()


if __name__ == '__main__':
    res = get_demographic_data_by_community(sex=None, age_ranges=None)
    print(res)