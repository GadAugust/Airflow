This repository hosts a beginner-friendly Airflow tutorial project, demonstrating the basics of creating and managing a Directed Acyclic Graph (DAG) in Apache Airflow. The project features a simple DAG configuration named first_demo_dag designed to introduce new users to key Airflow concepts and operators

## Key Components:

Custom Python Operator: A Python function greeting that prints a welcoming message, showcasing how to execute Python code within a DAG.  

Bash Operators: Two Bash tasks demonstrating how to incorporate shell commands within your workflow. The first task executes a brief pause, and the second prints a check-in message.  

DAG Configuration: Outlines how to set up a DAG with custom start dates, retry policies, and scheduling intervals,  **specifically running tasks on weekdays at 1:00 and 23:00.**

Technologies Used:  

Python
Apache Airflow
This project is ideal for those new to Airflow or seeking to understand how to construct a basic workflow using Python and Bash operators.
