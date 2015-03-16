#!/usr/bin/env python

import cmd
import tools.codecs

__VERSION__ = '0.0.1'


class CtfCmd(cmd.Cmd, object):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'ctf] '

    def set_prompt(self, other_cmd):
        other_cmd.prompt = self.prompt[:-2] + ':' + other_cmd.prompt

    def do_codecs(self, s):
        x = tools.codecs.Codecs()
        self.set_prompt(x)
        x.cmdloop()

    def do_exit(self, s):
        return True

def main():
    c = CtfCmd()
    print 'Unlogic CTF tools', __VERSION__
    c.cmdloop()


if __name__ == '__main__':
    main()
