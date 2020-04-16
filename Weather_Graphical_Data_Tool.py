# Weather Graphical Data Tool

import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

import METAR_Read2 as METAR

import tkinter as tk
import datetime
import numpy as np


answer = []


class Weather_Variables():
    def __init__(self, file):
        super().__init__()

        self.names = {
            "station": "Station",
            "valid": "Time",
            "tmpf": "Temperature [F]",
            "tmpc": "Temperature [C]",
            "dwpf": "Dewpoint [F]",
            "dwpc": "Dewpoint [C]",
            "relh": "Relative Humidity [%]",
            "drct": "Wind Direction",
            "sknt": "Wind Speed [Knots]",
            "p01i": "Precipitation [Inches]",
            "alti": "Pressure [Inches]",
            "mslp": "Pressure [Mb]",
            "vsby": "Visibility [Miles]",
            "gust": "Wind Gust [Knots]",
            "skyc1": "Sky Level 1 Coverage",
            "skyc2": "Sky Level 2 Coverage",
            "skyc3": "Sky Level 3 Coverage",
            "skyc4": "Sky Level 4 Coverage",
            "skyl1": "Sky Level 1 Altitude [Ft]",
            "skyl2": "Sky Level 2 Altitude [Ft]",
            "skyl3": "Sky Level 3 Altitude [Ft]",
            "skyl4": "Sky Level 4 Altitude [Ft]",
            "wxcodes": "Present Weather Codes",
            "feel": "Apparent Temperature [F]",
            "ice_accretion_1hr": "1 Hour Ice Accretion [Inches]",
            "ice_accretion_3hr": "3 Hour Ice Accretion [Inches]",
            "ice_accretion_6hr": "6 Hour Ice Accretion [Inches]",
            "peak_wind_gust": "Peak Wind Gust [Knots]",
            "peak_wind_drct": "Peak Wind Direction [deg]",
            "peak_wind_time": "Peak Wind Gust Time",
            "metar": "Raw Metar Data"
            }

        self.data = METAR.read_file(file)
        self.var_list = []
        self.dates = []
        # List of lists
        
        
    def stuff(self):
        
        print(self.var_list[4][:])
        print(self.var_list[5][:])
        print(self.var_list[6][:])
        
    def calculate_variables(self):
        self.tmpc = ['tmpc']
        self.dwpc = ['dwpc']
        for i in self.var_list[2][1:]:
            a = (float(i) - 32)*(5/9)
            self.tmpc.append(a)
        for i in self.var_list[3][1:]:
            b = (float(i) - 32)*(5/9)
            self.dwpc.append(b)
        for i in range(len(self.data[0])):
            self.data[i].insert(3, self.tmpc[i])
            self.data[i].insert(4, self.dwpc[i])
        self.var_list.insert(3, self.tmpc)
        self.var_list.insert(4, self.dwpc)


    def fill(self):
        n = len(self.data[0])
        varp = []
        num = 0
        j = 0
        i = 0
        # Creates lists for each specific variable in the sub-lists.
        while j < n:
            if i < len(self.data):
                if self.data[i][j] != 'M' and self.data[i][j] is not 'M/n':
                    if self.data[i][j] != 'T' and self.data[i][j] is not 'T/n':
                        varp.append(self.data[i][j])
                i+=1
            elif i == len(self.data):
                self.var_list.append(varp)
                j+=1
                i = 0
                varp = []
                
    
            
            
    def convert_time(self):
        t = []
        time = []
        for i in range(len(self.var_list[1])):
            t.append(self.var_list[1][i])
            if self.var_list[1][i][:10] != self.var_list[1][i-1][:10]:
                self.dates.append(self.var_list[1][i][:10])
                time.append(self.var_list[1][i][11:])
        
        
    def graph(self, b, opts):
        num = []
        numpy = []
        numpy1 = []
        numbers = []
        tic = []
        toc = []
        a = []
        self.b = b
        self.opts = opts
        # We need to pass in the choice for whatever we want to graph here.
        # for a in range(len(the list created from the checkbox choices))
        for i in range(len(self.b)):
            a.append(self.b[i])
            #print(a)
        for k in range(len(self.dates[1:])):
                numbers.append(k)
        
        for i in range(len(a)):
            c = self.data[0][:].index(a[i])
            num.append([])
            tic.append([])
            for j in range(len(self.var_list[c][1:])):
                num[i].append(j)
            for l in numbers:
                tic[i].append(l*(len(num[i])//len(numbers)))
            b = self.names[(self.var_list[c][0])]
            fig, ax = plt.subplots()
            ax.set_title(b)
            ax.ticklabel_format(useOffset=False)
            ax.plot(np.array(num[i][:]), np.array(self.var_list[c][1:]))
            plt.xticks(tic[i], self.dates[1:])
            plt.xticks(rotation = 45)
            #ax.set_xlim(left = 0, right = num[i][-1])
            ax.tick_params(length = 10, width = 2)
            ax.grid()
        
        if self.opts[0] == 1:
            c = self.data[0][:].index('tmpf')
            d = self.data[0][:].index('dwpf')
            for n in range(len(self.var_list[c][1:])):
                numpy.append(n)
            for l in numbers:
                toc.append(l*(len(numpy)//len(numbers)))
            fig, ax = plt.subplots()
            ax.set_title("Temperature and Dewpoint [F]")
            ax.plot(np.array(numpy[:]), np.array(self.var_list[c][1:]))
            ax.plot(np.array(numpy[:]), np.array(self.var_list[d][1:]))
            ax.set_xlim(left = 0, right = numpy[-1])
            ax.grid()
            plt.xticks(toc, self.dates[1:])
            plt.xticks(rotation = 45)
        if self.opts[1] == 1:
            o = self.data[0][:].index('tmpc')
            p = self.data[0][:].index('dwpc')
            for n in range(len(self.var_list[o][1:])):
                numpy1.append(n)
            for l in numbers:
                toc.append(l*(len(numpy)//len(numbers)))
            fig, ax = plt.subplots()
            ax.set_title("Temperature and Dewpoint [C]")
            ax.plot(np.array(numpy1[:]), np.array(self.var_list[o][1:]))
            ax.plot(np.array(numpy1[:]), np.array(self.var_list[p][1:]))
            ax.set_xlim(left = 0, right = numpy[-1])
            ax.grid()
            plt.xticks(toc, self.dates[1:])
            plt.xticks(rotation = 45)

        
        plt.show()
        
    def run(self, b, opts):
        self.fill()
        self.calculate_variables()
        #self.stuff()
        self.convert_time()
        self.graph(b, opts)





# Weather Analysis Tool User Interface

#################################################################################

# GUI

def close(root):
    root.destroy()
    import sys; sys.exit()

class Start():
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.answer = []
        
        # Prevents window size from being changed.
        self.root.resizable(width = False, height = False)
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        self.root.title("Weather Program")
        
        self.picture = tk.PhotoImage(file = "weatherpic.gif")


        self.top_label = tk.Label(self.frame, text = "Weather Program", font =
                             "Times 20 bold")
        self.top_label.grid(sticky = tk.N)

        tk.Label(self.frame, image = self.picture).grid()

        self.button_start = tk.Button(self.frame, text = 'Start', width = 10, command = self.start)
        self.button_start.grid(row = 2, padx = 30, sticky = tk.SW)
        self.button_quit = tk.Button(self.frame, text = 'Quit', width = 10, command = lambda: close(self.root))
        self.button_quit.grid(row = 2, padx = 30, sticky = tk.SE)
        self.root.mainloop()
        
        
    def start(self):
        self.root.destroy()
        question1()

        



    
class question1():
    def __init__(self):
        super().__init__()
        self.answer = []
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        
        self.a = tk.Label(self.frame, text = "Do you need to enter a link?")
        self.a.grid(row = 0)
        self.button_yes = tk.Button(self.frame, text = 'Yes', width = 10, command = self.yes)
        self.button_yes.grid(row = 1)
        self.button_no = tk.Button(self.frame, text = 'No', width = 10, command = self.no)
        self.button_no.grid(row = 2)
        
        self.root.mainloop()

    def yes(self):
        self.root.destroy()
        link1()
    def no(self):
        self.root.destroy()
        answer.append("weather_data.txt")
        main_screen()

        

    
class link1():
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.link = []
        self.answer = []
        self.a = tk.Label(self.root, text = "Please enter the link for analysis below.", font
             = "Arial 10 bold")
        self.a.grid(row = 0, column = 1, sticky = tk.N)
        self.b = tk.Label(self.root, text = "Link:")
        self.b.grid(row = 1, sticky = tk.W)
        self.s = tk.Entry(self.root, width = 40)
        self.s.grid(sticky = tk.W, row = 1, column = 1)
        self.button = tk.Button(self.root, text = 'Analyze', width = 10, command = self.aquire)
        self.button.grid(columnspan = 2, sticky = tk.W)
        self.root.mainloop()
        

        
    def aquire(self):
        self.link.append(self.s.get())
        lin = "https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station="
        if lin not in self.link[0]:
            tk.messagebox.showerror("Link Error", "Please enter a valid link.")
            del self.link[0]
        else:
            web = self.link[0]
            web2 = METAR.webpage(web)
            a = METAR.write_file(web2)
            answer.append(a)
            self.root.destroy()
            main_screen()




class Checkbar(tk.Frame):
        def __init__(self, parent = None, picks = [], side = tk.LEFT, anchor = tk.W):
            tk.Frame.__init__(self, parent)
            self.vars = []
            self.a = []
            i = 0
            for pick in picks:
                i += 1
                var = tk.IntVar()
                chk = tk.Checkbutton(self, text = pick, variable = var)
                chk.grid(row = i, rowspan = 1, sticky = tk.W)
                self.vars.append(var)
        def state(self):
            return map((lambda var: var.get()), self.vars)

class main_screen():
    def __init__(self):
        super().__init__()
        self.d = ['tmpf', 'tmpc', 'dwpf', 'dwpc', 'relh', 'drct', 'sknt', 'p01i', 'alti',
              'mslp', 'vsby', 'gust', 'ice_accretion_1hr', 'ice_accretion_3hr',
              'ice_accretion_6hr', 'peak_wind_gust', 'peak_wind_drct', 'peak_wind_time']
        self.d_names = ['Temperature [F]', 'Temperature [C]', 'Dewpoint [F]',
                        'Dewpoint [C]',
                   'Relative Humidity (%)', 'Wind Direction (Degrees)',
                   'Wind Speed [Knots]', 'Precipitation [Inches]', 'Pressure [Inches]',
                   'Pressure [Mb]', 'Visibility [Miles]', 'Wind Gust [Knots]',
                   '1 Hour Ice Accretion [Inches]', '3 Hour Ice Accretion [Inches]',
                   '6 Hour Ice Accretion [Inches]', 'Peak Wind Gust [Knots]',
                   'Peak Wind Direction [deg]', 'Peak Wind Gust Time']
        self.addit_options = ['Temperature and Dewpoint [F]',
                              'Temperature and Dewpoint [C]',
                              'Wind Speed and Gust [Knots]']
        self.root = tk.Tk()
        self.root.title("Weather Program")
        self.b = tk.Label(self.root, text = "Please select the following variables\n that you wish to graph:")
        self.b.grid(row = 1, column = 0, rowspan = 1, columnspan = 3 ,sticky = tk.NW)
        self.graphs = Checkbar(self.root, self.d_names)
        self.graphs.grid()
        tk.Button(self.root, text = 'Quit', width = 10, command = lambda: close(self.root)).grid(row = 3, rowspan = 1, sticky = tk.SE)
        c = tk.Button(self.root, text = 'Graph', width = 10, command = self.allstates).grid(row = 3, rowspan = 1, sticky = tk.SW)

        self.option_label = tk.Label(self.root, text = "Additional Options:")
        self.option_label.grid(row = 1, column = 13, padx = 50, rowspan = 1,  columnspan = 3, sticky = tk.NE)
        self.options = Checkbar(self.root, self.addit_options)
        self.options.grid(row = 2, column = 15, padx = 50, rowspan = 1,
                            columnspan = 3, sticky = tk.NE)

        self.root.mainloop()
    def allstates(self):
        self.e = []
        a = list(self.graphs.state())
        opts = list(self.options.state())
        for i in range(len(a)):
            if a[i] == 1:
                self.e.append(self.d[i])
        Weather_Variables(answer[0]).run(self.e, opts)
        



def main():
    # Define input variables
    Start()
main()
