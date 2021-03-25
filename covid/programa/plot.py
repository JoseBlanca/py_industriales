
import numpy

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


class _Figure:
    def __init__(self, fig_size=None):
        self._fig = Figure(figsize=fig_size)
        self._canvas = FigureCanvas(self._fig) # Don't remove it or savefig will fail later

    def save_fig(self, path):
        self._fig.savefig(path)


class SimpleFigure(_Figure):
    def __init__(self):
        super().__init__()
        self._axes = self._fig.add_subplot(111)    

    @property
    def axes(self):
        return self._axes


class SharedXFigure(_Figure):
    def __init__(self, num_axes, fig_size=None):
        super().__init__(fig_size=fig_size)
        self._axess = self._fig.subplots(nrows=num_axes, ncols=1, sharex=True)

    def get_axes(self, idx):
        return self._axess[idx]


def plot_hist(values, plot_path, n_bins=20, range_=None):
    fig = SimpleFigure()

    if range_ is None:
        range_ = numpy.nanmin(values), numpy.nanmax(values)

    bin_edges = numpy.linspace(range_[0], range_[1], num=n_bins)

    fig.axes.hist(values, bins=bin_edges)

    fig.save_fig(plot_path)


def set_y_label(axes, label):
    axes.set_ylabel(label)


def set_x_label(axes, label):
    axes.set_xlabel(label)


def set_x_ticks(axes, x_poss, labels, rotation=45, ha='right'):
    axes.set_xticklabels(labels, rotation=rotation, ha=ha)
    axes.set_xticks(x_poss)


def set_x_ticks_format(axes, rotation=45, ha='right'):
    for tick in axes.get_xticklabels():
        tick.set_rotation(rotation)
        tick.set_ha(ha)
