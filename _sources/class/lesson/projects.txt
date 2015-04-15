Final Project Guidelines
===============================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:

Important Dates
-------------------------------------------------------------------------------

* Project Proposal: May 1st
* (Tentative) Oral Presentation: May 20, 21th during discussion sessions (each
  group has 5 minutes) 
* Final report: May 31th

Submission
-------------------------------------------------------------------------------

* IU Canvas: https://canvas.iu.edu

Team Coordination
-------------------------------------------------------------------------------

Up to 3 members is recommended.

List of Possible Projects
-------------------------------------------------------------------------------

We have a few suggestions on possible projects from NIST, ICT, IU and others.
See the following lists.

.. list-table:: Possible Projects From NIST* (http://bigdatawg.nist.gov/_uploadfiles/M0399_v1_6344899314.doc)
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`Fingerprint Matching <ref-class-project-fingerprint-matching>`
     - Algorithm
     - NIST Special Database 14, 29, 30
     - - Apache Hadoop
       - Spark
       - HBase 
   * - :ref:`Human and Face Detection from Video (simulated streaming data) <ref-class-project-human-and-face-detection>`
     - Algorithm
     - OpenCV, INRIA Person Dataset
     - - Apache Hadoop
       - Spark
       - OpenCV
       - Mahout
       - MLlib
   * - :ref:`Live Twitter Analysis <ref-class-project-live-twitter>`
     - Visualization
     - Live Twitter feed
     - - Apache Strom
       - HBase
       - Twitter's Search and Streaming APIs, 
       - D3.js
       - Tableau
   * - :ref:`Big data Analytics for Healthcare Data/Health informatics <ref-class-project-healthcare>`
     - Analytics
     - Medicare Part-B in 2014
     - - Apache Hadoop
       - Spark
       - HBase
       - Mahout
       - Lucene/Solr
       - MLlib
   * - :ref:`Spatial Big data/Spatial Statistics/Geographic Information Systems <ref-class-project-spatial-bigdata>`
     - Analysis
     - Uber Ride Sharing GPS Data 
     - - Apache Hadoop 
       - Spark
       - GIS-tools
       - Mahout
       - MLlib 
   * - :ref:`Data Warehousing and Data mining <ref-class-project-data-warehousing>`
     - Data mining
     - 2010 Census Data Products: United States
     - - Apache Hadoop
       - Spark
       - HBase
       - MongoDB
       - Hive
       - Pig
       - Mahout
       - Lucene/Solr
       - MLlib

* \*Reference URL of these projects: http://bigdatawg.nist.gov/_uploadfiles/M0399_v1_6344899314.doc

.. list-table:: Possible Projects from BigDataBench, ICT, Chinese Academy of Sciences**
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - `Amazon Movie Reviews <http://snap.stanford.edu/data/web-Movies.html>`_
     - Analytics (Bayes)
     - `8 million reviews <http://snap.stanford.edu/data/movies.txt.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Google web graph <http://snap.stanford.edu/data/web-Google.html>`_
     - Analytics (PageRank)
     - `Webgraph from Google, 2002 <http://snap.stanford.edu/data/web-Google.txt.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Facebook Social Network <http://snap.stanford.edu/data/egonets-Facebook.html>`_
     - Analytics (Kmeans)
     - `Facebook data <http://snap.stanford.edu/data/facebook.tar.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Genome sequence data <http://ccl.cse.nd.edu/software/sand/>`_
     - Analytics
     - ``.cfa`` sample data
     - Work Queue

You can find more examples in the following link.
* \**Reference URL of these projects: http://prof.ict.ac.cn/BigDataBench/#Benchmarks

.. list-table:: Possible Projects From IU
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`Author Name Disambiguation for Bibliometric Data <project_namedisambugiuty>`
     -
     - https://github.com/scienceimpact/bibliometric
     - - graphdb
       - neo4j
       - Apache Giraph
       - mongodb
       - d3.js
       - sql
       - REST
   * - :ref:`A Paper on Container Technologies for BigData <project_namedisambugiuty2>`
     -
     - 
     - - Docker
       - CoreOS
       - Kubernetes
       - Redhat Atomic
       - Marathon
       - Mesos
   * - :ref:`A Survey of DevOps Frameworks in support of Big Data <project_namedisambugiuty3>`
     -
     -
     - - Any DevOps framework
       - Any PaaS using DevOps
       - Supporting services such as code reporsitories
   * - :ref:`A Survey of Online PaaS Frameworks and Clouds in support of Big Data <project_namedisambugiuty4>`
     -
     -
     - - Any online PaaS framework
       - Any PaaS used for Big Data
       - Heroku
       - CloudLab
       - ChameleonCloud
       - AWS
       - Azure
       - HP Helion
   * - Analysis on Census Data
     -
     - http://www.census.gov/population/www/cen2010/glance/ 
     - - HBase
       - Hadoop
       - Mahout
       - Spark/MLlib
       - D3

.. list-table:: Possible Projects From Ohters
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`Predicting Airline Delays with Hadoop <ref-class-project-airline-delays>`
     - Machine Learning
     - Airline delay dataset 2007, 2008
     - - Hadoop
       - Apache Pig
       - Python
       - Pandas
       - HDFS
       - scikit-learn
   * - :ref:`Daily Variation of Barometric Pressure <ref-class-project-barometric-pressure>`
     - Data Processing
     - Quality Controlled Local Climatological Data
     - - IPython Notebook 2.0 
       - Pandas
       - Numpy
       - matplotlib
       - d3.js
   * - :ref:`Data Visualization <ref-class-project-visualization>`
     - Visualization
     - Project dataset from DonorsChoose.org
     - - D3.js
       - DC.js
       - Python
       - MongoDB
   * - :ref:`MapReduce Implementation for Longest Common Substring Problem <ref-class-project-lcs>`
     - Parallel Programming
     - Escherichia coli K-12
     - - Python
       - Amazon
   * - :ref:`MapReduce Implementation for GFF Parsing <ref-class-project-gff>`
     - Parallel Programming
     - 
     - - Python
       - Disco
       - Amazon EC2

* :ref:`List of Datasets <ref-class-lesson-list-dataset>`
* :ref:`List of Technologies <ref-class-lesson-list-tech>`

Project Expectation
-------------------------------------------------------------------------------

We expect you to deal with one of the challenges from big data using open
source software. The main topics of your projects may cover one of these:

* parallel data processing on the cloud
* database on the cloud
* machine learning: optimization, modeling
* data mining
* visualization

*Other technology landscape can be addressed*

Project Proposal
-------------------------------------------------------------------------------

Please submit your project proposal to IU Canvas. The submission format is in a
file (either txt, Adobe PDF, or MS word). A project proposal is typically 1-2
pages long and should contain in the
description section:

* the nature of the project and its context
* the technologies used
* any proprietary issues
* specific aims you intent to complete
* and a list of intended deliverables (see also atrifacts)

Sample Project Proposal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

        Title: This is my title

        Team: (YOU CAN HAVE UP TO 3 PEOPLE IN A TEAM, IF YOU WANT MORE, PLEASE
        BE SURE TO CONTACT US)

                Fullname        e-mail  github username portalname

        Description:

                Put here your description

        Artifacts:

                Put here a list of artifacts that you will create (this can be
                filled out at a later time

                Examples are: A Survey Paper, a github repository link (with
                everything being there, including this description),
                screenshots, ...  

Oral Presentation (TBD)
-------------------------------------------------------------------------------

* A student will use Adobe Connect to give a presentation.

* 5 minutes per team.

* Oral presentation can be replaced with a 1-2 page progress report(s) upon
  approval.

Final Report
-------------------------------------------------------------------------------

* Source code on Github: https://github.com/futuresystems
* Written report: 4-6 pages
   - Test instruction (if necessary)
   - List of data source
   - List of technologies used

Questions & Support
-------------------------------------------------------------------------------

* Course TA's email: coursehelp@futuresystems.org
* Office Hours: Wednesday 7pm or Thursday 10am via `Adobe Connect <https://connect.iu.edu/bdossp_sp15/>`_

