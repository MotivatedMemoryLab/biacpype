def logged(logger):
    def decorate(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                logger.info(func.__name__ + " OK!")
                return
            except Exception as e:
                logger.error(e)
        return wrapper
    return decorate

