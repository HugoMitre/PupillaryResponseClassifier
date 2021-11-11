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
Memorization is a key cognitive process in the learning content. A course with difficult memory tasks can provoke a cognitive overload and frustration in a group of learners, also with easy memory tasks can evoke low cognitive load and boredom, both cases with poor learning outcomes. But first, the cognitive load must be measured to be controlled in learning courses in a non-invasive way avoiding distractions --e.g. remote eye-trackers. In eye-tracking studies, there are no cognitive load or memory task difficulty classifiers. We propose a classifier of working memory task difficulty based on cognitive load characteristics with pupil size data using remote eye-tracker. For this, we made a data analysis of pupil data from three memorization tasks with easy, medium, high difficulty, selecting the features with significant differences and training the most accurate classifiers used in eye-tracking research as the Support Vector Machine (SVM), Decision Tree (DT), Linear Discriminant Analysis (LDA), Random Forest (RF).

## Cite this work :link:
In case you are using this code, please cite this work as follows:

Hugo Mitre-Hernandez, Jorge Sanchez-Rodriguez, Sergio Nava-Muñoz, Carlos Lara-Alvarez (2021). Classifying the Difficulty Levels of Working Memory Tasks by using Pupillary Response. Preprint: PeerJ.

## Dataset :floppy_disk:
The dataset of the pupillary response can be found at:
Klingner, J., Tversky, B., & Hanrahan, P. (2011). [Effects of visual and verbal presentation on cognitive load in vigilance, memory, and arithmetic tasks](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-8986.2010.01069.x). Psychophysiology, 48(3), 323-332.
