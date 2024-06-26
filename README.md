# desi-mirror-temp
An experiment to see if machine learning models can be used to improve upon human predictions for temperatures inside the DESI dome.

![all histograms](images/ind_hist.png)

A random forest regression and a MLP neural network were trained on DESI telemetry data in order to predict the dome temperature for the following observing day. Compared to human predictions, the neural network resulted in a 52% increase in predictions that fell within the desired range of $1^{\circ}C$ below and $1.5^{\circ}C$ above the actual temperature. Similarly, the random forest resulted in a 47% increase in predictions within this range.

This repository is organized as follows:
1. 

A paper with more details on the project can be found at: (**INSERT DESI WIKI LINK HERE**).
