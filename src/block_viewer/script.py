from bitcoin.core.script import CScript


class Script(object):
    def __init__(self, script=None):
        self.script = script

    def parse_from_binary(self, script_data):
        self.script = CScript(script_data)
        return self.script

    def __repr_(self):
        return '<script: {script}>'.format(script=self.script)
