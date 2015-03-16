import cmd

class Codecs(cmd.Cmd, object):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'codecs] '
        self.last_output = ''

    def do_b64(self, s):
        a = s.split()
        if not len(a) == 2:
            self.help_b64()
            return

        if a[0] == 'enc':
            self.last_output = a[1].encode('base64')
            print self.last_output
        elif a[0] == 'dec':
            self.last_output = a[1].decode('base64')
            print self.last_output
        else:
            print 'Unknown option:', a[0]

    def help_b64(self):
        print 'Usage: b64 [dec|enc] <string>'

    def do_b64b(self, s):
        a = s.split()
        if len(a) < 2:
            self.help_b64b()
            return

        if a[0] == 'enc':
            try:
                with open(a[1], 'r') as fh:
                    data = fh.read()
            except IOError:
                print 'Unable to open %s for reading' % a[1]
                return

            self.last_output = data.encode('base64')
            print self.last_output
        elif a[0] == 'dec':
            try:
                with open(a[2], 'w') as fh:
                    data = a[1].decode('base64')
                    fh.write(data)
            except IOError:
                print 'Unable to open %s for writing' % a[2]
                return
        else:
            print 'Unknown option:', a[0]

    def help_b64b(self):
        print 'Usage: b64b enc <filename> or b64b dec <string> <filename>'

    def do_r13(self, s):
        a = s.split()
        if len(a) != 2:
            self.help_r64()
            return

        if a[0] == 'enc':
            self.last_output = a[1].encode('rot13')
            print self.last_output
        elif a[0] == 'dec':
            self.last_output = a[1].decode('rot13')
            print self.last_output
        else:
            print 'Unknown option:', a[0]

    def help_r13(self):
        print 'Usage: r13 [dec|enc] <string>'

    def do_exit(self, s):
        return True
