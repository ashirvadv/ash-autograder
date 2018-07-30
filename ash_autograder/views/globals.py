

def get_all_methods_from_class(class_name):
	result = [func for func in dir(class_name) if callable(getattr(class_name, func)) and not func.startswith("__")]
	return result