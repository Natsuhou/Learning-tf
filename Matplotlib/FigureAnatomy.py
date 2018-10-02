import matplotlib.pyplot as plt
import numpy as np

# The whole figure. The figure keeps track of all the child Axes, a smattering of 'special' artists
# (titles, figure legends, etc), and the canvas. (Don't worry too much about the canvas, it is crucial as it
# is the object that actually does the drawing to get you your plot,
# but as the user it is more-or-less invisible to you). A figure can have any number of Axes,
#  but to be useful should have at least one.

fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes