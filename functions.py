#!/usr/bin/python3

"""
Module representing a set of commonly used activation functions.
"""

from typing import TypeVar, Union, List
from classtools import Verifiers
from math import e, log, exp
from numpy import (
    array,
    float16,
    float32,
    float64,
    int16,
    int32,
    int64,
    int8,
    ndarray,
    uint16,
    uint32,
    uint64,
    uint8,
)

verify_type = Verifiers.verify_type

__nptypes = (
    float16,
    float32,
    float64,
    int16,
    int32,
    int64,
    int8,
    uint16,
    uint32,
    uint64,
    uint8,
)

npnum = TypeVar("npnum")

def step(x: Union[int, float, npnum], threshold: Union[int, float] = 0) -> int:
    """
    Heaviside step function.
    
    Args:
        x (Union[int, float, npnum]): Input value.
        threshold (Union[int, float]): Threshold value.
        
    Returns:
        int: 1 if x >= threshold, else 0.
    """
    x = verify_type(x, (int, float, *__nptypes))
    threshold = verify_type(threshold, (int, float, *__nptypes))
    return 1 if x >= threshold else 0

def sigmoid(x: Union[int, float, npnum]) -> float:
    """
    Sigmoid function.
    
    Args:
        x (Union[int, float, npnum]): Input value.
        
    Returns:
        float: Sigmoid of x.
    """
    x = verify_type(x, (int, float, *__nptypes))
    return 1 / (1 + exp(-x))

def relu(x: Union[int, float, npnum]) -> float:
    """
    Rectified Linear Unit function.
    
    Args:
        x (Union[int, float, npnum]): Input value.
        
    Returns:
        float: ReLU of x.
    """
    x = verify_type(x, (int, float, *__nptypes))
    return max(0, x)

def leaky_relu(x: Union[int, float, npnum]) -> float:
    """
    Leaky Rectified Linear Unit function.
    
    Args:
        x (Union[int, float, npnum]): Input value.
        
    Returns:
        float: Leaky ReLU of x.
    """
    x = verify_type(x, (int, float, *__nptypes))
    return x if x >= 0 else x / 10

def tanh(x: Union[int, float, npnum]) -> float:
    """
    Hyperbolic Tangent function.
    
    Args:
        x (Union[int, float, npnum]): Input value.
        
    Returns:
        float: Tanh of x.
    """
    x = verify_type(x, (int, float, *__nptypes))
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

def softmax(x: Union[List[float], ndarray], n: int = None) -> List[float]:
    """
    Softmax function.
    
    Args:
        x (Union[List[float], ndarray]): Input vector.
        n (int, optional): Index for a specific value. Defaults to None.
        
    Returns:
        List[float]: Softmax distribution.
    """
    x = verify_type(x, (list, ndarray))
    e_x = [exp(i) for i in x]
    sum_e_x = sum(e_x)
    distr = [i / sum_e_x for i in e_x]

    if n is not None:
        verify_type(n, int)
        return [distr[n]]
    
    return distr

def prelu(x: Union[int, float, npnum], lp: Union[int, float, npnum]) -> float:
    """
    Parametric Rectified Linear Unit function.
    
    Args:
        x (Union[int, float, npnum]): Input value.
        lp (Union[int, float, npnum]): Learned parameter.
        
    Returns:
        float: PReLU of x.
    """
    x = verify_type(x, (int, float, *__nptypes))
    lp = verify_type(lp, (int, float, *__nptypes))
    return max(lp * x, x)

def elu(x: Union[int, float, npnum], alpha: Union[int, float, npnum]) -> float:
    """
    Exponential Linear Unit function.
    
    Args:
        x (Union[int, float, npnum]): Input value.
        alpha (Union[int, float, npnum]): Scaling parameter.
        
    Returns:
        float: ELU of x.
    """
    x = verify_type(x, (int, float, *__nptypes))
    alpha = verify_type(alpha, (int, float, *__nptypes))
    return x if x > 0 else alpha * (exp(x) - 1)

def softplus(x: Union[int, float, npnum]) -> float:
    """
    Softplus function.
    
    Args:
        x (Union[int, float, npnum]): Input value.
        
    Returns:
        float: Softplus of x.
    """
    x = verify_type(x, (int, float, *__nptypes))
    return log(1 + exp(x))

