import sys
import json

import numpy as np
from keras.models import load_model

if __name__ == "__main__":
    dict = json.loads(sys.argv[1])
    X1 = float(dict['X1'])
    X2 = float(dict['X2'])
    X3 = float(dict['X3'])

    print(X1, X2, X3)

    X = np.array([X1, X2, X3])
    X = X.reshape(1,3)

    model = load_model('C:\\Users\\nww73\\Documents\\GitHub\\Web\\testapp\\routes\\model.h5')
    pred = np.sum(model.predict(X))

    print(pred)