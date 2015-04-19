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

.. empty line blocks

 |
 |
 |
 |
 |
 |
 |
 |
 |

List of Possible Projects
-------------------------------------------------------------------------------

We have a few suggestions on possible projects from NIST, ICT, IU and others.
See the following lists.

Possible Projects From NIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Possible Projects From NIST* (http://bigdatawg.nist.gov/_uploadfiles/M0399_v1_6344899314.doc)
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`Fingerprint Matching <ref-class-project-fingerprint-matching>`
     - Batch Data Analytics
     - NIST Special Database 14, 29, 30
     - - Apache Hadoop
       - Spark
       - HBase 
   * - :ref:`Human and Face Detection from Video (simulated streaming data) <ref-class-project-human-and-face-detection>`
     - Streaming Data Analytics
     - OpenCV, INRIA Person Dataset
     - - Apache Hadoop
       - Spark
       - OpenCV
       - Mahout
       - MLlib
   * - :ref:`Live Twitter Analysis <ref-class-project-live-twitter>`
     - Streaming Data Analytics
     - Live Twitter feed
     - - Apache Strom
       - HBase
       - Twitter's Search and Streaming APIs, 
       - D3.js
       - Tableau
   * - :ref:`Big data Analytics for Healthcare Data/Health informatics <ref-class-project-healthcare>`
     - Batch Data Analytics
     - Medicare Part-B in 2014
     - - Apache Hadoop
       - Spark
       - HBase
       - Mahout
       - Lucene/Solr
       - MLlib
   * - :ref:`Spatial Big data/Spatial Statistics/Geographic Information Systems <ref-class-project-spatial-bigdata>`
     - Batch Data Analytics
     - Uber Ride Sharing GPS Data 
     - - Apache Hadoop 
       - Spark
       - GIS-tools
       - Mahout
       - MLlib 
   * - :ref:`Data Warehousing and Data mining <ref-class-project-data-warehousing>`
     - Batch Data Analytics
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

Possible Projects from BigDataBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Possible Projects from BigDataBench, ICT, Chinese Academy of Sciences**
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - `Amazon Movie Reviews <http://snap.stanford.edu/data/web-Movies.html>`_
     - Batch Data Analytics
     - `8 million reviews <http://snap.stanford.edu/data/movies.txt.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Google web graph <http://snap.stanford.edu/data/web-Google.html>`_
     - Batch Data Analytics
     - `Webgraph from Google, 2002 <http://snap.stanford.edu/data/web-Google.txt.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Facebook Social Network <http://snap.stanford.edu/data/egonets-Facebook.html>`_
     - Batch Data Analytics
     - `Facebook data <http://snap.stanford.edu/data/facebook.tar.gz>`_
     - - Hadoop
       - Spark
       - MPI
   * - `Genome sequence data <http://ccl.cse.nd.edu/software/sand/>`_
     - Batch Data Analytics
     - ``.cfa`` sample data
     - Work Queue

You can find more examples in the following link.
* \**Reference URL of these projects: http://prof.ict.ac.cn/BigDataBench/#Benchmarks

Possible Projects from IU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Possible Projects From IU
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`Author Name Disambiguation for Bibliometric Data <project_namedisambugiuty>`
     - Batch Data Analytics
     - https://github.com/scienceimpact/bibliometric
     - - graphdb
       - neo4j
       - Apache Giraph
       - mongodb
       - d3.js
       - sql
       - REST
   * - Analysis of Census Data Category*
     - Batch Data Analytics
     - http://www.census.gov/population/www/cen2010/glance/ 
     - - HBase
       - Hadoop
       - Mahout
       - Spark/MLlib
       - D3

* \*Take data from US Census (you can use GE data on location of light bulbs if you want!)
  such as http://www.census.gov/population/www/cen2010/glance/
  Injest into Hbase.
  Build an analytics toolkit e.g. clustering people location with Hadoop/Mahout or Spark/MLlib
  Execute on a virtual cluster and visualize with D3.js. 

Report Style Projects
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. list-table:: Report Style Projects
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - Survey HPC-ABDS
        - http://bigdataopensourceprojects.soic.indiana.edu/#section3
     - Report style Project
     - 
     - Several topics such as review level 17 (orchestration), Compare level 6 (DevOps) and level 15B (PaaS Frameworks) and level 17
   * - :ref:`A Paper on Container Technologies for BigData <project_namedisambugiuty2>`
        - :ref:`A Survey of DevOps Frameworks in support of Big Data <project_namedisambugiuty3>`
        - :ref:`A Survey of Online PaaS Frameworks and Clouds in support of Big Data <project_namedisambugiuty4>`
     - Report style Project
     - 
     - - Docker
       - CoreOS
       - Kubernetes
       - Redhat Atomic
       - Marathon
       - Mesos
       - Heroku
       - CloudLab
       - Chameleon Cloud
       - AWS
       - Azure
       - HP Helion

Projects from Other Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Projects From Ohter Sources
   :widths: 30 10 10 10
   :header-rows: 1

   * - Title
     - Category
     - Data Sets
     - Technologies
   * - :ref:`Predicting Airline Delays with Hadoop <ref-class-project-airline-delays>`
     - Batch Data Analytics
     - Airline delay dataset 2007, 2008
     - - Hadoop
       - Apache Pig
       - Python
       - Pandas
       - HDFS
       - scikit-learn
   * - :ref:`Daily Variation of Barometric Pressure <ref-class-project-barometric-pressure>`
     - Data Processing Batch Data Analytics
     - Quality Controlled Local Climatological Data
     - - IPython Notebook 2.0 
       - Pandas
       - Numpy
       - matplotlib
       - d3.js
   * - :ref:`Data Visualization <ref-class-project-visualization>`
     - Big Data Visualization
     - Project dataset from DonorsChoose.org
     - - D3.js
       - DC.js
       - Python
       - MongoDB
   * - :ref:`MapReduce Implementation for Longest Common Substring Problem <ref-class-project-lcs>`
     - Batch Data Analytics
     - Escherichia coli K-12
     - - Python
       - Amazon
       - MapReduce
   * - :ref:`MapReduce Implementation for GFF Parsing <ref-class-project-gff>`
     - Batch Data Analytics
     - 
     - - Python
       - Disco
       - Amazon EC2
       - MapReduce

* :ref:`List of Possible Datasets <ref-class-lesson-list-dataset>`
* :ref:`List of Possible Technologies <ref-class-lesson-list-tech>`

Project Expectation (Grade)
-------------------------------------------------------------------------------

Projects are expected to software based and can receive full credit up to a
grade of A+. Report style projects have a best possible grade of A-.

Details on Software based Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Source code on Github: https://github.com/futuresystems
* Written report: 4-6 pages
   - Test instruction (if necessary)
   - List of data source
   - List of technologies used

Details on Report Style Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Report should be at least 10 pages (individuals, 15 pages 2 person team, 20
pages 3 person) long in Time Roman 11 point -- spacing 1.1 in Microsoft Word.
Figures can be included and proper citations must be included.
*Use IU Canvas to submit your final report.*

Use many examples given above to choose a project. You can follow one of these
examples or choose your own.

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

Report Style Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If you've chosen report style projects, you must submit a paper to IU Canvas.
* Report should be at least 10 pages (individuals, 15 pages 2 person team, 20
pages 3 person) long in Time Roman 11 point -- spacing 1.1 in Microsoft Word.
Figures can be included and proper citations must be included.

Questions & Support
-------------------------------------------------------------------------------

* Course TA's email: coursehelp@futuresystems.org
* Office Hours: Wednesday 7pm or Thursday 10am via `Adobe Connect <https://connect.iu.edu/bdossp_sp15/>`_

