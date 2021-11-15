#!/usr/bin/env python3
import acsys.dpm
import time
import datetime
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import ticker

blue = '#004C97'
green = '#4C8C2B'
red = '#8A2A2B'
orange = '#CB6015'
black = '#000000'
grey = '#63666A'
gold = '#EAAA00'

def acsysLoggerGet(device, event, T1, T2):
    
    #T2 = int(1000.0*time.time())# now, local time in milliseconds since epoch
    #T1 = int(T2 - nhours*3600.0*1000.0)
    
    T1 = 1000*T1
    T2 = 1000*T2
    
    times = []
    readings = []
    responses = []
    
    try:
        async def callDPM(con):
            #async with acsys.dpm.DPMContext(con, dpm_node = 'DPM02') as dpm:
            async with acsys.dpm.DPMContext(con) as dpm:
                await dpm.add_entry(0, dpm_request)
                await dpm.start()
                async for ii in dpm:
                    responses.append(ii)
                    if ii.isReadingFor(0):
                        if ii.data == []:
                            break
    
        dpm_request = device+"@"+event+"<-LOGGER:%s:%s"%(T1, T2)   
        acsys.run_client(callDPM)

        for response in responses:
            for i in range(len(response.data)):
                times.append(response.micros[i]/(1.0E6))
                readings.append(response.data[i])
        if times == []:
            raise Exception
        elif readings == []:
            raise Exception
    except:
        # Set data to NaN, which won't plot
        times = np.linspace(T1/1000.0, T2/1000.0, 10)
        readings = [np.nan]*10
    return times, readings
	   
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
	
def timePlot_singleAxis(filename, device_dict_list, T1, T2, dims=None, alpha=1.0):
    bgcolor = '#F1F1F1'
    fig, host = plt.subplots(1,1)
    lines = []
    legend_names = []
    plt.grid()
    if dims:
        fig.set_size_inches(dims[0], dims[1])
    # Plot devices
    for i in range(len(device_dict_list)):
        xdata = device_dict_list[i]["t_data"]
        ydata = device_dict_list[i]["data"]
        host.plot(xdata, ydata, color=device_dict_list[i]["color"], marker='o', markersize=3.0, markeredgewidth=0.0, linestyle='None', alpha=alpha)
        host.set_facecolor(bgcolor)
        lines.append(Line2D([0], [0], linewidth=6, color=device_dict_list[i]["color"]))
        legend_names.append(device_dict_list[i]["desc"] + ' (%s)'%(device_dict_list[i]["devicename"]))
        host.set_xlim(xdata[0], xdata[-1])
	
        if "yMin" in device_dict_list[i]:
            if "yMax" in device_dict_list[i]:
                plt.ylim(device_dict_list[i]["yMin"], device_dict_list[i]["yMax"])

        xtick_vals = np.linspace(T1, T2, 13)
        labels = []
        for xtick_val in xtick_vals:
            labels.append(datetime.datetime.fromtimestamp(xtick_val).strftime('%m/%d %H:%M'))
        plt.gca().set_xticks(xtick_vals)
        plt.gca().set_xticklabels(labels, rotation=90, ha='left')
        plt.gca().set_ylabel(device_dict_list[i]["units"])
        #plt.gca().yaxis.label.set_color(device_dict_list[i]["color"])
        #plt.gca().tick_params(axis='y', colors=device_dict_list[i]["color"])                 
    
    host.set_xlim(right=T2)
    host.legend(lines, legend_names, loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=4, prop={'size':9})
    plt.tight_layout()
    plt.subplots_adjust(right=0.95)
    #plt.savefig(filename+'.png')
    plt.savefig('/adwww/external_beams/'+filename+'.png')

def timePlot(filename, device_dict_list, T1, T2, dims=None):
    bgcolor = '#F1F1F1'
    fig, host = plt.subplots(1,1)
    plt.grid()
    lines = []
    legend_names = []
    
    if dims:
        fig.set_size_inches(dims[0], dims[1])
    
    # Plot devices
    for i in range(len(device_dict_list)):
    
        xdata = device_dict_list[i]["t_data"]
        ydata = device_dict_list[i]["data"]
        #xdata, ydata = acsysLoggerGet(device_dict_list[i]["devicename"], device_dict_list[i]["event"], nhours)
        if i == 0: 
            p0, = host.plot(xdata, ydata, color=device_dict_list[i]["color"], marker='o', markersize=3.0, markeredgewidth=0.0, linestyle='None')
            host.set_facecolor(bgcolor)
            lines.append(Line2D([0], [0], linewidth=6, color=device_dict_list[i]["color"]))
            legend_names.append(device_dict_list[i]["desc"] + ' (%s)'%(device_dict_list[i]["devicename"]))
            host.set_xlim(xdata[0], xdata[-1])
        elif i == 1:
            par1 = host.twinx()
            plt.plot(xdata, ydata, color=device_dict_list[i]["color"], marker='s', markersize=3.0, markeredgewidth=0.0, linestyle='None')
            lines.append(Line2D([0], [0], linewidth=6, color=device_dict_list[i]["color"]))
            legend_names.append(device_dict_list[i]["desc"] + ' (%s)'%(device_dict_list[i]["devicename"]))
            par1.set_xlim(xdata[0], xdata[-1])
	
        if "yMin" in device_dict_list[i]:
            if "yMax" in device_dict_list[i]:
                plt.ylim(device_dict_list[i]["yMin"], device_dict_list[i]["yMax"])
        #plt.locator_params(axis='y', nbins=6)
        
        xtick_vals = np.linspace(T1, T2, 13)
        labels = []
        for xtick_val in xtick_vals:
            labels.append(datetime.datetime.fromtimestamp(xtick_val).strftime('%m/%d %H:%M'))
        plt.gca().set_xticks(xtick_vals)
        plt.gca().set_xticklabels(labels, rotation=90, ha='left')
	
        ymin, ymax = plt.gca().get_ylim()
        plt.gca().yaxis.set_ticks(np.linspace(ymin, ymax, 6))
        plt.gca().set_ylabel(device_dict_list[i]["units"])
        plt.gca().yaxis.label.set_color(device_dict_list[i]["color"])
        plt.gca().tick_params(axis='y', colors=device_dict_list[i]["color"])                 
    
    host.set_xlim(right=T2)
    host.legend(lines, legend_names, loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=4, prop={'size':14})
    plt.tight_layout()
    #plt.savefig(filename+'.png')
    plt.savefig('/adwww/external_beams/'+filename+'.png')
