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
    print (ConfigFile.read)
    ConfigFile.close

