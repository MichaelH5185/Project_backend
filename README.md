# Project_backend
Dependences: python -m pip install requests
To run: open the ./DEW/ folder in the terminal and run the command: python manage.py runserver
Then navigate to http://127.0.0.1:8000 in your browser.
The current design takes a long time to process input because the NWS API limits the number of concurrent requests. I am currently working on a more verbose solution to avoid this problem.
