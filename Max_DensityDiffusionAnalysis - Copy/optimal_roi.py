import numpy as np
import math as m
from ipywidgets import interact, interactive, fixed, interact_manual, interactive_output, Layout
import ipywidgets as widgets


def critical_density(FR_max, R_coloc):
    '''
    Parameter:
        FR_max: maximum false positive rate
        R_coloc: colocalisation radius in µm
    Return:
        rho: critical density
    '''
    rho = (-1)*(np.log(1-FR_max))/((R_coloc**2)*m.pi)
    return rho


def opt_roi(rho, density, levels):
    '''
    Parameter:
        rho: critical density
        density: list of densities for each ROI
        levels: percentages for which ROI's are being constructed in the laserprofile
    Return:
        levels[position]: optimal percentage of the laserprofile to construct the ROI
    '''
    d = 10
    position = 0         #falls die gegebene Dichte zu groß ist, wird automatisch der größt mögliche ROI gewählt. Könnte auch ValueError raisen
    distance = [(i - rho) for i in density]
    
    for i in range(len(levels)):
        if 0 < distance[i] < d:
            d = distance[i]
            position = i +1
    return levels[position]   


def create_slider_dens(step, density):
    '''
    Creates slider for density.
    Prarameter:
        step: step size of slider
        density: data used for boundaries of slider
        
    Returns slider
    '''
    density_slider = widgets.FloatSlider(
        min=density.min(),
        max=density.max(),
        step=step,
        description='Critical den:',
        disabled= False,
        continuous_update=True,
        orientation='horizontal',
        readout=True,
        readout_format='.2f'
        )
    return density_slider






#def f(rho):
#    plt.figure(figsize=(15,10))
#    x = np.linspace(0.4, 1, num=1000)
#    plt.plot(levels, density, '-b', label = 'density')
#    plt.vlines(x=opt_roi(rho, density, levels), ymin=min(density), ymax=max(density), color='r', label='optimal ROI')
#    plt.hlines(y=rho, xmin=min(levels), xmax=max(levels), color='y', label='critical density')
#    plt.show()
#
#interactive_plot = interactive(f, rho=(min(density), max(density), 0.001))
#output = interactive_plot.children[1]
#output.layout.height = '1000px'
#interactive_plot

#interactive_plot.close()