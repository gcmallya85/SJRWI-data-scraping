This file describes the water quality data extracted from http://wqis.ipfw.edu/chartSelection/
Author - Ganesh Mallya
Created on - 08/26/2018
Modified by -
Modified on - 08/27/2018
Python script file - scrap_wq_data_SJRWI.py
1) stations.csv
This file contains station numbers, and corresponding name of the stations
Geographic coordinates of the station not available directly. Use other web services (such as google maps) to get the latitude and longitude information. Geographic markers available at http://wqis.ipfw.edu/chartSelection/. 

2) Folders are named using station numbers found in stations.csv. You will notice that some stations do not have a folder associated with it, this is because data were not available for such stations. Within each folder there are 4 files:
	a) bacteria.csv
		i) Columns are - SampleNumber; E. Coli (CFU/100 ml)
		ii) Data are separated by ";"
		iii) Missing values denoted as -999
		iv) StationNumber and Date can be extracted from a SampleNumber. For example a SampleNumber of 401092617 corresponds to sample collected at StationNumber 401 on September, 26, 2017.
	b) nutrients.csv
		i) Columns are - SampleNumber; Nitrate/Nitrite (mg/L); Total Phosphorus (mg/L); Dissolved Reactive Phosphorus (mg/L)
		ii) Data are separated by ";"
	c) pesticides.csv
		i) Columns are - SampleNumber; Alachlor (ug/L); Atrazine (ug/L); Metolachlor (ug/L)
		ii) Data are separated by ";"
	d) physical_properties.csv
		i) Columns are - SampleNumber; Conductivity (mS/cm); Dissolved Oxygen (mg/L); pH; Water Temperature (degree C); Total Dissolved Solids (g/L); Turbidity (NTU)
		ii) Data are separated by ";"
	
3) Units
	a) mg/L - milligram/liter
	b) ug - microgram/liter
	c) CFU - colony forming unit
	d) mS/cm - millisiemens/centimeter
	e) degree C - degree Celsius
	f) g/L - gram/liter
	g) NTU - Nephelometric turbidity unit