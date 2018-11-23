def Config_Open(cfg_f_n):
    if cfg_f_n == '':
        print ('\nFile name cannot be empty\n')
        assert()
    elif cfg_f_n == 'Wrapper.cfg':
        print ("\nFile is correct\n")

    else:
        print ('\nFilename is not correct\n')
        assert()
    ConfigFile = open(cfg_f_n,'r')
    cfg= ConfigFile.read()
    print (cfg)
    while 1==1:
        param = input ("\nplease enter paremetrs for check\n")
        if param in cfg: print('found')
        elif param not in cfg: cfg = cfg + '\nVar = ' + param
        else: print ('not found')
        print ('\n'+cfg)

    ConfigFile.close

