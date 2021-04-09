
from datetime import datetime, timedelta
import config

import covid_data
import plot
import spain_data
import utils_path


def plot_evolution_spain(plot_path, sex=None, date_range=None,
                         rate_by_100k=False, by_week=False):
    evolutions = covid_data.get_evolutions_for_spain(sex=sex,
                                                     date_range=date_range,
                                                     rate_by_100k=rate_by_100k,
                                                     by_week=by_week)
    _plot_evolution(plot_path=plot_path,
                    evolutions=evolutions,
                    by_week=by_week,
                    rate_by_100k=rate_by_100k,
                    date_range=date_range)


def _plot_evolution(plot_path, evolutions, by_week, rate_by_100k,
                    date_range,
                    main_evolution_label=None, reference_evolution_label=None,
                    reference_evolutions=None):
    fig = plot.SharedXFigure(num_axes=evolutions.shape[1],
                             fig_size=config.FOR_PANEL_EVOLUTION_FIG_SIZE)

    for idx, param in enumerate(config.ORIG_COUNT_COLS):
        axes = fig.get_axes(idx)
        evolution = evolutions[param]
        if date_range is not None:
            evolution = evolution.loc[date_range[0]: date_range[1]]

        axes.plot(evolution.index, evolution.values,
                  color=config.MAIN_EVOLUTION_COLOR,
                  label=main_evolution_label)

        if reference_evolutions is not None:
            reference_evolution = reference_evolutions[param].loc[date_range[0]: date_range[1]]
            axes.plot(reference_evolution.index,
                      reference_evolution.values,
                      color=config.REFERENCE_EVOLUTION_COLOR,
                      label=reference_evolution_label)
            axes.legend()

        ylabel = config.PLOT_PARAM_DESCRIPTIONS[param]
        if rate_by_100k:
            ylabel = f'{ylabel} (por 1e5 hab.)'
        if by_week:
            ylabel = f'{ylabel}\n(semanal)'
        plot.set_y_label(axes, ylabel)
        plot.set_x_ticks_format(axes, 45, ha='right')

    fig.save_fig(plot_path)


def _plot_evolution_per_region(out_dir, by, sex=None, date_range=None,
                               by_week=False,
                               plot_spain_reference=True):
    region_kind = by
    if by == config.PROVINCE:
        region_names_per_iso_code = spain_data.PROVINCE_NAMES_PER_ISO_CODE
    else:
        region_names_per_iso_code = spain_data.CA_NAMES_PER_ISO_CODE

    out_dir.mkdir(exist_ok=True)

    extended_date_range = date_range[0] - timedelta(days=30), date_range[1]
    if plot_spain_reference:
        spain_evolutions = covid_data.get_evolutions_for_spain(sex=sex,
                                                               date_range=extended_date_range,
                                                               rate_by_100k=True,
                                                               by_week=by_week)
    else:
        spain_evolutions = None

    region_evolutions = covid_data.get_evolutions_by_region(by=region_kind,
                                                            sex=sex,
                                                            date_range=extended_date_range,
                                                            rate_by_100k=True,
                                                            by_week=by_week)
    for region_iso, evolutions in region_evolutions.items():
        region_name = region_names_per_iso_code[region_iso]
        name_for_path = utils_path.get_nice_path(region_name)
        plot_path = out_dir / f'{name_for_path}_evolution.svg'
        _plot_evolution(evolutions=evolutions,
                        plot_path=plot_path,
                        by_week=by_week,
                        reference_evolutions=spain_evolutions,
                        main_evolution_label=region_name,
                        reference_evolution_label='España',
                        rate_by_100k=True,
                        date_range=date_range)



def plot_evolution_per_community(out_dir, sex=None, date_range=None,
                                 by_week=False,
                                 plot_spain_reference=True):

    _plot_evolution_per_region(out_dir=out_dir,
                               by=config.COMMUNITY,
                               sex=sex,
                               date_range=date_range,
                               by_week=by_week,
                               plot_spain_reference=plot_spain_reference)


def plot_evolution_per_province(out_dir, sex=None, date_range=None,
                                by_week=False,
                                plot_spain_reference=True):
    _plot_evolution_per_region(out_dir=out_dir,
                               by=config.PROVINCE,
                               sex=sex,
                               date_range=date_range,
                               by_week=by_week,
                               plot_spain_reference=plot_spain_reference)


if __name__ == '__main__':

    last_date = covid_data.get_last_date_in_dframe()
    one_week = timedelta(days=7)
    last_date = last_date - one_week
    one_moth = timedelta(days=30)
    date_range = (last_date - one_moth, last_date)

    for date_range, out_dir_name in ((date_range, 'recent'),
                                     (None, 'all')):

        out_dir = config.SPAIN_PLOT_DIR / out_dir_name
        out_dir.mkdir(exist_ok=True)
        plot_path = out_dir / 'spain_evolution.svg'
        plot_evolution_spain(plot_path, by_week=True, date_range=date_range)
        out_dir = config.COMMUNITY_PLOT_DIR / out_dir_name
        plot_evolution_per_community(by_week=True, out_dir=out_dir, date_range=date_range)
        out_dir = config.PROVINCE_PLOT_DIR / out_dir_name
        plot_evolution_per_province(by_week=True, out_dir=out_dir, date_range=date_range)
