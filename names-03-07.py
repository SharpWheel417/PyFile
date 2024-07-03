import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', '--name', default='name')
    parser.add_argument ('-c', '--count', default=0, type=int)

    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

for i in range(0,namespace.count):
    print ("Меня зовут, {}!".format (namespace.name))
