#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__   = 'GPL v3'
__copyright__ = '2021, Khiem'
__docformat__ = 'restructuredtext en'

from calibre.gui2.actions import InterfaceAction
from calibre.customize import InterfaceActionBase
from calibre.gui2 import error_dialog
from calibre.ebooks.metadata.meta import get_metadata, set_metadata
from calibre_plugins.add_google_style_bibtex_key.gen import gen

class InterfacePluginBase(InterfaceActionBase):
    name                = 'Add Google style Bibtex key'
    description         = 'Auto add generated Google style BibTex key'
    supported_platforms = ['windows', 'osx', 'linux']
    author              = 'Khiem'
    version             = (0, 0, 1)
    minimum_calibre_version = (0, 7, 53)
    actual_plugin = 'calibre_plugins.add_google_style_bibtex_key:AddGoogleStyleBibTexKey'

class AddGoogleStyleBibTexKey(InterfaceAction):
    name = 'Add Google style Bibtex key'
    action_spec = (_('Generate Bibtex key'), None, None, None)
    action_type = 'current'
    
    def genesis(self):
        self.qaction.triggered.connect(self.gui.iactions['View']._view_calibre_books)
        orig_func = self.gui.iactions['View']._view_calibre_books

        def add_google_style_bibtex_key(book_ids):
            # View the book(s)
            orig_func(book_ids)
            # Then update the date stamp
            db = self.gui.library_view.model().db
            bibtex_column = '#bibtexkey'
            custom_columns = db.custom_field_keys()
            # Make sure column exists
            if bibtex_column not in custom_columns: 
                return error_dialog(self.gui, 'Before running this plugin', 
                        'You need to create a custom Bibtex key column called %s '%bibtex_column, show=True)
            label = db.field_metadata.key_to_label(bibtex_column)
            print(label)

            for book_id in book_ids:
                print(book_id)

                current_bibtex = ''
                try:
                    current_bibtex = db.get_custom(book_id, label=label)
                except:
                    print('ignore')

                print(current_bibtex)

                if current_bibtex == '' or current_bibtex is None:
                    # https://github.com/kovidgoyal/calibre/blob/3dd95981398777f3c958e733209f3583e783b98c/src/calibre/db/legacy.py
                    mi = db.get_metadata(book_id, index_is_id=True, get_cover=False, cover_as_data=False)

                    # db.author.last_name + db.published.year + db.first two words of the book title in lower case, for example: punamusta2020were

                    generated_bibtex_key = gen.generate_bibtex(mi.authors, mi.pubdate, mi.title)

                    db.set_custom(book_id, generated_bibtex_key, label=label, commit=True)
        # thanks to Kovid Goyal for the following line, also for Calibre in general
        self.gui.iactions['View']._view_calibre_books = add_google_style_bibtex_key
