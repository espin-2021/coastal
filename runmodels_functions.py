#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output


# In[2]:


def plot_coast(domain):
    fig,ax = plt.subplots(figsize=(12,5))
    im = ax.imshow(domain, origin='lower', cmap='viridis_r')
    cb = fig.colorbar(im,ax=ax)
    cb.ax.set_ylabel('Water Depth (m)',fontsize=20,rotation=-90, labelpad=30)
    cb.ax.tick_params('y',labelsize=15)
    ax.set_xlabel('Along shore (km)',fontsize=20)
    ax.set_ylabel('Cross shore (km)',fontsize=20)
    ax.tick_params('both',labelsize=15)


def run_model_loop(Number_Iterations, domain ,cem ,waves, animate=True,update_ani=1000):
    alpha = 'sea_surface_water_wave__azimuth_angle_of_opposite_of_phase_velocity'
    Z = 'sea_water__depth'
    for time in range(Number_Iterations):
        waves.update()
        angle = waves.get_value(alpha)
        cem.set_value(alpha, angle)
        cem.update()
        if animate:
            if time%update_ani == 0:
                clear_output(wait=True)
                cem.get_value(Z, out=domain)
                plot_coast(domain)
                plt.title('Time Step: '+ str(time),fontsize=20)
                plt.show()

        else:
            clear_output(wait=True)
            print('Time Step: ',time, ' days')


def initialize_models(params,domain,cem,waves):
    '''
    Inputs:
    ------
    
    params = parameter dictionary
    
    domain = initial elevation domain
        ---> domain values in (-inifinity,1] 
                -->> 1 = land, <1 = water
            
    '''
    p = params
    
    N,M = domain.shape
    
    args = cem.setup( number_of_rows = N , number_of_cols = M, 
                      grid_spacing = p['grid_spacing'] ,  shelf_slope = p['shelf_slope'] , 
                      shoreface_depth = p['shoreface_depth'] , shoreface_slope = p['shoreface_slope'] 
                    )
    
    waves.initialize(*waves.setup())
    cem.initialize(*args)

    waves.set_value('sea_surface_water_wave__height', p['sea_surface_water_wave__height']);
    waves.set_value('sea_surface_water_wave__period',p['sea_surface_water_wave__period']);
    waves.set_value('sea_shoreline_wave~incoming~deepwater__ashton_et_al_approach_angle_highness_parameter',
                   p['sea_shoreline_wave~incoming~deepwater__ashton_et_al_approach_angle_highness_parameter']);
    waves.set_value('sea_shoreline_wave~incoming~deepwater__ashton_et_al_approach_angle_asymmetry_parameter',
                   p['sea_shoreline_wave~incoming~deepwater__ashton_et_al_approach_angle_asymmetry_parameter']);

    cem.set_value('land_surface__elevation',domain.flatten());


# In[ ]:




