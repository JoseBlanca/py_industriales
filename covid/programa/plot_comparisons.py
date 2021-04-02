
import config

from datetime import timedelta

import numpy

import covid_data
import plot
import spain_data


def plot_region_comparison(plot_path, dframes_per_param, title, region_type):

    fig = plot.SharedXFigure(num_axes=len(config.ORIG_COUNT_COLS),
                             fig_size=config.FOR_PANEL_EVOLUTION_FIG_SIZE)

    x_poss = None
    for idx, param in enumerate(config.ORIG_COUNT_COLS):
        region_values = dframes_per_param[param].sum(axis=0)

        if x_poss is None:
            x_poss = numpy.arange(region_values.size)
        
        axes = fig.get_axes(idx)
        axes.bar(x_poss, region_values)

        ylabel = config.PLOT_PARAM_DESCRIPTIONS[param]
        ylabel = f'{ylabel} (por 1e5 hab.)'
        plot.set_y_label(axes, ylabel)

    if region_type == config.COMMUNITY:
        names_for_regions = spain_data.CA_NAMES_PER_ISO_CODE
    else:
        names_for_regions = spain_data.PROVINCE_NAMES_PER_ISO_CODE

    labels = [names_for_regions[region_iso] for region_iso in region_values.index]
    plot.set_x_ticks(fig.get_axes(len(config.ORIG_COUNT_COLS) - 1), x_poss, labels)

    fig.get_axes(0).set_title(title)

    fig.save_fig(plot_path)


def plot_deaths_vs_hosp(plot_path, dframes_per_param, title, region_type):

    fig = plot.SimpleFigure()
    num_hosp = dframes_per_param[config.ORIG_HOSP_COL].sum(axis=0)
    num_dead = dframes_per_param[config.ORIG_DEATHS_COL].sum(axis=0)
    values = num_dead / num_hosp

    axes = fig.axes

    if region_type == config.COMMUNITY:
        names_for_regions = spain_data.CA_NAMES_PER_ISO_CODE
    else:
        names_for_regions = spain_data.PROVINCE_NAMES_PER_ISO_CODE
    labels = [names_for_regions[region_iso] for region_iso in num_hosp.index]

    x_poss = numpy.arange(values.size)

    axes.bar(x_poss, values)
    plot.set_x_ticks(axes, x_poss, labels)
    axes.set_title(title)
    plot.set_y_label(axes,
                     config.PLOT_PARAM_DESCRIPTIONS[config.ORIG_DEATHS_COL] + ' / ' + config.PLOT_PARAM_DESCRIPTIONS[config.ORIG_HOSP_COL])

    fig.save_fig(plot_path)


if __name__ == '__main__':

    last_date = covid_data.get_last_date_in_dframe()
    last_date = last_date - timedelta(days=7)
    two_weeks = timedelta(days=14)
    date_range = (last_date - two_weeks, last_date)

    out_dir = config.PLOT_DIR

    children = ['0-9']
    youngs = ['10-19', '20-29']
    middle_age = ['30-39', '40-49', '50-59']
    old = ['60-69', '70-79']
    very_old = ['80+']
    age_groups = [children, youngs, middle_age, old, very_old]

    for date_range, date_range_name in ((date_range, 'recent'),
                                        (None, 'all')):
        by = config.COMMUNITY
        for age_ranges, age_range_name in [(children, 'ninyos'),
                           (youngs, 'jovenes'),
                           (middle_age, 'mediana_edad'),
                           (old, 'mayores'),
                           (very_old, 'ancianos'),
                           (None, '')]:
            plot_path = out_dir / f'community_comparison_{age_range_name}_{date_range_name}.svg'
            plot_path2 = out_dir / f'hosp_vs_death_{age_range_name}_{date_range_name}.svg'
            dframes_per_param = covid_data.get_evolutions_per_param(by=by,
                                                                    date_range=date_range,
                                                                    rate_by_100k=True,
                                                                    age_ranges=age_ranges)
            if date_range is None:
                title = 'Parámetros desde el inicio de la pandemia'
            else:
                num_weeks = int((date_range[1] - date_range[0]) / timedelta(weeks=1))
                first_date = date_range[0]
                last_date = date_range[1]
                title = f'Parámetros en {num_weeks} semanas ({first_date.day}/{first_date.month}-{last_date.day}/{last_date.month})'

            if age_range_name:
                title += f' ({age_range_name})'

            plot_region_comparison(plot_path, dframes_per_param, title, region_type=by)
            plot_deaths_vs_hosp(plot_path2, dframes_per_param, title, region_type=by)