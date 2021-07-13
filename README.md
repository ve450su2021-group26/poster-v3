# How to run this project?

## Server-side

We recommend using Anaconda to manage server-side packages.

1. Install Anaconda3 on your platform

2. Create conda virtual environment:


        $ conda create --name env
        $ conda activate env


3. Run the following codes to install packages:


        (env)$ conda install pytorch torchvision cudatoolkit -c pytorch
        (env)$ conda install scikit-learn
        (env)$ pip install -r requirements.txt
        (env)$ pip install -r ./text_processing_module/requirements.txt


4. Boot Flask app: 
    (env)$ python app.py


## Client-side

Run the client-side Vue app in a different terminal window:


    $ cd client
    $ npm install
    $ npm run serve
    
    Navigate to localhost(http://localhost:8080)
