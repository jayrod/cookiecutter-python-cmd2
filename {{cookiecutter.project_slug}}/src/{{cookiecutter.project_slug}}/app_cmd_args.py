from argparse import ArgumentParser

class ParserFactory:

    @classmethod
    def parser(self, parser_name: str) -> ArgumentParser:
        """ This function will create an argument parser given a parser name"""

        #First argument parser
        def speak_parser():
 
            parser = ArgumentParser()
            parser.add_argument('-p', '--piglatin', action='store_true', help='atinLay')
            parser.add_argument('-s', '--shout', action='store_true', help='N00B EMULATION MODE')
            parser.add_argument('-r', '--repeat', type=int, help='output [n] times')
            parser.add_argument('words', nargs='+', help='words to say')
            
            return parser

        #Add other like minded arugument parsers here


        #This return statement performs all of the magic
        #after you add a new parser function add it to 
        #this return statement
        return {
            'speak_parser': speak_parser
            }.get(parser_name, lambda: 'Not a valid parser name')()



