def dispatch(func, delta, freq, *args, window=100):
    if(delta % freq <= window):
        # print((delta % freq), 'dispatched at delta: ', delta)
        func(*args)

def main(load_module, delta):
    # print('elapsed:', delta)
    dispatch(lambda: load_module('hello').main(), delta, 1)
