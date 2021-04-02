# for running unit tests on 6.00/6.0001/6.0002 student code

import os
import string
import sys
import unittest
import random
from contextlib import redirect_stdout

import ps4b as student


# A class that inherits from unittest.TestCase, where each function
# is a test you want to run on the student's code. For a full description
# plus a list of all the possible assert methods you can use, see the
# documentation: https://docs.python.org/3/library/unittest.html#unittest.TestCase
class TestPS4B(unittest.TestCase):

    def setUp(self):
        self.text1 = 'testing message'
        self.text2 = 'A m4ssage with punctuation in it+... Fun!'
        self.text3 = 'zzzzz~~~~....'
        self.text4 = 'he,(llo)'

        self.msg1 = student.Message(self.text1)
        self.msg2 = student.Message(self.text2)
        self.msg3 = student.Message(self.text3)
        self.msg4 = student.Message(self.text4)

        self.pads = [[71, 12, 44, 87, 81, 30, 61, 5, 66, 19, 73, 91, 19, 8, 83],
                     [34, 92, 62, 59, 32, 91, 21, 81, 94, 37, 20, 76, 17, 20, 7, 30, 3, 28, 21, 14, 67, 9, 91, 49, 4, 87, 25, 12, 88, 68, 37, 18, 62, 30, 79, 82, 83, 71, 7, 86, 77],
                     [73, 72, 17, 48, 0, 0, 34, 40, 45, 87, 25, 48, 16],
                     [47, 45, 29, 87, 44, 8, 87, 61]]
        self.ptmsg1 = student.PlaintextMessage(self.text1, self.pads[0])
        self.ptmsg2 = student.PlaintextMessage(self.text2, self.pads[1])
        self.ptmsg3 = student.PlaintextMessage(self.text3, self.pads[2])
        self.ptmsg4 = student.PlaintextMessage(self.text4, self.pads[3])

    def test_message_get_message_text(self):
        response = self.msg1.get_message_text()
        self.assertEqual(response, self.text1,
                         "get_message_text returned %s, but %s was expected" % (response, self.text1))
        response = self.msg2.get_message_text()
        self.assertEqual(response, self.text2,
                         "get_message_text returned %s, but %s was expected" % (response, self.text2))
        response = self.msg3.get_message_text()
        self.assertEqual(response, self.text3,
                         "get_message_text returned %s, but %s was expected" % (response, self.text3))

    def test_message_shift(self):
        shifts = [('A',5,'F'), ('a',10,'k'), (' ', -1,'~'), ('-',8,'5'), ('}',4,'"'), ('k',-3,'h'), ('Y',-12,'M')]
        for char,shift,exp in shifts:
            result = self.msg1.shift_char(char,shift)
            self.assertEqual(exp, result, "Shifting the character '{}' by {} resulted in '{}' but '{}' was expected".format(char, shift, result, exp))

    def test_message_apply_pad(self):
        pads = [(self.msg1, 'testing message', [84, 69, 6, 5, 21, 25, 1, 79, 35, 54, 35, 45, 60, 83, 45], 'iKyy~(ho1<7A>[3'),
                (self.msg2, 'A m4ssage with punctuation in it+... Fun!', [1, 56, 14, 14, 61, 42, 18, 26, 43, 63, 91, 22, 63, 87, 77, 73, 17, 56, 44, 40, 2, 36, 13, 35, 77, 0, 70, 39, 3, 87, 49, 7, 88, 38, 16, 70, 56, 45, 46, 0, 25], 'BX{BQ>s"1_s T`mZ\'G0=w&"-]nf1qw;{$T>tXsDn:'),
                (self.msg3, 'zzzzz~~~~....', [62, 30, 73, 77, 42, 11, 13, 51, 68, 79, 25, 90, 9], 'Y9dhE*,Rc}G)7'),
                (self.msg4, 'he,(llo)', [91, 6, 73, 31, 63, 26, 19, 1], "dkuGL'#*")]

        for m,msg,pad,exp in pads:
            result = m.apply_pad(pad)
            self.assertEqual(exp, result, "Applying a pad to '{}' resulted in '{}' but '{}' was expected".format(msg, result, exp))

    def test_plaintext_message_generate_pad(self):
        plaintexts = ((self.ptmsg4, [49, 53, 5, 33, 65, 62, 51, 38]),
                      (self.ptmsg3, [49, 53, 5, 33, 65, 62, 51, 38, 61, 45, 74, 27, 64]),
                      (self.ptmsg2, [49, 53, 5, 33, 65, 62, 51, 38, 61, 45, 74, 27, 64, 17, 36, 17, 12, 79, 32, 68, 90, 77, 18, 39, 12, 93, 9, 87, 42, 60, 71, 12, 45, 55, 40, 78, 81, 26, 70, 61, 56]),
                      (self.ptmsg1, [49, 53, 5, 33, 65, 62, 51, 38, 61, 45, 74, 27, 64, 17, 36]))

        for p,exp in plaintexts:
            random.seed(0)
            result = p.generate_pad()
            self.assertEqual(len(exp), len(result), "The length of the generated pad is {} but {} was expected".format(len(result), len(exp)))
            self.assertEqual(exp, result, "The generated pad is {} but {} was expected".format(result, exp))


    def test_plaintext_message_pad(self):
        pds = [(self.ptmsg1, self.pads[0], [63, 34, 46, 81, 31, 88, 60, 42, 10, 68, 40, 28, 86, 71, 10]),
                (self.ptmsg2, self.pads[1], [19, 44, 12, 44, 40, 28, 24, 8, 42, 77, 77, 54, 81, 11, 8, 88, 77, 42, 88, 82, 55, 0, 29, 43, 34, 55, 89, 13, 25, 56, 34, 88, 74, 58, 16, 34, 79, 26, 68, 74, 15]),
                (self.ptmsg3, self.pads[2], [52, 87, 79, 89, 15, 80, 69, 63, 54, 66, 68, 86, 16]),
                (self.ptmsg4, self.pads[3], [63, 73, 66, 38, 11, 47, 66, 19])]
        for p, init_pad, set_pad in pds:
            result=p.get_pad()
            self.assertEqual(init_pad, result, "The PlaintextMessage was initialized with the pad {} but get_pad() returned {}".format(init_pad, result))
            p.change_pad(set_pad)
            result=p.get_pad()
            self.assertEqual(set_pad, result, "The PlaintextMessage pad was changed to {} but get_pad() returned {}".format(set_pad, result))

        random.seed(0)
        new_plaintext = student.PlaintextMessage('Testing generating pad!')
        result = new_plaintext.get_pad()
        exp = [49, 53, 5, 33, 65, 62, 51, 38, 61, 45, 74, 27, 64, 17, 36, 17, 12, 79, 32, 68, 90, 77, 18]
        self.assertEqual(exp, result, "The randomly generated PlaintextMessage pad was {} but {} was expected".format(result, exp))

    def test_plaintext_message_encrypted_msg(self):
        pds = [(self.ptmsg1, '\\q@l[-E%Px]otoY', [63, 34, 46, 81, 31, 88, 60, 42, 10, 68, 40, 28, 86, 71, 10], 'T(Bf)gDJwJ<0XOo'),
                (self.ptmsg2, "c|Lo4ovYdE,V&|'/x+x#Yjp;sf9ugd/'iL}!s.|en", [19, 44, 12, 44, 40, 28, 24, 8, 42, 77, 77, 54, 81, 11, 8, 88, 77, 42, 88, 82, 55, 0, 29, 43, 34, 55, 89, 13, 25, 56, 34, 88, 74, 58, 16, 34, 79, 26, 68, 74, 15], "TLy`<0yo0me@fs(ic9\\gMa252Fyv(X,muh>Po`ZY0"),
                (self.ptmsg3, 'dc,Kz~AGL&G^>', [52, 87, 79, 89, 15, 80, 69, 63, 54, 66, 68, 86, 16], 'Orjt*od^Upr%>'),
                (self.ptmsg4, '83I 9tgf', [63, 73, 66, 38, 11, 47, 66, 19], 'HOnNw<R<')]
        for p, init_enc, new_pad, new_enc in pds:
            result = p.get_encrypted_message_text()
            self.assertEqual(init_enc, result, "The encrypted message returned was {} but {} was expected".format(result, init_enc))
            p.change_pad(new_pad)
            result = p.get_encrypted_message_text()
            self.assertNotEqual(init_enc, result, "change_pad did not update the encrypted message")
            self.assertEqual(new_enc, result, "The encrypted message returned was {} but {} was expected".format(result, new_enc))
        random.seed(0)
        new_plaintext = student.PlaintextMessage('Testing generating pad!')
        result = new_plaintext.get_encrypted_message_text()
        exp = '&;x6KM;FE3Y!Sr9zzW@U\\R3'
        self.assertEqual(exp, result, "The PlaintextMessage encrypted message from a randomly generated pad was {} but {} was expected".format(result, exp))

    def test_encrypted_message_decrypt(self):
        pds = (('Monoo#', [5,10,2,3,0,2], 'Hello!'),
                ('05<Nvv`\\.8_0qvh?b?', [59, 44, 50, 90, 86, 13, 13, 60, 64, 46, 70, 74, 45, 86, 5, 93, 15, 57], 'ThiS iS MixED cASe'),
                ("8fxvr6/C'9 _^[G4uXCN", [68, 85, 19, 19, 9, 52, 34, 35, 67, 48, 30, 76, 74, 33, 40, 24, 87, 38, 26, 46], 'Special Chars:~{}2) '),
                ('m]+h{eF&p.f\\eT]?Xb;K!{5', [25, 84, 33, 84, 91, 92, 68, 18, 80, 33, 86, 77, 93, 78, 74, 31, 68, 89, 49, 68, 12, 8, 18], 'This has longer shifts#'))
        for enc,pad,exp in pds:
            enc_msg = student.EncryptedMessage(enc)
            result = enc_msg.decrypt_message(pad)
            self.assertNotEqual(exp, enc_msg.apply_pad(pad), "Decrypting a message should negate the pad, not just apply it!")
            self.assertEqual(exp, result, "The decrypted message returned was {} but {} was expected".format(result, exp))

    def test_encrypted_message_try_pads(self):
        pds = (('Monoo#', [[22, 3, 32, 36, 41, 66], [31, 3, 92, 42, 49, 56], [58, 56, 75, 15, 1, 93], [5,10,2,3,0,2], [21, 92, 39, 23, 89, 2], [87, 69, 69, 11, 76, 62]], 'Hello!', [5,10,2,3,0,2]),
                ('05<Nvv`\\.8_0qvh?b?', [[42, 27, 38, 56, 8, 70, 7, 45, 17, 54, 51, 53, 69, 50, 40, 86, 67, 73], [59, 44, 50, 90, 86, 13, 13, 60, 64, 46, 70, 74, 45, 86, 5, 93, 15, 57], [43, 94, 13, 15, 33, 72, 27, 94, 28, 20, 54, 74, 67, 54, 7, 86, 70, 57], [25, 28, 94, 37, 58, 10, 52, 63, 30, 92, 72, 43, 34, 4, 3, 56, 73, 22], [72, 54, 52, 43, 47, 36, 67, 93, 16, 8, 25, 23, 22, 28, 59, 10, 2, 54], [89, 81, 94, 89, 23, 26, 53, 44, 31, 78, 50, 45, 71, 82, 79, 76, 22, 8]], 'ThiS iS MixED cASe', [59, 44, 50, 90, 86, 13, 13, 60, 64, 46, 70, 74, 45, 86, 5, 93, 15, 57]),
                ("8fxvr6/C'9 _^[G4uXCN", [[51, 32, 46, 74, 57, 81, 50, 58, 12, 78, 24, 76, 34, 66, 50, 60, 77, 5, 86, 75], [69, 37, 11, 94, 53, 18, 61, 72, 7, 45, 69, 88, 5, 58, 31, 56, 31, 44, 67, 41], [27, 35, 38, 26, 2, 84, 86, 85, 77, 40, 89, 80, 41, 78, 86, 5, 39, 50, 18, 43], [30, 12, 35, 7, 86, 43, 81, 87, 43, 57, 10, 26, 8, 31, 83, 56, 94, 83, 94, 33], [68, 85, 19, 19, 9, 52, 34, 35, 67, 48, 30, 76, 74, 33, 40, 24, 87, 38, 26, 46], [56, 34, 14, 73, 67, 35, 15, 17, 1, 16, 51, 7, 28, 31, 46, 26, 68, 84, 21, 91]], 'Special Chars:~{}2) ', [68, 85, 19, 19, 9, 52, 34, 35, 67, 48, 30, 76, 74, 33, 40, 24, 87, 38, 26, 46]),
                ('m]+h{eF&p.f\\eT]?Xb;K!{5', [[2, 48, 28, 94, 78, 42, 81, 58, 70, 78, 34, 47, 36, 47, 9, 39, 6, 45, 25, 82, 82, 49, 44], [11, 17, 9, 5, 71, 72, 35, 64, 44, 37, 59, 59, 80, 71, 59, 13, 86, 92, 44, 49, 38, 7, 15], [14, 60, 33, 28, 54, 63, 46, 46, 9, 73, 33, 25, 33, 87, 59, 69, 28, 92, 12, 22, 68, 40, 70], [25, 84, 33, 84, 91, 92, 68, 18, 80, 33, 86, 77, 93, 78, 74, 31, 68, 89, 49, 68, 12, 8, 18], [52, 52, 84, 23, 89, 81, 58, 71, 23, 31, 16, 27, 14, 11, 61, 91, 29, 32, 50, 37, 70, 59, 39], [3, 1, 91, 67, 74, 89, 76, 13, 64, 16, 90, 77, 7, 69, 12, 2, 73, 67, 15, 53, 47, 5, 94]], 'This has longer shifts#', [25, 84, 33, 84, 91, 92, 68, 18, 80, 33, 86, 77, 93, 78, 74, 31, 68, 89, 49, 68, 12, 8, 18]))
        for enc_msg,pads,exp_msg,exp_pad in pds:
            enc = student.EncryptedMessage(enc_msg)
            result_pad, result_msg = enc.decrypt_message_try_pads(pads)
            self.assertEqual(exp_pad, result_pad, "decrypt_message_try_pads returned {} as the best pad but {} was expected".format(result_pad, exp_pad))
            self.assertEqual(exp_msg, result_msg, "decrypt_message_try_pads returned the correct pad and {} as the decrypted story when {} was expected".format(result_msg, exp_msg))

        enc = student.EncryptedMessage("bad")
        result_pad, result_msg = enc.decrypt_message_try_pads([[1,2,3],[2,3,4]])
        self.assertEqual([1,2,3], result_pad, "decrypt_message_try_pads should return the first pad if none of them decrypt")
        self.assertEqual('a_a', result_msg, "decrypt_message_try_pads should return the first pad's decryption if none of them decrypt")



