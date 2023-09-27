
import time
from uuid import uuid1
from dataclasses import dataclass


@dataclass
class PromptInput:
    """
    _summary_
    
    """
    text_original: str
    text_processed: str
    id = uuid1() 
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))


@dataclass
class PromptOutput:
    """
    _summary_
    
    """
    text: str
    id: int 

