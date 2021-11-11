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

**Mean Pupil Diameter Change (MPDC)**. To estimate the MPDC, the baseline is substracted from the average of the  pupillary data, that is, 

<img width="211" alt="Captura de Pantalla 2021-11-11 a la(s) 10 41 54" src="https://user-images.githubusercontent.com/29002113/141335568-6a2babae-2bea-4b5d-98cc-73d41ecbf360.png">

where PSi is the pupillary data collected at time i, and BLPS is the baseline.



