
import config

import numpy

import covid_data
import plot

def _age_group_first_num(age_group):
    first =age_group.split('-')[0].strip('+')
    if first == 'NC':
        age = 1000
    else:
        age = int(first)
    return age


def plot_params_per_age_group(sex=None, date_range=None):
    dframe = covid_data.get_frame(sex=sex, date_range=date_range)
    values_per_age_group = dframe.groupby(by=config.ORIG_AGE_GROUP_COL).sum()

    fig = plot.SharedXFigure(num_axes=values_per_age_group.shape[1])

    age_groups = None
    for idx, param in enumerate(config.ORIG_COUNT_COLS):
        values = values_per_age_group[param]

        if age_groups is None:
            age_groups = sorted(values.index, key=_age_group_first_num)
            xposs = numpy.arange(len(age_groups))

        values = values.loc[age_groups]

        axes = fig.get_axes(idx)
        axes.bar(xposs, values)
        plot.set_y_label(axes, config.PLOT_PARAM_DESCRIPTIONS[param])
        plot.set_x_ticks(axes, xposs, age_groups)

    plot_path = config.AGE_GROUP_PLOT_DIR / 'params_per_age_group.svg'
    fig.save_fig(plot_path)


if __name__ == '__main__':
    plot_params_per_age_group()
