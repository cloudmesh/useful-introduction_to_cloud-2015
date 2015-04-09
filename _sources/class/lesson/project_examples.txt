.. _ref-class-lesson-project-examples:

Sample Projects
===============================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:
I
Project I: Daily Variation of Barometric Pressure
-------------------------------------------------------------------------------

Project Idea
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This type of projects gives you some experience of data processing.
Rich Python modules i.e. Pandas, NumPy or Matplotlib allow us to import and
manipulate dataset to provide results in a graphical format.

Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Description: Daily variation of barometric pressure (maximum minus minimum
  for each day) in inches, for the past 12 months. For each of the hand-picked
  major cities, the 365 daily ranges for that city are histogrammed.
* Dataset: `Quality Controlled Local Climatological Data <http://cdo.ncdc.noaa.gov/qclcd/QCLCD?prior=N>`_
* Technologies: 
  - IPython Notebook 2.0 (Pandas, Numpy, matplotlib)
  - d3.js

.. figure:: ../../images/projects/GeoSparkGrams.png

   GeoSparkGrams of Daily Barometric Volatility*


* \*Source: 
  - http://nbviewer.ipython.org/urls/gist.githubusercontent.com/michaelmalak/dd5495a605a8b951da43/raw/472b180b46d50726326eda2a4704f7ee0e94f539/GeoSparkGram.ipynb
  - http://technicaltidbit.blogspot.com/2014/05/geosparkgrams-tiny-histograms-on-map.html

Project II: Data Visualization
-------------------------------------------------------------------------------

Project Idea
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The main goal of this type of projects is visulaizing datasets stored in a
database.  You may like to use relational databases (SQL based) but this
example uses document based (JSON like, BSON) structure to store information
and you gain some experience with document-oriented databases.

You have open data based on CSV files. The tasks include
creating a database and automating the loading of the latest open data CSV
extracts from Amazon Storage (S3) into a database. With D3.js and DC.js
visualization toolkits, you understand how to provide results in an interactive
mode.

Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Description: DonorsChoose.org is a US based nonprofit organization that
  allows individuals to donate money directly to public school classroom
  projects. Public school teachers post classroom project requests on the
  platform, and individuals have the option to donate money directly to fund
  these projects. The classroom projects range from pencils and books to
  computers and other expensive equipments for classrooms. In more than 10
  years of existence, this platform helped teachers in all US states to post
  more than 7700,000 classroom project requests and raise more than
  $280,000,000. DonorsChoose.org is making the platform data open and available
  for making discoveries and building applications. In this tutorial we will be
  using one of the available datasets for building an interactive data
  visualization that represents school donations broken down by different
  attributes.

* Dataset: `Project dataset from DonorsChoose.org <https://s3.amazonaws.com/open_data/csv/opendata_projects.zip>`_
* Technologies:
  - D3.js
  - DC.js
  - Python
  - MongoDB

.. figure:: ../../images/projects/viz_demo.gif

   Interactive Data Visualization for donorschoose.org**

* \**Source:
  - http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/

Project III: 
