# Dette er en hjælper til håndtering af filer (f. eks. til webapps af tvivlsom kvalitet)
import os

class FileHandler:

    def __init__(self, directory='/'):
        self.directory = os.path.join(directory)

    def list_md_files(self):
        """Gennemgå biblioteket og opret en liste over filer, der slutter med '.md'."""
        return [file for file in os.listdir(self.directory) if file.endswith('.md')]

    def write_file(self, filename, content):
        with open(os.path.join(self.directory, filename), 'w', encoding='utf-8') as f:
            f.write(content)