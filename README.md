## Simulating Shoreline Change using Coupled Coastsat and Coastline Evolution Model (CEM)
This lab couples two coastal models: _CoastSat_ and _Coastal Evolution Model (CEM)_ in a jupyter notebook to allow users to explore shoreline change using real, observed shorelines and wave data. 

We use CoastSat to download and extract shorelines from satellite imagery.
These shorelines feed into the CEM where they are evolved by historical wave characteristics from a nearby buoy.

## Getting Started
##### Running this lab requires some advanced preparation (up to 1-2 days)
  ### Step 1. Download this repository to your local machine. 

  ### Step 2. Create a virtual environment
We recommend using anaconda to help manage your python packages - all of the following instructions assume you have Anaconda3 installed and working on your machine.
Open the Anaconda prompt (PC) or terminal (Mac, Linux) and ```cd``` (change directory) into the folder of this repo.

Create a new environment using the environment.yml file to install all the required packages
```
conda env create -f environment.yml -n coast_env
```

Now activate the new environment
```
conda activate coast_env
```

  ### Step 3. Activate Google Earth Engine Python API

Request access to Google Earth Engine at https://signup.earthengine.google.com/. It takes about 1 day for Google to approve requests.
Once your request has been approved, activate your coast_env environment and run the following command in Anaconda prompt/the terminal:
```earthengine authenticate```
A web browser will open, login with a gmail account and accept the terms and conditions. Then copy the authorization code into the Anaconda terminal.

  ### Step 4. You're now ready to run this notebook!

Type ```jupyter notebook``` in the terminal. A webpage will open showing your local repository in the jupyter application. Open the coastal notebook and start clicking!
* note : remember to activate your virtual environment each time you use this lab.


**More information on CoastSat: https://github.com/kvos/CoastSat**

**More information on CEM: https://csdms.colorado.edu/wiki/Model:CEM**

**We also use functions developed by nickc1 to download NDBC buoy data - see https://github.com/nickc1/buoypy**
