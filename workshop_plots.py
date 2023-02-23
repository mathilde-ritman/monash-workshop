import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np
import pandas as pd
import os

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix

from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
import cartopy.feature as cfeature

import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.gridspec as gridspec



def histogram_label_frequency(data, results_dir='', save=True):
    """ Frequency of observation of each class as a histogram. """
    
    font_s = 12

    fig, ax = plt.subplots()
    freq, bins, patches = ax.hist(data, bins=[0,1,2,3], align='left', rwidth=0.8, color='gray')
    # ax.set_ylim([0,225000])
    ax.set_xticks([0,1,2])
    ax.set_xticklabels(['No cloud', 'Cloud', 'Multi-layer cloud'], fontsize=font_s)
    ax.set_ylabel('Number of oberservations', fontsize=font_s)
    ax.set_yticklabels([])
    # label bars
    for patch, h in zip(patches, freq):
        ax.text(patch.get_x() + patch.get_width() / 2, h+0.01, '{:,}'.format(int(h)),
                ha='center', va='bottom')
    if save:
        fig.savefig(os.path.join(results_dir,'hist_target_freq.jpg'), dpi=300, bbox_inches = "tight")
    return

