# How to run this project?

Run the server-side Flask app in one terminal window:


    $ cd server
    $ python -m venv env
    $ source env/bin/activate
    
    (env)$ pip install -r requirements.txt
    (env)$ pip install -r ./text_processing_module/requirements.txt
    (env)$ python app.py


Run the client-side Vue app in a different terminal window:


    $ cd client
    $ npm install
    $ npm run serve
    
    Navigate to localhost(http://localhost:8080)
