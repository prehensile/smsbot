class BaseBot( object ):

    """
    Base class for bots.
    Extend and override these empty functions to create a workig bot.
    See storiesbot.py for an example working bot.
    """

    def __init__( self ):
        pass
    

    def can_handle( self, message ):
        """
        Should return True or False depending on whether this bot can reply to the passed message. 
        Something like:
            return message.lower().startswith("trigger_word")
        Would give you a bot which replies to messages starting with "trigger_word".
        """
        return False


    def handle( self, message ):
        """
        Handle (process) a message.
        Should return a reply to that message, which gets sent back to the originating mobile number.
        """
        return "Hello, world!"