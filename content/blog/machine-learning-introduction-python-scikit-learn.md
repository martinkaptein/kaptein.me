---
title: "Using machine learning to predict integers from a training set"
date: 2018-08-03
lastmod: 2019-09-21
draft: false
categories:
  - Machine learning
tags:
  - Machine learning
  - Python
  - scikit
  - tutorial
  - predict
slug: machine-learning-introduction-python-scikit-learn
comments: true
description: "This beginner tutorial is an introduction to Machine Learning in Python on how to predict integers from a training set using scikit-learn and the linear regression model."
authors: ["martinkaptein"]
cat:
  - technology
---


In this tutorial we are going to take a look at the simplest basics of Machine Learning. For this we will be using [scikit-learn / sklearn](http://scikit-learn.org/stable/), as an alternative to the Keras and Tensorflow framework, together with [Python](https://www.python.org/).

We will discover how to predict a series of integers based on a set of training data imported from a `.csv` file. Also, feel free to discover [the end result in my Github repository](https://github.com/martinkaptein/integer-predictor). Without further a do, let’s get started!

## Installation

For this we will use Python version 3.x, which can be downloaded [from their website](https://www.python.org/). Also we will need some dependencies. After you have downloaded and installed Python on your machine (UNIX) run:

`sudo pip3 install scikit-learn numpy pandas`

**Note: If you have only one Python installation on your machine, and it is already version 3.x you might have to substitute `pip3` and `python3` for `pip` and `python` in your Terminal or Command Line application.** *(Also, most of the code is compatible with Python 2 anyway, so that shouldn’t really be a problem).*

Also, you might want to prepare a file with a series of integers, that we will use as a training set for our machine learning setup later. The file should look like this:

```
0 ,
2 ,
4 ,
6 ,
8 ,
10 ,
12 ,
```

Save this file as `filename.csv`.

Alternatively you can download [the example.csv file from my Github repository here](https://raw.githubusercontent.com/martinkaptein/integer-predictor/master/example.csv): 

*in your working directory run*
```
wget https://raw.githubusercontent.com/martinkaptein/integer-predictor/master/example.csv
```

Now, create a `yourfilename.py` file and open it with your favourite code editor. Let’s get to the interesting part!

## The code

### Importing the necessary machine learning libraries to Python

Let’s import all the necessary stuff! Begin your file with the lines:

```
import numpy as np
np.set_printoptions(threshold=np.inf)
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings(action="ignore", module="sklearn", message="^internal gelsd")
```

What this does is import **numpy**, which we need for **sklearn**, **sklearn** or **scikit-learn** with the **Linear Regression** model, which we will train and fit later with the training data, as well as **pandas**, which we need to work with `.csv` files.

Also, we use some options to suppress some non-essential warnings, as well as numpy configuration to later print the full result of the prediction.

### Model input and output definition 

Every Machine Learning tool needs input (x) and output (y) variables. This is totally logical, as we expect the machine learning algorithm to find the correlation between an input and output through a training procedure. But we only have a single set of input numbers (integers) that we need to predict. So how do we deal with it?

My solution is to generate a second **dataset** or, better, **array**:

We will use the array of numbers that we want to predict (from our `example.csv`) as an output (=y variable). The input (=x variable) will be a simple linear array of numbers (e.g `0, 1, 2, 3, 4` etc.) with the length of `y`. Hence, we want to feed the machine learning algorithm something like this (with the `example.csv` in mind):


Input x    | Output y
--------|------
0     | 0
1   | 12
2 | 24
3 | 36
4 | 48
5 | 60
6 | 72


Now we can just ask the Machine Learning model: Whats the `output` of the `input = 7`? Or, whats the `output` of the `input = [7,8,9,10,20,30,40]`?

Now it makes much more sense. Let’s implement that in our Python code:

### Reading, indexing and slicing the csv file with Pandas

Let’s first define our output for our model, as it is just the content of our file. We just need to parse it using `pandas`:

*(Remember, the output variable is y, input variable is x)*

```
inputData = pd.read_csv(example.csv, delimiter=',', header=None)
y = inputData.iloc[:,0]  #select first column, next column would be [:,1] etc.
```

Pandas DataFrame indexing and slicing is somewhat confusing to the beginner, just bare with me.

Great! We defined the output of our model! Now, let’s define the input (x).

First let’s get a Python function to build the linear array (1,2,3,etc) of the length of the output, we will call it `linearizer`:

*By the way, there are probably much more elegant solutions out there, but this should do just fine.*

```
def linearizer(lowerLimit, upperLimit): # including lower and upper limit!
    upperLimit += 1
    out = []
    while (lowerLimit < upperLimit):
        out.append(lowerLimit)
        lowerLimit += 1
    return out 
```
 Now, let’s build the array for our input (x):

```
length_y = len(y.index) #Get the length of our output
x = []
x = linearizer(0, (length_y - 1)) #minus 1 to compensate for position 0
```

What we need to do now, is to convert the simple Python array to a Pandas Dataframe. We can do this very simply by:

`x = pd.DataFrame(x)`.

Fantastic, we have our input and output ready for our model to use.

### Defining and training the scikit model

As, I have already stated in the beginning, for this problem, it is wisest to use the Linear Regression model.
Let’s define the model:

`model = LinearRegression()`

Amazing! Now let’s train the model with our input and output.

`model.fit(x, y)`

It literally this simple! By the way, the **Keras** interface works in a very similar way, but we will get there!

### Making predictions with our sklearn model  

Now let’s say that we want to predict n integers ahead / forward.

This can be done really easily with `model.predict()`. The process is, again, similar: We create a pandas array (as input x) for the next n numbers and feed it into model.predict(). We ‘ask’ the model: what are the y for these x?

The code will then look like this:

```
#build new array, 10 positions (as an example) ahead
positionsToPredict = 10 #want to predict future n items
new_data = linearizer(length_y, (positionsToPredict + length_y))
new_data = pd.DataFrame(new_data)

# feed the array into model.predict()
prediction = model.predict(new_data)
```

Finally, print your data:

`print('\nPredictions based on Linear Regression:\n\n',prediction)`

Very finally, run the whole contraption:

`python3 yourfilename.py`

## Conclusion

This concludes the short introduction into the realm of machine learning. Feel free to take a look [at my Github repo here](https://github.com/martinkaptein/integer-predictor/) to view the source code, run or modify the full program.

Also feel free to comment!

