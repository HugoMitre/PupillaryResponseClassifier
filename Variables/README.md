# Variables to calculate the cognitive load measurement of memorization tasks.

MasterVisual.py was developed in python 3.8.3. To execute this file is necessary to have the following libraries:

- Pandas> = 1.0.5
- Numpy> = 1.18.5
- Scipy> = 1.5.0 

When executed, the variables are calculated for each participant and each of the tests they performed. At the end, a CSV file is generated with all the calculated variables. 

*The CSV file is saved in the same folder where MasterVisual.py is saved.

The following variables were calculated from the pupillary data:

**Baseline Pupil Size (BLPS)**. The prestimulus phase lasts two seconds before the question,
The BLPS is used to set a value of the pupil stabilization. It is calculated in each trial, Klingner et al. (2011) used a baseline subtraction in each trial based on the average pupil diameter measured over 20 samples in 400 ms at the end of a pre-stimulus (pupil stabilization) period.

**Mean Pupil Diameter Change (MPDC)**. To estimate the _MPDC_, the baseline is substracted from the average of the  pupillary data, that is, 

<img width="211" alt="Captura de Pantalla 2021-11-11 a la(s) 10 41 54" src="https://user-images.githubusercontent.com/29002113/141335568-6a2babae-2bea-4b5d-98cc-73d41ecbf360.png">

where _PSi_ is the pupillary data collected at time _i_, and _BLPS_ is the baseline.

**Average Percentage Change in Pupil Size (APCPS)**. is calculated as the difference between the measured pupil size and the baseline pupil size, divided by the baseline pupil size.

<img width="170" alt="Captura de Pantalla 2021-11-11 a la(s) 10 45 21" src="https://user-images.githubusercontent.com/29002113/141336073-890b68fe-824a-42a0-b43a-e7c70caf724e.png">

where _PSi_ is the pupil size collected in the _i–th_ time, and _BLPS_ is the baseline of the pupil size. The _APCPS_ is the average in the measurement interval time.

<img width="159" alt="Captura de Pantalla 2021-11-11 a la(s) 10 46 39" src="https://user-images.githubusercontent.com/29002113/141336289-1daaf324-80f3-44b0-b21d-47946ee9dbeb.png">

where _n_ is the number of measurements in the interval.





