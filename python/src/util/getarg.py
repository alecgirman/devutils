# getarg(argv, ['-f', '--file'], 'r', 'Input file')

# Flags:
# --- value flags ---
# r - Required

def getarg(argv, opt, flags, atype, helpmsg):
    required = 'r' in flags
    usevalue = 'v' in flags

    for idx, arg in enumerate(argv):
        do_argcheck = arg in opt
        for o in opt:
            do_argcheck = do_argcheck or o in arg
        if do_argcheck:
            valuestr = ''
            if arg.startswith('--'):
                if usevalue:
                    valuestr = arg[arg.index('=') + 1:] if '=' in arg else argv[idx + 1]
                else:
                    return True
            elif arg.startswith('-'):
                
                if usevalue:
                    valuestr = arg[2:] if len(arg) > 2 else argv[idx + 1]
                else:
                    return True
            else:
                pass # dont know what to do here
            if atype == 'float':
                return float(valuestr)
            if atype == 'int':
                return int(valuestr)
            if atype == 'str':
                return valuestr
