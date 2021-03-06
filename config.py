from configparser import ConfigParser
from pathlib import Path

# find a better way to look for credentials
def config(filename=Path("C:/Users/Vicente Bispo/Documents/Projetos/Projetos/02 - Finco/credentials.ini"), section='postgresql'):
    #create parser
    parser=ConfigParser()

    #read config
    parser.read(filename)

    #get section, default postgresql
    db = {}
    if parser.has_section(section):
        params=parser.items(section)
        for param in params:
            db[param[0]]=param[1]

    else:
        raise Exception('Section {0} not found in the {1} file'.format(section,filename))

    return db
