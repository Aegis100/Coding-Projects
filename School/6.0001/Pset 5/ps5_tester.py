import unittest
import random 
import filecmp
from pydub import AudioSegment

from ps5 import build_scale
from ps5 import build_major_scale
from ps5 import build_minor_scale
from ps5 import add_piano_note, add_perc_note
from ps5 import add_note
from ps5 import scale_to_segment
from ps5 import melody_to_segment
from ps5 import drumline_to_segment
from ps5 import add_drumline_to_song
from music_lib import y_axis_perc_instr
from ps5 import bpm_to_beat_len
from music_lib import segment_to_wav

PREFIX = "./"

class TestPS5(unittest.TestCase):
    # helpers
    def is_within_epsilon(self, true_value, estimated_value, epsilon):
        return abs(true_value - estimated_value) <= epsilon

    def help_check_scale(self, scale, root_pitch, intervals, num_octaves):
        # check scale starts on root pitch
        self.assertTrue(scale[0] == root_pitch, "scale should start with root_pitch")
        # check correct number of octaves generated
        self.assertTrue(len(scale) == (len(intervals) * num_octaves) + 1,
                        "scale length should be (len(intervals) * num_octaves) + 1")
        x = 1 # check intervals between pitches
        while x < len(scale):
            self.assertTrue(scale[x - 1] + intervals[(x % len(intervals)) - 1] == scale[x],
            "incorrect interval between pitches in scale between pitch %d and %d" % (x - 1, x))
            x += 1

            
    # tests
    def test_1_build_scale_1(self):
        # test creation of scales with arbitrary intervals and numbers of octaves
        intervals = [1, 2, 3, 1, 2, 3, 1]
        scale = build_scale(root_pitch=0, intervals=intervals, num_octaves=2)
        if len(scale) == 0:
            self.fail("build_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=0, intervals=intervals, num_octaves=2)
        
    def test_1_build_scale_2(self):    
        intervals =  [3, 2, 1, 1, 1, 2, 3]
        scale = build_scale(root_pitch=48, intervals=intervals, num_octaves=3)
        if len(scale) == 0:
            self.fail("build_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=48, intervals=intervals, num_octaves=3)
        
    def test_1_build_scale_3(self):  
        intervals = [2, 1, 3, 2, 3, 2, 1]
        scale = build_scale(root_pitch=23, intervals=intervals, num_octaves=4)
        if len(scale) == 0:
            self.fail("build_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=23, intervals=intervals, num_octaves=4)
        
    def test_1_build_scale_4(self):    
        intervals = [1, 1, 2, 1, 1, 1, 2]
        scale = build_scale(root_pitch=8, intervals=intervals, num_octaves=7)
        if len(scale) == 0:
            self.fail("build_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=8, intervals=intervals, num_octaves=7)
        
    def test_1_build_scale_5(self):    
        intervals = [2, 2, 1, 2, 1, 2, 1]
        scale = build_scale(root_pitch=50, intervals=intervals, num_octaves=7)
        if len(scale) == 0:
            self.fail("build_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=50, intervals=intervals, num_octaves=7)
        
    def test_2_build_major_scale_1(self): 
        intervals = [2, 2, 1, 2, 2, 2, 1]
        scale = build_major_scale(root_pitch=0, num_octaves=1)
        if len(scale) == 0:
            self.fail("build_major_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=0, intervals=intervals, num_octaves=1)
        
    def test_2_build_major_scale_2(self): 
        intervals = [2, 2, 1, 2, 2, 2, 1]
        scale = build_major_scale(root_pitch=90, num_octaves=2)
        if len(scale) == 0:
            self.fail("build_major_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=90, intervals=intervals, num_octaves=2)
        
    def test_2_build_major_scale_3(self)  :
        intervals = [2, 2, 1, 2, 2, 2, 1]
        scale = build_major_scale(root_pitch=3, num_octaves=8)
        if len(scale) == 0:
            self.fail("build_major_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=3, intervals=intervals, num_octaves=8)
        
    def test_3_build_minor_scale_1(self):
        intervals = [2, 1, 2, 2, 1, 2, 2]
        scale = build_minor_scale(root_pitch=4, num_octaves=1)
        if len(scale) == 0:
            self.fail("build_minor_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=4, intervals=intervals, num_octaves=1)
     
    def test_3_build_minor_scale_2(self):
        intervals = [2, 1, 2, 2, 1, 2, 2]
        scale = build_minor_scale(root_pitch=75, num_octaves=4)
        if len(scale) == 0:
            self.fail("build_minor_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=75, intervals=intervals, num_octaves=4)
        
    def test_3_build_minor_scale_3(self):
        intervals = [2, 1, 2, 2, 1, 2, 2]
        scale = build_minor_scale(root_pitch=17, num_octaves=8)
        if len(scale) == 0:
            self.fail("build_minor_scale not yet implemented")
            return
        self.help_check_scale(scale, root_pitch=17, intervals=intervals, num_octaves=8)

    def test_4_add_note_multiple(self):
        # TODO this is 2 test cases 
        scale = build_major_scale(root_pitch=30, num_octaves=3)
        dur = bpm_to_beat_len(240)
        segment = AudioSegment.silent(dur*len(scale))
        segment.export(PREFIX + "/generated/test_4_add_note_multiple.wav", format = "wav")
        for i in range(len(scale)):
            if i%2 == 0:
                add_piano_note(segment, scale[i], i*dur, dur*2)
        if len(segment) == 0:
            self.fail("scale_to_playable_melody not yet implemented")
            return
        self.assertTrue(len(segment) == len(scale)*dur, 
                        f"the playable melody should be same length as test_4_add_note_multiple.wav, expected {len(scale)*dur}, got {len(segment)}")
        
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_4_add_note_multiple.wav")
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_4_add_note_multiple.wav to debug.")
    def test_4_add_note_multiple_long(self):  
        mary = [(52, 0, 500), (50, 500, 500), (48, 1000, 500), (50, 1500, 500), 
                (52, 2000, 500), (52, 2500, 500), (52, 3000, 1000), 
                (50, 4000, 500), (50, 4500, 500), (50, 5000, 1000), 
                (52, 6000, 500), (55, 6500, 500), (55, 7000, 1000)]
        dur = bpm_to_beat_len(120)
        segment = AudioSegment.silent(dur*len(mary))
        for pitch, start, b in mary:
            segment = add_piano_note(segment, pitch, start, b)
        segment.export(PREFIX + "/generated/test_4_add_note_multiple_long.wav", format = "wav")
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_4_add_note_multiple_long.wav")
        self.assertTrue(len(segment) == len(expected), 
                        f"the melody should be same length as test_4_add_note_multiple_long.wav, expected {len(expected)}, got {len(segment)}")
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_4_add_note_multiple_long.wav to debug.")
        
    def test_4_add_single_note_to_empty_piano(self): 
        # add a single note to empty, piano 
        empty_segment = AudioSegment.empty()
        segment = add_piano_note(empty_segment, 48, 0, 1000)
        segment.export(PREFIX + '/generated/test_4_add_single_note_to_empty_piano.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + '/Audio/test_4_add_single_note_to_empty_piano.wav')
        self.assertTrue(len(segment) == len(expected), 
                        f"the melody should be same length as test_4_add_single_note_to_empty_piano.wav, expected {len(expected)}, got {len(segment)}")
        self.assertTrue(expected == segment, 
                        "Generated audio does not match the expected. Compare your generated sample to test_4_add_single_note_to_empty_piano.wav to debug.")

    def test_4_add_single_note_to_empty_perc(self): 
        # add a single note to empty, piano 
        empty_segment = AudioSegment.empty()
        segment = add_perc_note(empty_segment, "snare", 0)
        segment.export(PREFIX + '/generated/test_4_add_single_note_to_empty_perc.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + '/Audio/test_4_add_single_note_to_empty_perc.wav')
        self.assertTrue(len(segment) == len(expected), 
                        f"the melody should be same length as test_4_add_single_note_to_empty_perc.wav, expected {len(expected)}, got {len(segment)}")
        self.assertTrue(expected == segment, 
                        "Generated audio does not match the expected. Compare your generated sample to test_4_add_single_note_to_empty_perc.wav to debug.")

    def test_4_add_one_note_after_one_note(self):
        # one note segment, add another note right after it 
        empty_segment = AudioSegment.empty() 
        one_note_segment = add_piano_note(empty_segment, 48, 0, 1000)
        segment = add_piano_note(one_note_segment, 50, 1000, 1000)
        segment.export(PREFIX + '/generated/test_4_add_note_after_one_note.wav', format = 'wav')     
        expected = AudioSegment.from_wav(PREFIX + '/Audio/test_4_add_note_after_one_note.wav')
        self.assertTrue(len(segment) == len(expected), 
                        f"the melody should be same length as test_4_add_note_after_one_note.wav, expected {len(expected)}, got {len(segment)}")
        self.assertTrue(expected == segment, 
                        "Generated audio does not match the expected. Compare your generated sample to test_4_add_note_after_one_note.wav to debug.")

    def test_4_add_one_note_in_middle(self):
        # add a note in the middle 
        empty_segment = AudioSegment.empty() 
        segment = add_piano_note(empty_segment, 48, 0, 1000)
        segment = add_piano_note(segment, 50, 1000, 1000)
        segment = add_piano_note(segment, 52, 2000, 1000)
        segment = add_perc_note(segment, "snare", 1000)
        segment.export(PREFIX + '/generated/test_4_add_one_note_in_middle.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + '/Audio/test_4_add_one_note_in_middle.wav')
        self.assertTrue(len(segment) == len(expected), 
                        f"the melody should be same length as test_4_add_one_note_in_middle.wav, expected {len(expected)}, got {len(segment)}")
        self.assertTrue(expected == segment, 
                        "Generated audio does not match the expected. Compare your generated sample to test_4_add_one_note_in_middle.wav to debug.")

    def test_4_add_note_two_notes_simultaneous(self):
        segment = AudioSegment.empty() 
        segment = add_piano_note(segment, 24, 0, 2000) 
        segment = add_piano_note(segment, 68, 1000, 500)
        segment.export(PREFIX + "/generated/test_4_add_note_two_notes_simultaneous.wav", format = "wav")
        expected = AudioSegment.from_wav(PREFIX + '/Audio/test_4_add_note_two_notes_simultaneous.wav')
        self.assertTrue(len(segment) == len(expected), 
                        f"the melody should be same length as test_4_add_note_two_notes_simultaneous.wav, expected {len(expected)}, got {len(segment)}")
        self.assertTrue(expected == segment, 
                        "Generated audio does not match the expected. Compare your generated sample to test_4_add_note_two_notes_simultaneous.wav to debug.")
        
    def test_5_scale_to_segment_major(self):
        dur = bpm_to_beat_len(120)
        scale = build_major_scale(root_pitch=24, num_octaves=4)
        segment = scale_to_segment(scale)
        segment.export(PREFIX + "/generated/test_5_scale_to_segment_major.wav", format = "wav")
        if len(segment) == 0:
            self.fail("scale_to_playable_melody not yet implemented")
            return
        self.assertTrue(len(segment) == len(scale)*dur, 
                        f"the playable melody should be same length as scale*duration, expected {len(scale)*dur}, got {len(segment)}")
        
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_5_scale_to_segment_major.wav")
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_5_scale_to_segment_major.wav to debug.")
        
    def test_5_scale_to_segment_minor(self):
        dur = bpm_to_beat_len(120)
        scale = build_minor_scale(root_pitch=51, num_octaves=2)
        segment = scale_to_segment(scale)
        segment.export(PREFIX + "/generated/test_5_scale_to_segment_minor.wav", format = "wav")
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_5_scale_to_segment_minor.wav")
        self.assertTrue(len(segment) == len(scale)*dur, 
                        f"the playable melody should be same length as scale*dur, expected {len(scale)*dur}, got {len(segment)}")
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_5_scale_to_segment_minor.wav to debug.")
        
    def test_6_note_starts_not_sorted(self):
        notes = [(50,1000, 1000), (48, 0, 1000) ]
        segment = melody_to_segment(notes)
        segment.export(PREFIX + '/generated/test_6_note_starts_not_sorted.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + '/Audio/test_6_note_starts_not_sorted.wav')
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_6_note_starts_not_sorted.wav, expected {len(expected)}, got {len(segment)}")
        
        self.assertTrue(expected == segment,
                        "Generated audio does not match the expected. Compare your generated samples to test_6_note_starts_not_sorted.wav to debug.")
        

    def test_6_melody_to_segment_mary_lamb(self):
        mary = [(52, 0, 500), (50, 500, 500), (48, 1000, 500), (50, 1500, 500), 
        (52, 2000, 500), (52, 2500, 500), (52, 3000, 1000), (50, 4000, 500), 
        (50, 4500, 500), (50, 5000, 1000), (52, 6000, 500), (55, 6500, 500), 
        (55, 7000, 1000)]

        segment = melody_to_segment(mary)
        segment.export(PREFIX + '/generated/test_6_melody_to_segment_mary_lamb.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_6_melody_to_segment_mary_lamb.wav")
        if len(segment) == 0:
            self.fail("melody_to_segment not yet implemented")
            return
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_6_melody_to_segment_mary_lamb.wav, expected {len(expected)}, got {len(segment)}")
        
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_6_melody_to_segment_mary_lamb.wav to debug.")
        
    def test_6_melody_to_segment_one_note(self):
        mel2 = [(52, 3000, 1000)]
        segment = melody_to_segment(mel2)
        segment.export(PREFIX + '/generated/test_6_melody_to_segment_one_note.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_6_melody_to_segment_one_note.wav")
        if len(segment) == 0:
            self.fail("melody_to_segment not yet implemented")
            return
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_6_melody_to_segment_one_note.wav, expected {len(expected)}, got {len(segment)}")
        
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_6_melody_to_segment_one_note.wav to debug.")

    def test_7_short(self):
        drumline = [("cymbal_crash", 0), ("tom_floor", 2), ("hihat", 3)]
        segment = drumline_to_segment(drumline)
        segment.export(PREFIX + "/generated/test_7_short.wav", format = "wav")
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_7_short.wav")
        if len(segment) == 0:
            self.fail("drumline_to_segment not yet implemented")
            return
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_7_short.wav, expected {len(expected)}, got {len(segment)}")
        
        
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_7_short.wav to debug.")

    def test_7_drumline_to_segment(self):
        drum = [('hihat', 0), ('kick', 0), ('hihat', 2), ('kick', 3), 
                ('hihat', 4), ('snare', 4), ('hihat', 4), 
                ('kick', 4), ('hihat', 7), ('kick', 7), 
                ('hihat', 9), ('hihat', 10), ('snare', 10),
                ('hihat', 11), ('kick', 11), ('hihat', 12)]

        segment = drumline_to_segment(drum)
        segment.export(PREFIX + '/generated/test_7_drumline_to_segment.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_7_drumline_to_segment.wav")
        if len(segment) == 0:
            self.fail("drumline_to_segment not yet implemented")
            return
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_7_drumline_to_segment.wav, expected {len(expected)}, got {len(segment)}")
        
        
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_7_drumline_to_segment.wav to debug.")

    
    def test_7_note_starts_not_sorted(self):
        drumline = [("snare", 1), ("kick", 0)]
        segment = drumline_to_segment(drumline)
        segment.export(PREFIX + '/generated/test_7_note_starts_not_sorted.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + '/Audio/test_7_note_starts_not_sorted.wav')
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_7_note_starts_not_sorted.wav, expected {len(expected)}, got {len(segment)}")
        
        
        self.assertTrue(expected == segment,
                        "Generated audio does not match the expected. Compare your generated samples to test_7_note_starts_not_sorted.wav to debug.")
    
  
    def test_8_add_drumline_one_note_song(self):
        song = [(48, 0, 500)]
        segment = add_drumline_to_song(48, 2, 48, 2, song, bpm=120)
        segment.export(PREFIX + '/generated/test_8_one_note_song.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_8_one_note_song.wav")
        
        if len(segment) == 0:
            self.fail("add_drumline_to_song not yet implemented")
            return 
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_8_one_note_song.wav, expected {len(expected)}, got {len(segment)}")
        
        
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_8_one_note_song.wav to debug.")

    
    def test_8_add_drumline_non_default_bpm(self):
        song = [(48, 0, 500)]
        segment = add_drumline_to_song(48, 1, 48, 1, song, bpm=200)
        segment.export(PREFIX + '/generated/test_8_non_default_bpm.wav', format = 'wav')
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_8_non_default_bpm.wav")
        
        if len(segment) == 0:
            self.fail("add_drumline_to_song not yet implemented")
            return 
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_8_non_default_bpm.wav, expected {len(expected)}, got {len(segment)}")
        
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_8_non_default_bpm.wav to debug.")

    
    
    def test_8_add_drumline_to_song(self):
        mary = [(52, 0, 500), (50, 500, 500), (48, 1000, 500), (50, 1500, 500), 
        (52, 2000, 500), (52, 2500, 500), (52, 3000, 1000), (50, 4000, 500), 
        (50, 4500, 500), (50, 5000, 1000), (52, 6000, 500), (55, 6500, 500), 
        (55, 7000, 1000)]
        
        segment = add_drumline_to_song(48, 2, 48, 2, mary, bpm=120)
        segment.export(PREFIX + "/generated/test_8_mary_lamb.wav", format = 'wav')
        
        expected = AudioSegment.from_wav(PREFIX + "/Audio/test_8_mary_lamb.wav")
        
        if len(segment) == 0:
            self.fail("add_drumline_to_song not yet implemented")
            return 
        self.assertTrue(len(segment) == len(expected), 
                        f"the length of the output is incorrect, compare to test_8_mary_lamb.wav, expected {len(expected)}, got {len(segment)}")
        
        
        self.assertTrue(expected == segment, 
                "Generated audio does not match the expected. Compare your generated samples to test_8_mary_lamb.wav to debug.")

        

point_values = {
    'test_1_build_scale_1' : 0.01,
    'test_1_build_scale_2' : 0.01,
    'test_1_build_scale_3' : 0.01,
    'test_1_build_scale_4' : 0.01,
    'test_1_build_scale_5' : 0.01,
    'test_2_build_major_scale_1' : 0.01,
    'test_2_build_major_scale_2' : 0.01,
    'test_2_build_major_scale_3' : 0.01,
    'test_3_build_minor_scale_1' : 0.01,
    'test_3_build_minor_scale_2' : 0.01,
    'test_3_build_minor_scale_3' : 0.01,
    'test_4_add_note_multiple' : 0.03,
    'test_4_add_note_multiple_long' : 0.03,
    'test_4_add_single_note_to_empty_piano' : 0.03,
    'test_4_add_single_note_to_empty_perc' : 0.03,
    'test_4_add_one_note_after_one_note' :0.04,
    'test_4_add_one_note_in_middle' : 0.04,
    'test_4_add_note_two_notes_simultaneous' : 0.04,
    'test_5_scale_to_segment_major' : 0.1,
    'test_5_scale_to_segment_minor' : 0.1,
    'test_6_melody_to_segment_mary_lamb' : 0.05,
    'test_6_melody_to_segment_one_note' : 0.05,
    'test_6_note_starts_not_sorted' : 0.05,
    'test_7_short' : 0.05,
    'test_7_drumline_to_segment' : 0.05,
    'test_7_note_starts_not_sorted' : 0.05,
    'test_8_add_drumline_one_note_song': 0.05,
    'test_8_add_drumline_non_default_bpm': 0.05,
    'test_8_add_drumline_to_song' : 0.05
}


class Results_600(unittest.TextTestResult):
    # We override the init method so that the Result object
    # can store the score and appropriate test output.
    def __init__(self, *args, **kwargs):
        super(Results_600, self).__init__(*args, **kwargs)
        self.output = []
        self.points = sum(point_values.values())
        self.total_points = sum(point_values.values())

    def addFailure(self, test, err):
        test_name = test._testMethodName
        msg = str(err[1])
        self.handleDeduction(test_name, msg)
        super(Results_600, self).addFailure(test, err)

    def addError(self, test, err):
        test_name = test._testMethodName
        msg = 'Your code produced an error on test %s: %s' % (test_name, str(err[1]))
        self.handleDeduction(test_name, msg)
        super(Results_600, self).addError(test, err)

    def handleDeduction(self, test_name, message):
        point_value = point_values[test_name]
        self.output.append('[-%s]: %s' % (point_value, message))
        self.points -= point_value

    def getOutput(self):
        if len(self.output) == 0:
            return "All correct!"
        return '\n'.join(self.output)

    def getPoints(self):
        return round(self.points, 2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPS5))
    result = unittest.TextTestRunner(verbosity=2, resultclass=Results_600).run(suite)

    output = result.getOutput()
    points = result.getPoints()

    print("\n\nProblem Set 5 Unit Test Results:")
    print(output)
    print("Points: {points}/{total_points}".format(points=points, total_points=result.total_points))
