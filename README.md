Description
===========
The project is an open source collaborative coding challenge. The goal of the project is to explore immigration data trends on H1B for past fiscal years. The dataset is retrieved from the US Department of Labor and Certification (https://www.foreignlaborcert.doleta.gov/performancedata.cfm)


Details
===================
The dataset is read and parsed one line at a time. 
A cleaning step is  performed first. Lines with the specific keyword are extracted. In the case of this study, the keyword is set to "CERTIFIED".  Columns associated with the study  ( "STATE" and "OCCUPATION") are selected. Extra trailing characters are stripped, and format for state code is checked for consistency.
The clean dataset is then processed by computing the number of applications for the chosen attribute.
The data is sorted and the leading lines are selected.


Software
=======
Python 3 
