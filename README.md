# TietoliikenneProjekti

![image](https://github.com/AatuLintulahti/TietoliikenneProjekti/assets/122259056/f6c0d717-6bd8-41fc-8171-bcee3f77b3b3)


Overview of the program

This project involves designing the receiver of the NRF5340DK, aimed at students challenging their skills in sensor data collection and IoT interaction. The main task is to use NRF5340DK, previously known as "Thingy", to measure sensor data (such as from an accelerometer) and wirelessly transmit this information to the IoT router, specifically the Raspberry Pi

Data transmission and storage

The Raspberry Pi plays an important role in this process, acting as a bridge between the Thingy and the Oamk MySQL server. It receives sensor data from the Thingy and sends it to the server for storage. This system ensures a seamless flow of data from sensors to a centralized database, making the data accessible for further analysis.

database connections and APIs

A key feature of this framework is the addition of a TCP socket interface and a simple HTTP API for database communication. These interfaces provide robust and flexible tools for data acquisition and manipulation. The TCP socket interface is particularly good for real-time data communication, and the HTTP API provides a more standardized and consistent way to access data

Data acquisition and machine learning applications

The core of this project is to retrieve hidden data for machine learning. Developers have created a customized program that retrieves data from a MySQL database using an HTTP interface on a physical PC. This data is then processed and used in machine learning application K-Means. The focus is on the potential application of the collected data in machine learning models, exploring its potential in predictive analytics, pattern recognition etc.
