import requests
import bots.basebot as bb

_STORY_URL = "http://twentythreemillionstories.org/api/story/generate"


class StoriesBot( bb.BaseBot ):

    def __init__( self ):
        print( "StoriesBot init" )


    def can_handle( self, message ):
        return message.lower().startswith("story")


    def fetch_story( self ):
        r = requests.get( _STORY_URL )
        return r.json()


    def handle( self, message ):
        story = self.fetch_story()
        return story[ "story" ]

