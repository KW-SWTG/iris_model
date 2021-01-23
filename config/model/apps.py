from django.apps import AppConfig
import pickle

class ModelConfig(AppConfig):
    name = 'model'
    models = pickle.load(open("C:\\Users\\이주연\\iris_model.sav", "rb"))
