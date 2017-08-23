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
- Run `conda create -n ml-workshop`. This creates a sandbox where we'll install all the software we'll need.
- Activate the environment: `activate ml-workshop`
- Install the needed libraries:
  * `conda install matplotlib numpy pandas jupyter theano`
  * `conda install -c conda-forge keras`

### Set up development environment (Mac)

#### 1) Clone this repository.

#### 2) Install Python
Go to your terminal and type `python`. If you get `command not found` that means Python isn't installed. You can install it by doing the following:

- Install `brew` by entering: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
- Type `brew install python`

If all goes well you should type `python` in your terminal and see something like this:

```
Python 2.7.10 (default, Feb  7 2017, 00:08:15)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

#### 3) Install Virtualenv
Virtualenv is a python library that helps us build an isolated (virtual) development environment.

- From your commandline, install `virtualenv` by running the following command: `pip install virtualenv`
- Move to the directory of this repository: `cd machine-learning-workshop`
- Create the virtual environment: `virtualenv ml-workshop`
- Activate the environment: `source ml-workshop/bin/activate`

#### 4) Install required libraries.
After you've activated `virtualenv`, run the following command:

`pip install -r pip-requirements.txt`

The command above should install all the software we'll need for the workshop.
