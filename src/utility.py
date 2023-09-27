from spellchecker import SpellChecker


def simple_spellchecker(prompt_text):
    """"
    __sumamary__

    """

    spell = SpellChecker(distance=1) # change to 2 for longer words

    for word in spell.unknown(prompt_text.split()):
        try:
            prompt_text = prompt_text.replace(word, spell.correction(word))
        except:
            pass

    return prompt_text 