import logging
import importlib
import os, sys


from bots.basebot import BaseBot

class BotHandler( object ):

    def __init__( self ):
        self._bots = []
        self.load_bots()


    def load_bots( self ):
        logging.debug( "BotHandler.load_bots()...")
        loaded = []
        for fn in os.listdir( "bots" ):
            if fn.startswith("__"):
                continue
            mn = os.path.splitext(fn)[0]
            mn = "bots.%s" % mn
            module = importlib.import_module( mn, package=None )
            for name, val in module.__dict__.items():
                try:
                    if( issubclass(val, BaseBot) and (val is not BaseBot) ):
                        bot = val()
                        loaded.append( bot )
                except:
                    pass
        self._bots = loaded
        

    def handle( self, message ):
        messages = []
        for bot in self._bots:
            if bot.can_handle( message ):
                messages.append(
                    bot.handle(message)
                )
        return messages


def main():
    # test handling a message
    bh = BotHandler()
    message = "STORY"
    if len( sys.argv ) > 1:
        message = sys.argv[1]
    print( bh.handle( message ) )

if __name__ == '__main__':
    main()

