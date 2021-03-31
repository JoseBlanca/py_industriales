
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

if __name__ == '__main__':

    last_date = covid_data.get_last_date_in_dframe()
    last_date = last_date - timedelta(days=7)
    two_weeks = timedelta(days=14)
    date_range = (last_date - two_weeks, last_date)

    out_dir = config.PLOT_DIR

    for date_range, out_name in ((date_range, 'recent'),
                                 (None, 'all')):
        by = config.COMMUNITY
        plot_path = out_dir / f'community_comparison_{out_name}.svg'
        dframes_per_param = covid_data.get_evolutions_per_param(by=by,
                                                                date_range=date_range,
                                                                rate_by_100k=True)
        if date_range is None:
            title = 'Parámetros desde el inicio de la pandemia'
        else:
            num_weeks = int((date_range[1] - date_range[0]) / timedelta(weeks=1))
            first_date = date_range[0]
            last_date = date_range[1]
            title = f'Parámetros en {num_weeks} semanas ({first_date.day}/{first_date.month}-{last_date.day}/{last_date.month})'
        plot_region_comparison(plot_path, dframes_per_param, title, region_type=by)
