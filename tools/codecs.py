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
        try:
            cmd, data = s.split(None, 1)
        except ValueError:
            self.help_b64()
            return

        s = self.set_to_last(data)

        if cmd == 'enc':
            try:
                self.last_output = s.encode('base64')
                print self.last_output
            except Exception, e:
                print e.message

        elif cmd == 'dec':
            try:
                self.last_output = s.decode('base64')
                print self.last_output
            except Exception, e:
                print e.message

        else:
            print 'Unknown command:', cmd

    def help_b64(self):
        print 'Usage: b64 [dec|enc] <string>'

    def do_b64b(self, s):
        try:
            cmd, data = s.split(None, 1)
        except ValueError:
            self.help_b64()
            return

        if cmd == 'enc':
            try:
                with open(data, 'r') as fh:
                    data = fh.read()
            except IOError:
                print 'Unable to open %s for reading' % data
                return

            try:
                self.last_output = data.encode('base64')
                print self.last_output
            except Exception, e:
                print e.message

        elif cmd == 'dec':
            d = data.split()[:-1]
            filename = data.split()[-1]

            s = self.set_to_last(d)
            try:
                data = s.decode('base64')
            except Exception, e:
                print e.message
                return

            try:
                with open(filename, 'w') as fh:
                    fh.write(data)
            except IOError:
                print 'Unable to open %s for writing' % filename
        else:
            print 'Unknown command:', cmd

    def help_b64b(self):
        print 'Usage: b64b enc <filename> or b64b dec <string> <filename>'

    def do_r13(self, s):
        try:
            cmd, data = s.split(None, 1)
        except ValueError:
            self.help_b64()
            return

        s = self.set_to_last(data)

        if cmd == 'enc':
            try:
                self.last_output = s.encode('rot13')
                print self.last_output
            except Exception, e:
                print e.message

        elif cmd == 'dec':
            try:
                self.last_output = s.decode('rot13')
                print self.last_output
            except Exception, e:
                print e.message
        else:
            print 'Unknown command:', cmd

    def help_r13(self):
        print 'Usage: r13 [dec|enc] <string>'

    def do_bin(self, s):
        try:
            cmd, data = s.split(None, 1)
        except ValueError:
            self.help_b64()
            return

        s = self.set_to_last(data)

        if cmd == 'enc':
            try:
                self.last_output = ' '.join(format(ord(c), 'b').
                                            zfill(8) for c in s)
                print self.last_output
            except Exception, e:
                print e.message

        elif cmd == 'dec':
            try:
                bin_str = ''.join(s[1:])
                n = int(bin_str, 2)
                self.last_output = binascii.unhexlify('%x' % n)
                print self.last_output
            except Exception, e:
                print e.message

        else:
            print 'Unknown command:', cmd

    def help_bin(self):
        print 'Usage: bin [dec|enc] <string>'

    def do_hex(self, s):
        try:
            cmd, data = s.split(None, 1)
        except ValueError:
            self.help_b64()
            return

        s = self.set_to_last(data)

        if cmd == 'enc':
            try:
                self.last_output = binascii.hexlify(s)
                print self.last_output
            except Exception, e:
                print e.message

        elif cmd == 'dec':
            try:
                self.last_output = binascii.unhexlify(s)
                print self.last_output
            except Exception, e:
                print e.message

        else:
            print 'Unknown command:', cmd


    def help_hex(self):
        print 'Usage: hex [dec|enc] <string>'

    def do__(self, s):
        print self.last_output

    def do_exit(self, s):
        return True
