import argparse
import sys
from Switch.Switch import CheckKey
from termcolor import colored
__author__ = 'catsec'
__twitter__ = '@catsec1'
__version__ = '1.0.0'
__year__ = '2020'


def Red(value):
    return colored(value, 'red', attrs=['bold'])

def Green(value):
    return colored(value, 'green', attrs=['bold'])


banner = """
{0} 
{1} Killswitch for local Files
{1} Copyright (c) {2} {3} ({4})
""".format(Red('CatSec KillSwitch ' + __version__), Red('--['), __year__, __author__, __twitter__)

parser = argparse.ArgumentParser(description=banner)

parser.add_argument('--file',
                    nargs='?',
                    help='File to encrypt if switch fires')

parser.add_argument('--password', nargs='?',
                    help='Password to encrypt file')

parser.add_argument('--phrase', nargs='?',
                    help='Phrase to activate the encryption')

parser.add_argument('--url', nargs='?',
                    help='Pastbin URL to watch')

parser.add_argument('--directory', nargs='?',
                    help='Directory to encrypt if switch fires')

parser.add_argument('--decrypt', nargs='?',
                    help='Keyphrase to decrypt files')

args = parser.parse_args()
url = args.url
filePath = args.file
password = args.password
phrase = args.phrase
directory = args.directory
decrypt = args.decrypt

__author__  = 'catsec'

def main():
    # no args provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    print(banner)
    CheckKey(url=url, filePath=filePath, password=password, phrase=phrase, directory = directory, decrypt = decrypt)

if __name__ == '__main__':
    main()

