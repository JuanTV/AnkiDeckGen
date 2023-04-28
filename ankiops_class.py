'''AnkiOps class definition to create and manipulate Anki decks and cards programmatically'''

import random
import genanki

class AnkiOps:
    ''' Define a class to create and manipulate Anki decks and cards programmatically'''
    def __init__(self, model_name: str, model_fields: list,
                 model_templates: list, model_id:int):
        '''Initializes Anki_ops class with the following parameters: model name,
            model fields, model_templates be aware that the model_fields
            must be a list of dictionaries with the form 
            {'name': 'field_name'} and the model_templates must be a list of dictionaries
            with the form {'name': 'template_name', 
            'qfmt': 'question_format', 'afmt': 'answer_format'} '''
        self._model = None
        self._model_id = model_id
        self._model_name = model_name
        self._model_fields = model_fields
        self._model_templates = model_templates
        self._deck = None
        self._deck_id = None
    def __str__(self) -> str:
        '''Returns a string with the AnkiOps class parameters'''
        out = {'model_name': self._model_name,
               'model_fields': self._model_fields,
               'model_templates': self._model_templates,
               'deck': self._deck,
               'deck_id': self._deck_id
               }
        return str(out)
    def set_model_name(self, model_name: str) -> None:
        '''Sets the model name'''
        self._model_name = model_name
    def set_model_fields(self, model_fields: list) -> None:
        '''Sets the model fields'''
        self._model_fields = model_fields
    def set_model_templates(self, model_templates: list) -> None:
        '''Sets the model templates'''
        self._model_templates = model_templates
    def set_deck_id(self, deck_id: int) -> None:
        '''Sets the deck ID'''
        self._deck_id = deck_id
    def set_deck(self, deck_name: str, new: bool) -> str:
        '''Sets a Anki deck with the given parameters, if new is True, a new deck is created'''
        if new:
            self._deck_id = random.randrange(1 << 30, 1 << 31)
        self._deck = genanki.Deck(self._deck_id, deck_name)
        return f'Deck ID: {self._deck_id}\nDeck: {self._deck}'
    def add_cards(self, cards: list) -> genanki.Deck:
        '''Adds a list of cards to the deck,
            the list must have the form [{'front': 'question', 'back': 'answer'}, ...]'''
        for front, back in cards:
            note = genanki.Note(model=self._model, fields=[front, back])
            self._deck.add_note(note)
        return self._deck
    def create_model(self) -> genanki.Model:
        '''Creates a new Anki model with the given parameters'''
        self._model = genanki.Model(
            self._model_id,
            self._model_name,
            fields=self._model_fields,
            templates=self._model_templates
        )
        return self._model
    def save_deck(self, path: str) -> None:
        ''' Save the deck to an Anki package (*.apkg) file '''
        genanki.Package(self._deck).write_to_file(path)
    