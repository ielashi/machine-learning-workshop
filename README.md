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
- Configure Keras (the library we'll use to do machine learning:
  * From your user directory go to the `.keras` directory.
  * If `keras.json` isn't present in the folder, create it. If it's there, update it to make it look like this:
  
  ```
  {
    "floatx": "float32",
    "epsilon": 1e-07,
    "backend": "theano",
    "image_dim_ordering": "th"
  }
  ```

### Set up development environment (Mac)

#### 1) Clone this repository.

#### 2) Download and install Anaconda (Python 2.7) from [here](https://www.continuum.io/downloads).

#### 3) Set up the development environment.
To set up the development environment, you'll need to do the following:
- In your terminal run: `conda create -n ml-workshop`. This creates a sandbox where we'll install all the software we'll need.
- Activate the environment: `source activate ml-workshop`
- Install the needed libraries:
  * `conda install matplotlib numpy pandas jupyter theano`
  * `conda install -c conda-forge keras`
- Configure Keras (the library we'll use to do machine learning:
  * Go to `~/.keras` directory.
  * If `keras.json` isn't present in the folder, create it. If it's there, update it to make it look like this:
  
  ```
  {
    "floatx": "float32",
    "epsilon": 1e-07,
    "backend": "theano",
    "image_dim_ordering": "th"
  }
  ```
