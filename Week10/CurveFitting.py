from numpy import *

def LinearLeastSquaresFit(x,y):
    """Take in arrays representing (x,y) values for a set of linearly varying data and 
    perform a linear least squares regression.  Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties."""
    
    xBracket = average(x)
    yBracket = average(y)
    xSquaredBracket = average(x ** 2)
    xyBracket = average(x * y)
    slope = (xyBracket - xBracket * yBracket) / (xSquaredBracket - xBracket ** 2)
    intercept = (xSquaredBracket * yBracket - xBracket * xyBracket) / (xSquaredBracket - xBracket ** 2)
    d = y - (slope * x + intercept)
    slerr = sqrt(1 / (len(d) - 2.) * average(d ** 2) / (xSquaredBracket - xBracket ** 2))
    interr = sqrt(1 / (len(d) - 2.) * average(d ** 2) * xSquaredBracket / (xSquaredBracket - xBracket ** 2))
    
    return slope, intercept, slerr, interr

def WeightedLinearLeastSquaresFit(x, y, w):
    """Take in arrays representing (x, y) values for a set of linearly varying data and an array of weights w.
    Perform a weighted linear least sqares regression.  Return the resulting slope and intercept 
    parameters of the best fit line with their uncertainties.

    If the weights are all equal to one, the uncertainties on the parameters are calulated using the
    non-weighted least squares equations."""
    
    slope = (sum(w) * sum(w * x * y) - sum(w * x) * sum(w * y)) / (sum(w) * sum(w * x ** 2) - (sum(w * x)) ** 2)
    intercept = (sum(w * x ** 2) * sum(w * y) - sum(w * x) * sum(w * x * y)) / (sum(w) * sum(w * x ** 2) - (sum(w * x)) ** 2)
    slerr = sqrt((sum(w)) / (sum(w) * sum(w * x ** 2) - (sum(w * x)) ** 2))
    interr = sqrt((sum(w * x ** 2)) / (sum(w) * sum(w * x ** 2) - sum(w * x) ** 2))
    
    return slope, slerr, intercept, interr
