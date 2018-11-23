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
def list_modif ():
    list1 = ['asd', 2, '1', 'country']
    list2 = [2,5,6,9]
    print (str(list1) + "   &    " + str(list2))
    list1.append(list2 [2])
    list2.insert( int(list1[2]), str(list2[3]))
    print (str (list1) + '    &    ' + str (list2) )


list_modif()
