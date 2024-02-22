import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv('laptop_pricing.csv')
data = dataset.drop(columns=['Manufacturer'])
data = pd.get_dummies(data)
data