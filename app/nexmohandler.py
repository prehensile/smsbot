import os
import nexmo 

class NexmoHandler( object ):

    def __init__( self ):
        self._client = nexmo.Client(
            key=os.environ.get("NEXMO_KEY"),
            secret=os.environ.get("NEXMO_SECRET")
        )
    

    def parse_request( self, fields ):
        return {
            "message" : fields.get( "text" ),
            "originating_number" : fields.get( "msisdn" ),
            "receiving_number" : fields.get( "to" )
        }
    

    def send_message( self, to_number=None, message=None, from_name='SMSBot' ):
        response = self._client.send_message({
            'from': from_name,
            'to': to_number,
            'text': message
        })
        return response

    

