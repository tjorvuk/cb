def dispatch(func, delta, freq, args = [], window=100, dbg=False):
    if(delta % freq <= window):
        if(dbg): print((delta % freq), 'dispatched at delta: ', delta)
        func(*args)

def main(load_module, delta, run_command):
    dispatch(lambda: load_module('hello').main(), delta, 1)
    dispatch(lambda: load_module('report').main(), delta, 300 * 1000)
    # dispatch(lambda: print('-----'), delta, 1)
    # dispatch(lambda: run_command('update'), delta, 60 * 5 * 1000, dbg=True)