# Dictionary mapping function names from the above TestCase class to
# the point value each test is worth.
point_values = {
    'test_message_get_message_text': 0.25,
    'test_message_shift':.5,
    'test_message_apply_pad': .5,
    'test_plaintext_message_generate_pad':.5,
    'test_plaintext_message_pad':.5,
    'test_plaintext_message_encrypted_msg':.5,
    'test_encrypted_message_decrypt':.25,
    'test_decode_story':0,
    'test_encrypted_message_try_pads':.5,
}

# Subclass to track a point score and appropriate
# grade comment for a suit of unit tests


class Results_600(unittest.TextTestResult):

    # We override the init method so that the Result object
    # can store the score and appropriate test output.
    def __init__(self, *args, **kwargs):
        super(Results_600, self).__init__(*args, **kwargs)
        self.output = []
        self.points = 3.5

    def addFailure(self, test, err):
        test_name = test._testMethodName
        msg = str(err[1])
        self.handleDeduction(test_name, msg)
        super(Results_600, self).addFailure(test, err)

    def addError(self, test, err):
        test_name = test._testMethodName
        self.handleDeduction(test_name, None)
        super(Results_600, self).addError(test, err)

    def handleDeduction(self, test_name, message):
        point_value = point_values[test_name]
        if message is None:
            message = 'Your code produced an error on test %s.' % test_name
        self.output.append('[-%s]: %s' % (point_value, message))
        self.points -= point_value

    def getOutput(self):
        if len(self.output) == 0:
            return "All correct!"
        return '\n'.join(self.output)

    def getPoints(self):
        return self.points


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPS4B))
    result = unittest.TextTestRunner(
        verbosity=2, resultclass=Results_600).run(suite)

    output = result.getOutput()
    points = result.getPoints()

    if points < .1:
        points = 0

    print("\nProblem Set 4B Unit Test Results:")
    print(output)
    print("Points: %s/3.5\n" % points)
