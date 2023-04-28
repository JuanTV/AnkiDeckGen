''' Main script'''

import ankiops_class

def main():
    ''' Main function'''

    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ]
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ]
    # List of Linux directories and their descriptions, these are going to be the cards for our anki deck
    linux_dirs = [
        ('/', 'Root directory, starting point of the filesystem hierarchy.'),
        ('/bin', 'Contains essential system command executables.'),
        ('/sbin', 'Contains essential system administration command executables.'),
        ('/boot', 'Contains files needed to start the boot process.'),
        ('/etc', "Contains system-wide configuration files and scripts."),
        ('/dev', 'Contains device files representing hardware devices.'),
        ('/home', 'Contains personal directories for each user.'),
        ('/lib', 'Contains shared libraries and kernel modules.'),
        ('/opt', 'Optional directory for storing third-party software.'),
        ('/proc', 'Virtual filesystem providing an interface to kernel internal data structures.'),
        ('/sys', 'Virtual filesystem providing an interface to kernel internal data structures for devices, drivers, and other components.'),
        ('/tmp', 'Temporary directory for storing files deleted after a system reboot.'),
        ('/usr', 'Contains user-related files, shared libraries, header files, documentation, and non-essential software binaries.'),
        ('/var', 'Contains variable data files, such as logs, databases, and mail spools.'),
    ]
    linux_ankimodel = ankiops_class.AnkiOps(model_id=1607392319, model_name='Simple Model', model_fields=fields, model_templates=templates)
    print (linux_ankimodel)
    linux_ankimodel.create_model()
    linux_ankimodel.set_deck('Linux Filesystem Deck', True)
    linux_ankimodel.add_cards(linux_dirs)
    linux_ankimodel.save_deck('linux_filesystem_deck.apkg')


    
if __name__ == '__main__':
    main()