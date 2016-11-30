import matplotlib 
from PIL import Image 
import numpy as np
import constants as c 


i = Image.open(c.constants.Dot)
iar = np.asarray(i)
print(i)
print(iar)
