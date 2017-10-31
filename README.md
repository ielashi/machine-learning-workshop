# Machine Learning for Software Developers ([Video](https://www.youtube.com/watch?v=9x1vF8Jl_Qs))

This repository contains material for a short workshop on machine learning. It is intended for software developers who have little to no experience in the field.

## Workshop Outline

- Day 1 ([Slides](http://bit.ly/2gqTYu8))
  * What is learning?
  * What is programmed vs what is learned
  * A high-level look into brains (neurons and synapses)
  * Code deep-dive: building a brain and teaching it to recognize Arabic digits
  * Exercise 1: teaching a brain to recognize English digits
- Day 2 ([Slides](http://bit.ly/2wTmH1C))
  * Recap of day 1
  * A gentle introduction to neural networks
  * Building a neural network using Keras
  * Exercise 2: building a neural network to recognize Arabic characters

## Setting up (do this before the workshop)

The following instructions will guide you through setting up so that you have all the software and datasets needed for the workshop.

### Create an account on [Kaggle](https://www.kaggle.com/)
You'll need this account for some of the projects we'll be doing.

### Download the datasets
- [Arabic Handwritten Digits Dataset](https://www.kaggle.com/mloey1/ahdd1)
- [MNIST Dataset](https://www.kaggle.com/c/digit-recognizer/data) (download both `train.csv` and `test.csv`)
- [Arabic Handwritten Characters Dataset](https://www.kaggle.com/mloey1/ahcd1)

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

#### 2) Download and install Anaconda (Python 2.7) from [here](https://www.continuum.io/downloads).

#### 3) Set up the development environment.
To set up the development environment, you'll need to do the following:
- In your terminal run: `conda create -n ml-workshop`. This creates a sandbox where we'll install all the software we'll need.
- Activate the environment: `source activate ml-workshop`
- Install the needed libraries:
  * `conda install matplotlib numpy pandas jupyter theano`
  * `conda install -c conda-forge keras`
