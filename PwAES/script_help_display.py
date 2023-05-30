
def help_display (argv,n_args,docs):
    if len(argv) != n_args + 1:
        print('Error: incorrect number of args entered, see doc string below.\n')
        print(docs)
        input('Hit any key to exit')
        exit()
    if argv[1].lower() in ['-h','--help','h','help']:
        print(docs)
        input('Hit any key to exit')
        exit()