# Classifying the Difficulty Levels of Working Memory Tasks by using Pupillary Response :page_facing_up:
Authors: [Hugo Mitre-Hernandez](http://scholar.google.com/citations?user=TjQqDSIAAAAJ&hl=en), [Jorge Sanchez-Rodriguez](https://scholar.google.com/citations?user=1hWlnBoAAAAJ&hl=en), [Sergio Nava-Muñoz](https://scholar.google.com/citations?user=Fc9sxKgAAAAJ&hl=en&authuser=1&oi=ao), [Carlos Lara-Alvarez](https://scholar.google.com.mx/citations?user=LwK9CQ8AAAAJ&hl=es)

Institution: [Center for Research in Mathematics (CIMAT)](http://www.cimat.mx/en), Zacatecas, Zacatecas, Mexico.

E-mails: hmitre@cimat.mx, jorge.rodriguez@cimat.mx, nava@cimat.mx, carlos.lara@cimat.mx 

## Content :heavy_check_mark: 
This repository contains the code and its instructions in the article "Classifying the Difficulty Levels of Working Memory Tasks by using Pupillary Response". You will find:
- The variables description and its **Python code** to calculate the cognitive load measurement of memorization tasks. 
- The data analysis of the variables using **R language** with the aim to find significant differences of three difficulty levels. The data was extracted from an eye-tracking study (Klingner et al. 2011).
- The classifiers training description and its **Python code** to classify difficulty levels, and the results of precision, recall and F1-score.

## Resume :memo:
Knowing the difficulty of a given task is crucial for improving the learning outcomes. This paper studiesthe difficulty level classification of memorization tasks from pupillary response data. Developing a difficulty level classifier from pupil size features is challenging because of the inter-subject variability of pupil responses. Eye-tracking data used in this study was collected while students solved different memorization tasks divided as low-, medium-, and high-level.  Statistical analysis shows that values of pupillometric features (as peak dilation, pupil diameter change, and suchlike) differ significantly for different difficulty levels. We used a wrapper method to select the pupillometric features that work the best for the most common classifiers; Support Vector Machine (SVM), Decision Tree (DT), Linear DiscriminantAnalysis (LDA), and Random Forest (RF). Despite the statistical difference, experiments showed that a random forest classifier trained with five features obtained the best F1-score (82%).  This result is essential because it describes a method to evaluate the cognitive load of a subject performing a task using only pupil size features.

## Cite this work :link:
In case you are using this code, please cite this work as follows:

Hugo Mitre-Hernandez, Jorge Sanchez-Rodriguez, Sergio Nava-Muñoz, Carlos Lara-Alvarez (2021). Classifying the Difficulty Levels of Working Memory Tasks by using Pupillary Response. Preprint: PeerJ.

## Dataset :floppy_disk:
The dataset of the pupillary response can be found at:
Klingner, J., Tversky, B., & Hanrahan, P. (2011). [Effects of visual and verbal presentation on cognitive load in vigilance, memory, and arithmetic tasks](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-8986.2010.01069.x). Psychophysiology, 48(3), 323-332.
