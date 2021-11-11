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

**Peak Dilation (PD)**. The Peak Pupil Dilation (PPD) is defined as,

<img width="212" alt="Captura de Pantalla 2021-11-11 a la(s) 10 49 41" src="https://user-images.githubusercontent.com/29002113/141336748-e5818576-7a03-42b4-9cf7-f6ff7ba52a10.png">

To reduce the error caused by different sizes of the human eye, we modified the equation proposed in Marandi et al. (2018) by including the _BLPS_.

<img width="143" alt="Captura de Pantalla 2021-11-11 a la(s) 10 50 43" src="https://user-images.githubusercontent.com/29002113/141336897-090f53b8-16ce-4547-9f1e-22b018f19509.png">

**Entropy of Pupil (Epupil)**. Supose that the pupil dilation is a random variable _S_ with possible values _S1,S2,...,Sm_ such that _S1 = min{PS1,PS2,...,PSn}_, _Sm = PPD_. Consider that _Pi = f(i)_, where _f(i)_ is the relative frequency associated with the _i-th_ value _Si_ (i.e., how often the value si happens divided by the number of observations _n_). The information entropy is defined as

<img width="150" alt="Captura de Pantalla 2021-11-11 a la(s) 11 11 43" src="https://user-images.githubusercontent.com/29002113/141340021-09a57270-8f4b-4984-8103-b50472125bed.png">

Entropy can be described qualitatively as a measure of energy dispersal. The concept is linked to disorder: entropy is a measure of disorder, and nature tends toward maximum entropy for any isolated system.

**Time to Peak (TTP)**. Siegle et al. (2008) show that pupil dilation peaked between the completion of the memory encoding interval time and the start of memory storage. The dilation is proportional to the difficulty of the memory task, as higher the difficulty, higher the peak is. Then, the time to peak may reveal the difficulty level. It is defined as,

<img width="131" alt="Captura de Pantalla 2021-11-11 a la(s) 11 13 04" src="https://user-images.githubusercontent.com/29002113/141340191-6aac55ef-7b67-44c0-8ed3-fffa081ce9aa.png">

**Peak Dilation Speed (PDS)**. The method of least squares can find a relation between time and peak dilation (Siegle et al., 2008). Consider the _PS_ slope of the line that ends at the pupil dilation peak, estimated as

<img width="179" alt="Captura de Pantalla 2021-11-11 a la(s) 11 15 11" src="https://user-images.githubusercontent.com/29002113/141340496-74b61877-93ec-4853-88b9-18311c602dc6.png">

where _0 ≤ i ≤ n_, and _ti_ and _PSi_ are the time and size of the _i-th_ measurement, respectively. Finally, the slope is used to calculate the angle,

<img width="120" alt="Captura de Pantalla 2021-11-11 a la(s) 11 16 19" src="https://user-images.githubusercontent.com/29002113/141340657-9612bdbd-ede9-484b-b971-9322ef023526.png">




