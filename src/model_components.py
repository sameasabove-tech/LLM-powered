
from dataclasses import dataclass
import time

@dataclass
class PromptInput:
    """
    _summary_
    
    """
    text_original: str
    text_processed: str
    id: int = 1 # set id to 1, but change this to call the util function after 
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))


@dataclass
class PromptOutput:
    """
    _summary_
    
    """
    text: str
    id: int = 1

