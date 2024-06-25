def get_model(model_name):
    if model_name == 'msclap':
        from models.msclap import CLAP
        return CLAP
    elif model_name == 'mspengi':
        from models.mspengi import Pengi
        return Pengi
    else:
        raise NameError("Model with name: {} is not found.".format(model_name))