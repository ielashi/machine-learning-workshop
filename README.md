# Machine Learning for Software Developers

This two-day workshop is intended for software developers who have little to no experience in machine learning.

## Setting up (do this before the workshop)

The following instructions will guide you through setting up so that you have all the software and datasets needed for the workshop.

### Create an account on [Kaggle](https://www.kaggle.com/)
You'll need this account for some of the projects we'll be doing.

### Download the datasets
- [Arabic Handwritten Digits Dataset](https://www.kaggle.com/mloey1/ahdd1)
- [MNIST Dataset](https://www.kaggle.com/c/digit-recognizer/data) (download both `train.csv` and `test.csv`)

### Set up development environment (Windows)

#### 1) Clone this repository.

#### 2) Download and install Anaconda (Python 2.7) from [here](https://www.continuum.io/downloads).

#### 3) Set up the development environment.
To set up the development environment, you'll need to do the following:
- Open `Anaconda Prompt`
- Move to the directory of this repository: `cd machine-learning-workshop`
- Load the environment: `conda env create -f windows-environment.yml`. This will install the needed software libraries.

### Set up development environment (Mac)

#### 1) Clone this repository.

#### 2) Install Virtualenv
Virtualenv is a python library that helps us build an isolated (virtual) development environment.

- From your commandline, install `virtualenv` by running the following command: `pip install virtualenv`
- Run the following command: `sudo /usr/bin/easy_install virtualenv`
- Move to the directory of this repository: `cd machine-learning-workshop`
- Create the virtual environment: `virtualenv ml-workshop`
- Activate the environment: `source ml-workshop/bin/activate`

#### 3) Install required libraries.
After you've activated `virtualenv`, run the following command:

`pip install -r pip-requirements.txt`

The command above should install all the software we'll need for the workshop.
