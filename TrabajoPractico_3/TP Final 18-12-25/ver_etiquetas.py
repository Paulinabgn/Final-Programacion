import pickle

with open('./data/claims_clf.pkl', 'rb') as archivo:
    clasificador = pickle.load(archivo)

print("Etiquetas posibles que puede predecir el clasificador:")
print(clasificador.encoder_.classes_)
