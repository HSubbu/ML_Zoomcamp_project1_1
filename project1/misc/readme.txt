Problem Statement
A campus recruitment program is a program conducted within universities or 
other educational institutions that helps students as they near graduation find employment.
As part of this program, educational institutions partner with corporations that wish to
recruit from student populations.The placement of a student depends on various factors 
like their performance in school and colleges, work experience, etc.The objective here is 
to predict if a student will get placed or not.

1.  VS code editor was used for buulding  the project along with jupyter notebook.The Notebook 
project1\ML_Zoomcamp_project1.ipynb contains the orginal python code for EDA and model 
building.

2. The train.py is python script from the above notebook which generates project_one_model.pkl
from training the model

3. The project1\placement-test.py is for loading and checking if saved model is working fine
with a sample data.

4. The term Web service is either: a service offered by an electronic device 
to another electronic device, communicating with each other via the World Wide Web, 
or a server running computer device,serving web documents. A web service to predict whether 
a candidate will get placed has been developed and can be used by Collge Authorties

5. An user will request service of our service by passing candidate details and webservice
will return probability of Placement of candidate

6. predict.py is a python script for webservice using flask framework. The 
file takes input in terms of candidate (list of dictionaries)
and returns probability of placement

7. seeking_webservcie.ipynb is a notebook which runs the requests to the webservice
and passes teh candidate details to webservice as a json and gets output as a json. 
For availing the webservice, pass on a list of python dictionary containing the features and 
probability of Placement would be the output. 

8. The file waitress_server.py runs a WSGI server waitress for the webservice.
Run python3 waitress_server.py and thereafter pass requests to webservice through the 
seeking_webservice.ipynb for getting the results. We can also pass the requests through 
seeking_webservice.py by running the cmd python3 seeking_webservcice.py on another terminal 

9. pipenv version 2021.5.29 has been installed to create Virtual env for the project.

10. A Dockerfile has been created for running the app in a container.

11. Run following cmds to run the webservice . It is assumed that 
candidate profile is already available in seeking_webservice.py
  $ docker build -t placement-prediction .
  $ docker run -it -p 9696:9696 placement-prediction 


