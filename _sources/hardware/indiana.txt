.. _s-hardware:

**********************************************************************
Hardware at Indiana University
**********************************************************************

In this section we describe the hardware that is available at Indiana
University and allows you as part of course work or joint projects to
gain easily access to them.


Compute Resources
==================

The tables :ref:`t-clusters` and :ref:`t-clusters-details` show an
overview of some imporatnt information about these clusters.

.. _t-clusters:

.. csv-table:: **Table**: Compute Resources
   :header: Name, System Type           , # Nodes, # CPUS, # Cores, TFLOPS , RAM (GB), Storage (TB), Site

   india        , IBM iDataplex          ,128,256,1024,11,3072,335, IU
   bravo        , HP Proliant            ,16,32,128,1.7,3072,128, IU
   delta        , SuperMicro GPU Cluster ,16,32,192,           ,1333,144, IU
   echo         , SuperMicro ScaleMP Cluster,16,32,192,2,6144,192, IU

.. _t-clusters-details:

.. csv-table:: **Table**: Compute Resource Details
   :header: Name , India,Echo, Bravo, Delta

   Organization, Indiana University,, Indiana University, Indiana University
   Machine Type                           , Cluster                                ,Cluster SclaeMP, Cluster                               , Cluster
   System Type                            , IBM iDataPlex dx 360 M2                ,SuperMicro, HP Proliant                           ,
   CPU type                               , Intel Xeon X5550                       ,Intel Xeon E5-2640, Intel Xeon E5620                      , Intel Xeon 5660
   Host Name                              , india                                  ,echo, bravo                                 , delta
   CPU Speed                              , 2.66GHz                                ,2.50GHz, 2.40GHz                               , 2.80 GHz
   Number of CPUs                         ,256,,32,32
   Number of nodes                        ,128,12,16,16
   RAM                                    , 24 GB DDR3 1333Mhz                     ,, 192 GB DDR3 1333Mhz                   , 192 GB DDR3 1333 Mhz
   Total RAM (GB)                         ,3072,,3072,3072
   Number of cores                        ,1024,144,128,
   Operating System                       , Linux                                  ,, Linux                                 ,Linux
   Tflops                                 ,11,,1.7,
   Disk Size (TB)                         ,335,2.8,,15
   Hard Drives                            , 3000 GB Internal 7200 RPM SATA Drive   ,, 6x2TB Internal 7200 RPM SATA Drive    , Seagate Constellation 7.2 K RPM     64 MB Cache SATA 92GB
   Primary storage shared by all nodes  ,  NFS                                   ,, NFS                                   ,NFS
   Storage details                        ,,,, RAID 9260-4i 1pt SAS2  512 MB SGL
   Connection configuration               , Mellanox 4x DDR InfiniBand adapters    ,, Mellanox 4x DDR InfiniBand adapters   ,
   Primary storage shared by all nodes   ,,,,
   CPUs (cores) per node                  ,,,,2
   Cores per CPU,,,,6
   Total number of GPU cores,,,,192
   GPU type                               ,,,, nVIDIA Tesla C2070
   Cores per GPU,,,,448
   GPUs per node,,,,2
   Batch system                           ,,,, Torque




Networks
======================================================================

.. csv-table::
   :header: Resource Name, Network Devices
   
   IU iDataPlex , DDR IB , QLogic switch with Mellanox ConnectX adapters,Blade Network Technologies & Force10 Ethernet switches
 
 
Below is further information about networking:

.. list-table::
   :header-rows: 1
   :widths: 20,20,60

   * - Resource
     - Network Switch
     - Link
   * - FutureSystems Core
     - Juniper EX8200
     -
   * - India
     - Force10 C-150
     - `Juniper/Dell EX series Force 10 <https://www.juniper.net/us/en/products-services/switching/ex-series/Force10>`__
   * - Bravo
     - Force10 S60
     - `force10-s60 <http://www.dell.com/us/enterprise/p/force10-s60/pd>`__
   * - Delta
     - Force10 S60
     -
   * - Echo
     - Force10 S60
     -
   * - Node NICs
     - built-in (IBM iDataPlex DX360 M2) dual Intel 82575EB Gigabit Network Connection
       10Gbps, Myricom Myri-10G Dual-Protocol NIC (available on login
       node)
     -
 
.. Allan confirmed that we have up-to-date information for network switches on india. Sep 19th, 2014
   .. todo:: Hyungro, get info from Koji or Allan . we need current network swithes inside india 
             old switch is  `IBM rack switches (formerly BNT) <http://www-03.ibm.com/systems/networking/switches/rack.html>`__
             but that switch was replaced
 
 
