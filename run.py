def dispatch(func, delta, freq, args = [], window=100, dbg=False):
    if(delta % freq <= window):
        if(dbg): print((delta % freq), 'dispatched at delta: ', delta)
        func(*args)

def main(load_module, delta, run_command):
    # print('elapsed:', delta)

    # dispatch(lambda: load_module('hello').main(), delta, 1)
    dispatch(lambda: print('xxxxx'), delta, 1 * 1000)
    dispatch(lambda: run_command('update'), delta, 10 * 1 * 1000, dbg=True)
