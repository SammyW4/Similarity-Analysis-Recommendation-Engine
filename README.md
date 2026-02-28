# INST414-Module-2-Assignment
Web Network Analysis with PageRank
Project Overview

This project analyzes the structure of a web-based network using Python. The goal is to model relationships between web pages as a graph and identify important nodes using the PageRank algorithm.

The network is built as a directed graph where nodes represent web pages and edges represent hyperlinks between them.

Objectives

Construct a directed network graph

Visualize the network structure

Compute the number of nodes and edges

Identify important nodes using PageRank

Interpret the structure of the network

Technologies Used

Python

NetworkX

Matplotlib

Project Structure
network_analysis.py   # Main script
README.md             # Project documentation

(If you have a data file, add it here:)

data.csv              # Edge list data used to build the network
How to Run the Project
1. Install Dependencies
pip install networkx matplotlib
2. Run the Script
python network_analysis.py

The script will:

Build the directed graph

Print the total number of nodes

Print the total number of edges

Display a visualization of the network

Compute and display the top nodes ranked by PageRank

Network Description

Nodes represent web pages (or domains).

Edges represent hyperlinks from one page to another.

The graph is directed, meaning links have direction.

The visualization shows clusters and hub-like nodes, where highly connected nodes appear near the center of the network.

PageRank Analysis

PageRank is used to determine node importance. Nodes with higher PageRank scores are considered more influential because they are connected to other important nodes in the network.

The top-ranked nodes demonstrate which pages act as central hubs within the network.

Key Insights

The network contains peripheral nodes with fewer connections.

A dense core of nodes suggests the presence of hubs.

PageRank highlights influential nodes that play a central role in connectivity.

Conclusion

This project demonstrates how network analysis techniques can be applied to web-based data to understand structure and influence. By combining visualization and PageRank, we can identify key nodes and better interpret the overall network topology.
