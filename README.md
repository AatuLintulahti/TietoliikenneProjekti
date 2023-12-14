# TietoliikenneProjekti

![image](https://github.com/AatuLintulahti/TietoliikenneProjekti/assets/122259056/f6c0d717-6bd8-41fc-8171-bcee3f77b3b3)


## Overview of the program

This project involves creating software for the NRF5340DK, PC, and Raspberry PI. The main task is to use NRF5340DK to measure sensor data from an accelerometer and wirelessly transmitting this data using bluetooth to the IoT router, specifically the Raspberry Pi. The Rasperry Pi will move said data to a MySQL server hosted by OAMK. This data will then be download to be used as training data for a K-means algorithm.

## Data transmission and storage

The Raspberry Pi plays an important role in this process, acting as a bridge between the NRF5340DK and the Oamk MySQL server. It receives sensor data from the NRF5340DK and sends it to the server for storage, making the data accessible for further analysis.

## Database connections and APIs

A key feature of this framework is the addition of a TCP socket interface and a simple HTTP API for database communication. These interfaces provide robust and flexible tools for data acquisition and manipulation. The TCP socket interface is particularly good for real-time data communication, and the HTTP API provides a more standardized and consistent way to access data

## Data acquisition and machine learning applications

The core of this project is to retrieve hidden data for machine learning. We have created a program that retrieves data from a MySQL database using an HTTP interface on a PC. This data is then processed and used in machine learning K-means application. The focus is on the potential application of the collected data in machine learning models, exploring its potential in predictive analytics, pattern recognition etc.

![3d scatterplot](https://github.com/AatuLintulahti/TietoliikenneProjekti/assets/122258677/2deecb3f-6ba0-41fb-9d7c-79d52ca7a76c)

## Confusion matrix

Here is a confusion matrix implemented on the NRF5340DK that represents the degree of error in the predictions of the K-means algorithm by comparing expected results from the the accelerometer and algorithms predictions.

![kuva](https://github.com/AatuLintulahti/TietoliikenneProjekti/assets/122258677/0c5e76c2-9b64-443a-858f-2e41a12eb9cb)
