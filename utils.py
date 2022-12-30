import pickle
import numpy as np
import config # var, fun, classes

with open(config.MODEL_FILE_PATH,"rb") as f:
    model = pickle.load(f)

def get_price(data):
    CRIM     = eval(data['CRIM'])
    ZN       = eval(data['ZN'])
    INDUS    = eval(data['INDUS'])
    CHAS     = eval(data['CHAS'])
    NOX      = eval(data['NOX'])
    RM       = eval(data['RM'])
    AGE      = eval(data['AGE'])
    DIS      = eval(data['DIS'])
    RAD      = eval(data['RAD'])
    TAX      = eval(data['TAX'])
    PTRATIO  = eval(data['PTRATIO'])
    B        = eval(data['B'])
    LSTAT    = eval(data['LSTAT'])

    new_test_array = np.array([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, 
                        DIS, RAD, TAX, PTRATIO, B, LSTAT],ndmin = 2)

    predicted_value = model.predict(new_test_array)[0]
    print("predicted_value :",predicted_value)
    return np.around(predicted_value,3)