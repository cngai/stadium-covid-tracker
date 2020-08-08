import chartify
import pandas as pd

# TEST PLAYGROUND TO GET FAMILIAR WITH CHARTIFY LIBRARY

def print_public_methods(obj):
    print('Methods:')
    print('\n'.join([x for x in dir(obj) if not x.startswith('_')]))

ch = chartify.Chart() # chart object

# Adding chart labels
ch.set_title('Test Title')
ch.set_subtitle('This is my subtitle.')
ch.set_source_label('testsource.com')
ch.axes.set_xaxis_label('Time')
ch.axes.set_yaxis_label('# of Infected Fans')

ch.show() # renders the chart

