from contextlib import contextmanager
from typing import Generator

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure


def set_mpl(tex: bool = True):
    sns.set()
    if tex:
        plt.rc("text", usetex=True)
        plt.rc("font", family="serif")

    plt.rc("font", size="12")
    plt.rcParams["figure.dpi"] = 200


@contextmanager
def genfig(
    size: tuple[int, int] = (5, 4), dpi: int = 100, n: tuple[int, int] = (1, 1)
) -> Generator[list[plt.Axes], None, Figure]:
    set_mpl()
    figsize = (size[0] * n[1], size[1] * n[0])
    fig, axs = plt.subplots(nrows=n[0], ncols=n[1], figsize=figsize, dpi=dpi)
    yield axs.flatten().tolist() if max(n) > 1 else [axs]  # type: ignore
    return fig


@contextmanager
def plotting():
    set_mpl()
    yield
    plt.show()


def title(ax: plt.Axes, name: str):
    ax.set_title(name, fontsize=14, loc="left", pad=9)


def label(ax: plt.Axes, x: str | None = None, y: str | None = None):
    if x is not None:
        ax.set_xlabel(x)
    if y is not None:
        ax.set_ylabel(y)
