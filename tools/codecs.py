import cmd
import binascii


class Codecs(cmd.Cmd, object):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'codecs] '
        self.last_output = ''

    def set_to_last(self, s):
        if s == '_':
            s = self.last_output
        return s

    def do_b64(self, s):
        a = s.split()
        if not len(a) == 2:
            self.help_b64()
            return

        s = self.set_to_last(a[1])

        if a[0] == 'enc':
            try:
                self.last_output = s.encode('base64')
                print self.last_output
            except Exception, e:
                print e.message

        elif a[0] == 'dec':
            try:
                self.last_output = s.decode('base64')
                print self.last_output
            except Exception, e:
                print e.message

        else:
            print 'Unknown command:', a[0]

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

            try:
                self.last_output = data.encode('base64')
                print self.last_output
            except Exception, e:
                print e.message

        elif a[0] == 'dec':
            if len(a) < 3:
                self.help_b64b
                return

            s = self.set_to_last(a[1])
            try:
                data = s.decode('base64')
            except Exception, e:
                print e.message
                return

            try:
                with open(a[2], 'w') as fh:
                    fh.write(data)
            except IOError:
                print 'Unable to open %s for writing' % a[2]
        else:
            print 'Unknown option:', a[0]

    def help_b64b(self):
        print 'Usage: b64b enc <filename> or b64b dec <string> <filename>'

    def do_r13(self, s):
        a = s.split()
        if len(a) != 2:
            self.help_r64()
            return

        s = self.set_to_last(a[1])

        if a[0] == 'enc':
            try:
                self.last_output = s.encode('rot13')
                print self.last_output
            except Exception, e:
                print e.message

        elif a[0] == 'dec':
            try:
                self.last_output = s.decode('rot13')
                print self.last_output
            except Exception, e:
                print e.message
        else:
            print 'Unknown command:', a[0]

    def help_r13(self):
        print 'Usage: r13 [dec|enc] <string>'

    def do_bin(self, s):
        a = s.split()

        if len(a) < 2:
            self.help_bin()
            return

        s = self.set_to_last(a[1])

        if a[0] == 'enc':
            try:
                self.last_output = ' '.join(format(ord(c), 'b').
                                            zfill(8) for c in s)
                print self.last_output
            except Exception, e:
                print e.message

        elif a[0] == 'dec':
            try:
                bin_str = ''.join(s[1:])
                n = int(bin_str, 2)
                self.last_output = binascii.unhexlify('%x' % n)
                print self.last_output
            except Exception, e:
                print e.message

        else:
            print 'Unknown command:', a[0]

    def help_bin(self):
        print 'Usage: bin [dec|enc] <string>'

    def do_hex(self, s):
        a = s.split()
        if len(a) < 2:
            self.help_hex()
            return

        s = self.set_to_last(a[1])

        if a[0] == 'enc':
            try:
                self.last_output = binascii.hexlify(s)
                print self.last_output
            except Exception, e:
                print e.message

        elif a[0] == 'dec':
            try:
                self.last_output = binascii.unhexlify(s)
                print self.last_output
            except Exception, e:
                print e.message

    def help_hex(self):
        print 'Usage: hex [dec|enc] <string>'

    def do__(self, s):
        print self.last_output

    def do_exit(self, s):
        return True
