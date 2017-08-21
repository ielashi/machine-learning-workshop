# Machine Learning for Software Developers

This two-day workshop is intended for software developers who have little to no experience in machine learning.

## Setting up (do this before the workshop)

The following instructions will guide you through setting up so that you have all the software and datasets needed for the workshop.

### 1) Clone this repository
### 2) Install Python
If you're using Mac OS, python is already installed so you can skip this step. If you haven't done so already, you'll need to have python 2.7 installed on your machine.  If you're using Windows, you can download python 2.7 from [here](https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi).

*Windows Users:* When you're installing python, make sure to select "Add python.exe to Path" during setup.

After the install, you should be able to go to your command prompt and type:

`python --version`

If python was installed correctly, you'll see an output similar to the following:

`Python 2.7.13`

### 3) Install Virtualenv
Virtualenv is a python library that helps us build an isolated (virtual) development environment.

- From your commandline, install `virtualenv` by running the following command: `pip install virtualenv`
- Move to the directory of this repository: `cd machine-learning-workshop`
- Create the virtual environment: `virtualenv ml-workshop`
- Activate the environment. On Mac OS or Linux, run `source ml-workshop/bin/activate`. On Windows, run `ml-workshop\Scripts\activate`

### 4) Install required libraries.
After you've activated `virtualenv`, run the following command:

`pip install -r pip-requirements.txt`

The command above should install all the software we'll need for the workshop.

*Windows Users:* If you get an error asking you to install the Visual C++ compiler, you can download it from [here](https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266)

### 5) Create an account [Kaggle](https://www.kaggle.com/)
You'll need this account for some of the projects we'll be doing.

### 6) Download the datasets
- [Arabic Handwritten Digits Dataset](https://www.kaggle.com/mloey1/ahdd1)
- [MNIST Dataset](https://www.kaggle.com/c/digit-recognizer/data) (download both `train.csv` and `test.csv`)
