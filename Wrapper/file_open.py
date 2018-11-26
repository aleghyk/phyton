def Config_Open(cfg_f_n, lock_f):
    if cfg_f_n == '':
        print ('\nFile name cannot be empty\n')
        assert()
    elif cfg_f_n == 'Wrapper.cfg':
        print ("\nFile is correct\n")
        lock_f() #fuction call through description which was transfered as var
    else:
        print ('\nFilename is not correct\n')
        #assert()
    try:
        ConfigFile = open(cfg_f_n,'r')
    except:
        print ('incorrect file name'+ cfg_f_n)
        return
    cfg= ConfigFile.read()
    print (cfg)
    temp = list(cfg)
    print ("\nas a list\n")
    print (temp)
    input("continue?")
    while 1==1:
        param = input ("\nplease enter paremetrs for check\n")
        if param in cfg: print('found')
        elif param not in cfg: cfg = cfg + '\nVar = ' + param
        else: print ('not found')
        print ('\n'+cfg)

    ConfigFile.close