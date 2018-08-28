# SJRWI data scraper

## Motivation

St. Joseph River Watershed Initiative (http://www.sjrwi.org/) has a goal of promoting environmentally and economically sustainable land use and practices. To achieve this, they have been supportive of water quality monitoring programs within the watershed. The data collected have been made available to the public free of charge through a web interface (http://wqis.ipfw.edu/).

The user has to select a station of interest, select the class of water quality (Nutrients, Pesticides, etc.), the parameter of interest and the date range. The data for the selected station are displayed in form of HTML tables, and are paginated when we have more than 25 records at a station.

While the data is valuable for the research community, the web interface does not presently allow users to download the entire dataset. Users have to manually copy paste rows of data to Excel or Text files, page by page, station by station, and for each water quality class separately. This is time consuming and can be error prone. 

To simplify this task, this repository provides a python script that automatically scrapes the data from the web, and saves it as a 'comma' separated value files. As a result, all stakeholders can now focus on more important tasks such modeling, data analysis, inference, data visualization, decision making, etc.

The repository comes with a Readme.txt file that describes the data structure and dependencies. For data collection methods and quality issues please visit SJRWI website (http://www.sjrwi.org/). The repository is released with an MIT license, but we request anyone who uses this repository to cite the work as below. This helps to get the word out, so that many people find it useful. Thank you for your support.

===
## Cite this repository as follows:

Ganeshchandra Mallya, 2018. SJRWI data scraper, GitHub repository, https://github.com/gcmallya85/SJRWI-data-scraping.
```
@misc{Mallya2018,
  author = {Ganeshchandra, Mallya},
  title = {SJRWI data scraper},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/gcmallya85/SJRWI-data-scraping}},
  commit = {e06009bf6679825657a3a423d6cb553b747bb6b1}
} 
```