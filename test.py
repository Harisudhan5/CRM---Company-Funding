import pickle
import numpy as np
with open('model_crm.pkl', 'rb') as file:
    model = pickle.load(file)
    ar = np.array([[1,1,1,1,1,1]])
    print(model.predict(ar))

    