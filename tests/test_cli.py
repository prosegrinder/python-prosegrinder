import shutil
from os import path

from click.testing import CliRunner

from prosegrinder import __main__ as main

TXT_FILENAME = path.join(path.dirname(__file__), 'resources/shortstory.txt')
with open(TXT_FILENAME) as txt_file:
    TXT_CONTENTS = txt_file.read()

def test_cli_defaults():
    JSON_FILENAME = \
        path.join(path.dirname(__file__), 'resources/cli-default.json')
    with open(JSON_FILENAME) as json_file:
        JSON_CONTENTS = json_file.read()
    runner = CliRunner()
    with runner.isolated_filesystem():
        shutil.copyfile(TXT_FILENAME, "shortstory.txt")
        result = runner.invoke(main.cli, ['shortstory.txt'])
        assert result.exit_code == 0
        assert result.output == JSON_CONTENTS
