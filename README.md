# Executing UAV-Drone control

- With the emerging 5G/6G technologies, drones or unmanned aerial vehicles (UAVs) are widely expected to result in enabling new types of applications and services in cities. Such applications include delivery of items both at the intermediate points in the supply-chain as well as the last mile, sensing of various environmental parameters such as air pollution, mosquito breeding sites as well as infrastructural usage like the conditions of roads and traffic loads. They can also provide connectivity services to users by positioning themselves in proper locations so that they can serve as WiFi hotspots[2].

- These applications typically use a network of drones that are controlled either by a centralized or local controller. Controlling such a network of drones, however, brings in a number of challenges. First, most of these applications require coordination among the drones. A network of drones use the cellular network to send the sensed data, as well as receive the control information. However, for such a system to work reliably, it is essential for the drones to get the control information within a specific end-to-end latency(defined in §8) [6]

- Such low latencies can usually not be obtained by simply performing the computation at the cloud, as recent prior studies have shown latency up to 130 ms over the cloud [6]. The standard technique of reducing latency is to install compute nodes closer to the sensors. This can either be in the base stations, or at the drones themselves, referred to as edge compute nodes and local compute nodes respectively. However, there are costs involved in reducing latency using such compute resources, including power consumption and hardware installation/maintenance. Thus, enabling such a network of drones requires a good understanding of the tradeoffs involved between cost and latency.

- Drones or unmanned aerial vehicles (UAVs) are widely expected to result in enabling new types of applications and services in cities. Such applications include delivery of items both at the intermediate points in the supply-chain as well as the last mile [1], sensing of various environmental parameters such as air pollution, mosquito breeding sites as well as infrastructural usage like the conditions of roads [5, 3] and traffic loads [3]. They can also provide connectivity services to users by positioning themselves in proper locations so that they can serve as WiFi hotspots [2]. 

- A number of studies have designed prototypes and simulation based techniques to enable these applications. We would primarily focus on implementing and benchmarking custom control applications which would gather sensor data from remote/worker UAVs and would make decisions on a central UAV. This central UAV would manage a small swarm of remote/worker UAVs. 

## Problem statement
The goal of this project is to use P4Pi to implement sample P4 programs for UAV applications on Raspberry Pi, implement a network of drones, and share control data between the drone clients and controller drones. We want to profile the control message communication latencies under varying knobs such as the size of transmitted/received control data.

## Work

![](https://github.com/ashcode028/UAV-RPI-Control/blob/62317cf102dadd3f681a3a5699dc543152e1da58/images/Screenshot%20from%202022-05-15%2016-06-07.png)
### Results

|Strategy | Datapoints/sec |Throughput (Kb/sec)|
|Single Thread tcp|366.55|5.864|
|Single Thread udp|325.105|5.249|
|Basic Message Queue|374.153|5.986|


![](https://github.com/ashcode028/UAV-RPI-Control/blob/62317cf102dadd3f681a3a5699dc543152e1da58/images/Screenshot%20from%202022-05-15%2016-06-02.png)
### Results
|Strategy| Datapoints/sec |Throughput (Kb/sec)|
|Single Thread tcp | 355.821|5.693|
|Single Thread udp |325.105|5.249|
|Basic Message Queue|365.363|5.840|


## References
[1] Swiggy, anra conduct first-ever delivery trials of food, medicine with drones. 

[2] I. Donevski, C. Raffelsberger, M. Sende, A. Fakhreddine, and J. J. Nielsen. An Experimental Analysis on Drone-Mounted Access Points for Improved Latency-Reliability, page 3136. Association for Computing Machinery, New York, NY, USA, 2021. 

[3] H. Menouar, I. Guvenc, K. Akkaya, A. S. Uluagac, A. Kadri, and A. Tuncer. Uav-enabled intelligent transportation systems for the smart city: Applications and challenges. IEEE Communications Magazine, 55(3):22–28, 2017. 

[4] M. Quigley, K. Conley, B. Gerkey, J. Faust, T. Foote, J. Leibs, R. Wheeler, A. Y. Ng, et al. Ros: an open-source robot operating system. In ICRA workshop on open source software, volume 3, page 5. Kobe, Japan, 2009. 

[5] C. Suduwella, A. Amarasinghe, L. Niroshan, C. Elvitigala, K. De Zoysa, and C. Keppetiyagama. Identifying mosquito breeding sites via drone images. In Proceedings of the 3rd Workshop on Micro Aerial Vehicle Networks, Systems, and Applications, DroNet ’17, page 2730, 2017. 

[6] M. Xu, Z. Fu, X. Ma, L. Zhang, Y. Li, F. Qian, S. Wang, K. Li, J. Yang, and X. Liu. From Cloud to Edge: A First Look at Public Edge Platforms, page 3753. Association for Computing Machinery, 2021.

