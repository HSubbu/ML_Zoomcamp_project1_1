# ML_Zoomcamp_project1_1
Development of DS project -Placement App by Subramanian Hariharan

Problem Statement
A campus recruitment program is a program conducted within universities or other educational institutions that helps students as they near graduation find employment. As part of this program, educational institutions partner with corporations that wish to recruit from student populations.The placement of a student depends on various factors like their performance in school and colleges, work experience, etc. This data set consists of Placement data of students in a XYZ campus. It includes secondary and higher secondary school percentage and specialization.
The objective here is to predict if a student will get placed or not.Submissions are evaluated using the Accuracy Score.

Data source https://dphi.tech/challenges/data-sprint-42-campus-recruitment/146/data

The iterative model developed was score 96% for the test set on the website and was used to benchmark the model. The application/webservice has been containerised using Docker to run WSGI server waitress . Detailed description is also provided in a text file with the source files. To run the application 

- go into the project folder
- confirm docker available by $docker --version and $ docker service status 
- build docker file $ docker build -t placement-app .
- run the docker container $ docker run -dit -p 9696:9696 placement-app
- run python script containing test data $ python3 seeking_webservice.py
- output will be displayed on the terminal

