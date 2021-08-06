# C1-Challenge-Reponse
Here is my response for the correlation one backend software engineering challenge. To satisfy the requirements of a DB and API, I built a REST API with SQL ALchemy and Docker in Visual Studio Code. 

Prior to launching this project, you need to download Docker. In the "set-up.md" file, I included the list of packages and code to install and execute this project successfully. 

STEPS:
1. In visual studio code, create a new cmd terminal and run the following code: py -m venv venv . 
2. Next, activate your virtual environment: venv\Scripts\activate 
3. Run the following code to download the images. These images will be used to built the container: docker-compose build 
4. Then run : docker-compose up 
5. Log into pgadmin (http://127.0.0.1:5050) . Click "Servers", then "Object", then "Create", then "Server..."
6. In the "Create-Server" window under the "General" tab, enter the "Name" as "db"
7. Go to the next tab, "Connection", and enter the "Host name/address" as "db". Change the username to "postgres" and the password is "password". Note: this information can be altered within python in the .env file. 
8. Refresh the server, and you will see the assessment_db. 
9. The migration needs to be created, so in the terminal run the code: docker-compose run app alembic revision --autogenerate -m "New Migration"
10. The migration needs to be processed, so run the code: docker-compose run app alembic upgrade head
11. In a browser, check the API at the link: http://127.0.0.1:8000
12. The following link will provide the documentation to add and retrieve user and assessment information : http://127.0.0.1:8000/docs
13. After receiving a 200 response, refresh the tables in pgadmin and you will see the user and assessment information. 


Final thoughts: 
I found this exercise to be very challenging, but I'm glad that I had the opportunity to learn more about relational database management. If I had more time, I would have attempted the following:
- create a random generator that provides each user with a unique session ID for the "session_id" field
- incorporated test questions and a scoring framework to evaluate the tester's submission
- incorporated a time and date field for each assessment submission
- incorporated a method to provide an average score of each user, so as to track their progress 
