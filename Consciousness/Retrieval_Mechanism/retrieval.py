from Models.model import queryModel, textModel, audioModel, imageModel, videoModel
from Vision.Text.text_functions import text_retrieval
from Audio.audio_functions import audio_retrieval
from Vision.VisualFrame.StaticFrames.image_functions import image_retrieval
from Vision.VisualFrame.Video.video_functions import video_retrieval
from Thinking.NeuralStructure.neural_structure_functions import thought_retrieval
from Feeling.Emotional_Feeling.emotional_feeling_functions import feeling_retrieval

class RetrievalMechanism:
    def __init__(self, query: queryModel): 
        self.query = query
        
    def retrieve(self):
        
        if self.query is None:
            raise ValueError("Query cannot be None!")
        
        if isinstance(self.query.Query, textModel):
            return self.retrieve_text(self.query)
        elif isinstance(self.query.Query, audioModel):
            return self.retrieve_audio(self.query)
        elif isinstance(self.query.Query, imageModel):
            return self.retrieve_image(self.query)
        elif isinstance(self.query.Query, videoModel):
            return self.retrieve_video(self.query)
        else:
            raise TypeError("Unsupported query type!")
        
    def retrieve_text(self):
        '''
        Retrieves text from tokentized data
        '''
        return text_retrieval(self.query)
    
    def retrieve_audio(self):
        '''
        Retrieves audio text from audio data
        '''
        return audio_retrieval(self.query)
        
    def retrieve_image(self):
        '''
        Retrieves image captions from image data
        '''
        return image_retrieval(self.query)
    
    def retrieve_video(self):
        '''
        Retrieves video captions from video data
        '''
        return video_retrieval(self.query)
    
    def retrieve_thoughts(self):
        '''
        Retrieves thoughts from the query
        '''
        return thought_retrieval(self.query)
    
    def retrieve_feelings(self):
        '''
        Retrieves feelings from the query
        '''
        return feeling_retrieval(self.query)
    