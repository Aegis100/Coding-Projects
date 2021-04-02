### New version of Ps5

from pydub import AudioSegment
import random
import numpy as np
random.seed(23) # do not change or tester will break!

#import music_lib

# from music_lib.py
from music_lib import print_scale
from music_lib import note_name_to_midi_pitch # mapping note strings to midi pitches
from music_lib import midi_pitch_to_note_name # mapping midi pitches to note strings
from music_lib import bpm_to_beat_len         # converting beats per minute to milliseconds
from music_lib import dur_str_to_beatscale    # converting duration strings to scalars
# helpers to create AudioSegments
# helpers to create WAV files
from music_lib import segment_to_wav          # saving created segments to wav files
#Functions to generate random melodies
from music_lib import rand_abstract_melody, abstract_to_playable_melody


# =============================================================================
# Part 1: Building Scales

# Manual testing code is supplied at the bottom of the pset under Part 1.
def build_scale(root_pitch, intervals, num_octaves):
    """
    Creates a scale starting from root_pitch. Each interval in the intervals list 
    specifies the integer distance to the next pitch. The process of adding intervals 
    to the preceding note is repeated num_octave times, to extend the scale's length. 
    The notes in the scale are either monotonically increasing or monotonically decreasing.
    
    For example, a call with
    root_pitch = 48
    intervals = [2, 2, 1, 2, 2, 2, 1] 
    num_octaves = 2 
    
    returns: 
    [C,   D,  E,  F,  G,  A,  B,  C,  D,  E,  F,  G,  A,  B,  C] # this line is for illustration only and should not be returned
    [48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72] # return this 

    Parameters
    ----------
    root_pitch : integer
        the first pitch of the scale (which sets the musical key).
    intervals : list of integers
        a list of integers representing the offset to add to each preceding
        pitch integer to build the scale, first starting with the root_pitch. After
        adding the last interval, the first interval is selected, and the process 
        is repeated to build the next octave in the scale. 
    num_octaves : integer
        applying the intervals from a starting pitch produces one octave of a scale.
        applying the intervals again from the end of that scale produces the next octave.
        The process can be repeated to generate num_octaves octaves.
        num_octaves determines the scale's length.
    Returns
    -------
    list of pitch integers representing a scale, defined by the given root_pitch 
    and the intervals
    """
    pitch_list = [root_pitch]
    for octave_num in range(num_octaves):
        for interval in intervals:
            pitch_list.append(pitch_list[-1] + interval)
    return pitch_list


  
# Manual testing code is supplied at the bottom of the pset under Part 1.
def build_major_scale(root_pitch, num_octaves=1):
    """
    Build a Major scale starting from a root_pitch (which sets the musical key).
    Add the intervals for a standard Major scale in a call to build_scale.
    Make sure to pass through num_octaves to generate the proper length scale.

    Parameters
    ----------
    root_pitch : integer
        the first pitch integer that represents the root pitch of the scale
    num_octaves: integer
        the number of octaves (repetitions of added intervals) to include in the 
        built scale. determines the scale's length

    Returns
    -------
    scale : list of (pitch) integers 
        represents a Major scale, ranging from root_pitch followed
        by num_octaves worth of octaves. root_pitch is the first note of the first
        octave.
    """
    scale_list = build_scale(root_pitch, [2, 2, 1, 2, 2, 2, 1], num_octaves)
    return scale_list


# Manual testing code is supplied at the bottom of the pset under Part 1.
def build_minor_scale(root_pitch, num_octaves=1):
    """
    Build a Minor scale starting from a root_pitch (which sets the musical key).
    Add the intervals for a standard Minor scale in a call to build_scale.
    Make sure to pass through num_octaves to generate the proper length scale.

    Parameters
    ----------
    root_pitch : integer
        the first pitch integer that represents the root pitch of the scale

    Returns
    -------
    scale : list of (pitch) integers 
        represents a Minor scale, ranging from root_pitch followed
        by num_octaves worth of octaves. root_pitch is the first note of the first
        octave.
    """
    scale_list = build_scale(root_pitch, [2, 1, 2, 2, 1, 2, 2], num_octaves)
    return scale_list

# =============================================================================
# Part 2: Creating Segments

def add_note(seg, name, pos, dur = None):
    """ Add a note sound to a given segment at a particular absolute location in time
    
    To shorten an AudioSegment, read the documentation for the AudioSegment object itself
    https://github.com/jiaaro/pydub/blob/master/API.markdown#audiosegment 
    
    Parameters
    ----------
        seg: the input audio, as a PyDub AudioSegment object.
        name: the filepath name of the '.wav' audio file to add in (e.g. piano note, see add_piano_note below)
        pos: time location of where to place the note (in milliseconds)
        dur (optional): the length of the note to add (in milliseconds). This can shorten the note
    
    Returns
    ----------
        output_segment: PyDub AudioSegment with the note with filename <name> added.
    """
    
    #TODO: load the audio segment specified by the filepath 'name' - see Documentation and add_piano_note below!
    note = AudioSegment.from_file(name, format="wav")
    #TODO: if dur is specified (not None), shorten this audio segment to the correct duration. Otherwise keep full duration.
    # To shorten an AudioSegment, see the documentation for "first 5 seconds of sound1" 
    # at https://github.com/jiaaro/pydub/blob/master/API.markdown#audiosegment
    if dur != None:
        short_note = note[:dur]
    else:
        short_note = note
    #TODO: Add a 100ms fade to the end of the new note
    a_short_note = short_note.fade_out(duration=100)
    #TODO: ensure that input audio segment is long enough for the new note to be overlayed. Lengthen it if not.
    if len(seg) < len(a_short_note):
        duration = len(a_short_note) - len(seg)
        silence = AudioSegment.silent(duration=duration)
        seg1 = seg + silence
    else:
        seg1 = seg
    #TODO:  overlay (ie, mix in) the new note at the correct position.
    if pos >= len(seg1):
        seg2 = seg1 + a_short_note
        return seg2
    elif pos + len(a_short_note) > len(seg1):
        duration = pos + len(a_short_note) - len(seg1)
        seg2 = seg1 + AudioSegment.silent(duration=duration)
        seg2 = seg2.overlay(a_short_note, position=pos)
        return seg2
    else:
        seg2 = seg1.overlay(a_short_note, position=pos)
        return seg2
    
    
    

# We can now use our implementation of add_note to create different instrument notes
# using samples! Below we provide some helper functions for this.
# Do not edit these functions, but observe their implementation

def add_piano_note(seg, pitch, pos, dur):
    return add_note(seg, f'./samples/piano_{pitch}.wav', pos, dur)

def add_perc_note(seg, name, pos):
    return add_note(seg, f'./samples/perc_{name}.wav', pos)

def get_piano_note(pitch):
    filename = f'./samples/piano_{pitch}.wav'
    return AudioSegment.from_file(filename)

def get_drum_note(name):
    filename = f'./samples/perc_{name}.wav'
    return AudioSegment.from_file(filename)


##Now uncomment Part 2 at the bottom for testing


# =============================================================================
# Part 3: Rendering Melodies


#Implement here!
def scale_to_segment(scale, bpm=120):
    """
    Convert a scale, played on a piano, to a PyDub AudioSegment using the helper functions above.
    PyDub AudioSegements can be easily written to WAV files.
    
    You will find bpm_to_beat_len helpful to convert bpm to beat length.

    Parameters
    ----------
    scale : list of pitch integers
        a list of integers representing pitches that create a scale.

    bpm : int, optional
        The desired speed of the music measured in beats per minute (bpm).
        Higher values make faster music. Lower values make slower music.
        The default is 120. Do not change the default value!
    
    Returns
    -------
    output_segment : PyDub AudioSegment containing audio playing the
        incoming scale on a piano with default note durations

    """
    dur = bpm_to_beat_len(bpm) # duration of each scale note (bpm == beats per minute)

    #TODO: Create empty audio segment, and add each note in the scale one by one. Use add_piano_note.
    segment = AudioSegment.empty()
    pos = 0
    for pitch in scale:
        pos += dur
        segment = add_piano_note(segment, pitch, pos, dur)
    return segment

#Implement!
# melody is given as an array of notes, where each note of the tuple: (pitch, start, duration)
def melody_to_segment(notes):
    """
    Convert an entire melody from a list of note tuples to a PyDub AudioSegment (played on piano).
    Create PyDub AudioSegment of correct length
    Overlay each note at the correct position    

    Parameters
    ----------
    notes : list of note tuples (pitch, start, duration)
        A list of tuples representing a sequence of notes to play. start is given in ms.

    Returns
    -------
    output_segment : PyDub AudioSegment containing audio playing the
        desired melody with default note durations on piano.

    """
    # need to figure out the full length of the entire melody by finding the furthest *ending* time:
    
    #TODO:create audio segment of correct full length
    
    #TODO: add each note in the melody at the correct location, with correct duration and 100ms fade. Use helper functions as needed.
    


##Now uncomment Part 3 at the bottom for testing

# Drumline is given as (name, start) tuples
def drumline_to_segment(drumline, bpm = 120):
    """
    Convert a drumline from a list of drum tuples to a PyDub AudioSegment.
    Create PyDub AudioSegment of correct length
    Overlay each drum hit at the correct position    

    Parameters
    ----------
    notes : list of drum tuples (name, start_beat)
        A list of tuples representing a sequence of drums to play. start_beat is given in integer values of beats, starting at 0.

    Returns
    -------
    output_segment : PyDub AudioSegment containing audio playing the
        desired drumline at the given bpm.

    """
    #TODO: calculate duration in milliseconds of each beat (bpm_to_beat_len)
    
    #TODO: Convert start_beat to the corresponding values in time.
    
    #TODO: figure out the full length of the entire melody by finding the furthest *ending* time:
    
    #TODO:create empty audio segment of correct full length
    
    #TODO: add each drum note in at the correct location. Use helper functions as needed.
    #NOTE: WE DO NOT WANT A FADE ON DRUM NOTES. Does this affect which helper functions we can use?
    
    pass

# =============================================================================
# Part 4: Adding Drums to Melodies!

def add_drumline_to_song(root_pitch_major, num_octaves_major, root_pitch_minor, num_octaves_minor, melody_notes, bpm=120):
    """
    Return an AudioSegment in which 
    First a major scale is played. This major scale starts on root pitch root_pitch_major and has num_octaves_major number of octaves. 
    Second a minor scale is played. This minor scale starts on root pitch root_pitch_minor and has num_octaves_minor number of octaves. 
    Third a melody is played. The melody is produced by converting the notes melody_notes to a segment. 
    You should use the melody_to_segment and drumline_to_segment functions.
    
    A drum line is overlaid on top of the entire AudioSegment containing the major scale followed by the minor scale followed by the melody. 
    In the drum line, a snare is played on odd beats (1, 3, 5, ...), and a kick is played on even beats (0, 2, 4, 6, ...). 
    Remember to make the integer number of drumbeats fit into the length of the segment (hint: use // when calculating the number of beats)

    Parameters
    ----------
    
    root_pitch_major : int
        Root pitch of the major scale. This major scale will be included in the resulting AudioSegment.  
    num_octaves_major : int
        Number of octaves of the major scale. 
    root_pitch_minor : int
        Root pitch of the minor scale. This minor scale will be included in the resulting AudioSegment. 
        The minor scale is played after the major scale.
    num_octaves_minor : int
        Number of octaves of the minor scale.
    melody_notes : list of note tuples (pitch, start, duration)
        A list of tuples representing a sequence of notes to play. 
        The resulting sequence of notes is played after the minor scale.
    bpm : int, optional
        the desired speed of the music measured in beats per minute (bpm).
        higher values make faster music. Lower values make slower music.
        the default is 120. Do not change the default value!

    Returns
    -------
    AudioSegment

    """
    pass 
    # TODO make major scale and build its AudioSegment  

    # TODO make minor scale and build its AudioSegment
    
    # TODO get AudioSegment of melody_notes (hint: use melody_to_segment)
    
    # TODO append minor scale to major scale. Then append melody to the result. 
    
    # TODO calculate note duration for the input bpm (hint: use bpm_to_beat_len)
    # Sum the durations of the scales and the duration of the melody to get the total duration of the drum line

    # TODO make the drum line, with snare on odd-beats (1, 3, ...) and kick on even-beats (0, 2, 4, ...).
    
    # TODO overlay the drum line AudioSegment on top of the AudioSegment containing the scales and melody
    
    # produce scale segments 
    

##Now uncomment Part 4 at the bottom for testing

# =============================================================================
# =============================================================================



if __name__ == "__main__":
    
    
    #### Part 1 ####################
    #-------------------------------
    intervals = [2, 2, 1, 2, 2, 2, 1] 
    num_octaves = 2 
    C_maj = build_scale(48, intervals, 2)  
    
    #print(C_maj)
    ## Should print [48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72]
    
    #-------------------------------
    #print(build_major_scale(40))
    ## Should print [40, 42, 44, 45, 47, 49, 51, 52]
    
    #-------------------------------
    #print(build_minor_scale(48))
    ## Should print [48, 50, 51, 53, 55, 56, 58, 60]
    
    
    #### Part 2 ###################
    #-------------------------------
    seg = AudioSegment.empty()
    seg = add_note(seg, f'./samples/piano_42.wav', 0, 500)
    seg = add_note(seg, f'./samples/piano_44.wav', 500, 500)
    seg = add_note(seg, f'./samples/piano_46.wav', 1000, 500)
    segment_to_wav(seg, "./generated/add_note_test.wav")
    ## Play the generated file in the /generated folder.
    ## It should sound like 3 ascending notes.

    
    #-------------------------------
    s1 = AudioSegment.empty();
    s1 = add_piano_note(s1, 60, 0, 1000);
    s1 = add_piano_note(s1, 64, 1000, 500);
    s1 = add_piano_note(s1, 67, 2000, 500);
    s1 = add_piano_note(s1, 72, 3000, 1000);
    s1 = add_piano_note(s1, 64, 3000, 1000);
    s1 = add_piano_note(s1, 48, 3000, 1000);
    segment_to_wav(s1, "./generated/add_piano_note_test.wav")
    
    
    #### Part 3 ##################
    #-------------------------------
    C_maj = build_major_scale(42)
    scale_to_segment(C_maj)
    segment_to_wav(seg, "./generated/scale_to_segment_test.wav")
    ## Should sound like a 1 octave C Major scale
    
    #-------------------------------
    #C_maj = build_major_scale(48)
    #beat_dur = bpm_to_beat_len(120)
    #scale_melody = [(C_maj[i], i*beat_dur, beat_dur) for i in range(len(C_maj))]
    #seg = melody_to_segment(scale_melody)
    #segment_to_wav(seg, "./generated/melody_to_segment_test.wav")
    
    ## Should sound identical to the scale_to_segment C Major scale test.
    ## Seems more complicated, but gives us flexibility to build more complex melodies!
    
    #-------------------------------
    ## Try it with the Yankee Doodle melody below!
    #yankee = [(60, 0, 500), (60, 500, 500), (62, 1000, 500), (64, 1500, 500), 
    #          (60, 2000, 500), (64, 2500, 500), (62, 3000, 1000), (60, 4000, 500), 
    #          (60, 4500, 500), (62, 5000, 500), (64, 5500, 500), (60, 6000, 1000), 
    #          (59, 7000, 1000), (60, 8000, 500), (60, 8500, 500), (62, 9000, 500), 
    #          (64, 9500, 500), (65, 10000, 500), (64, 10500, 500), (62, 11000, 500), 
    #          (60, 11500, 500), (59, 12000, 500), (55, 12500, 500), (57, 13000, 500), 
    #          (59, 13500, 500), (60, 14000, 1000), (60, 15000, 1000)]
    #seg = melody_to_segment(yankee)
    #segment_to_wav(seg, "./generated/yankee_doodle.wav")
    
    #-------------------------------
    #drumline = [('snare', 0), ('tom_floor', 0), ('kick', 1), ('snare', 2), ('tom_floor', 2)]
    #seg = drumline_to_segment(drumline)
    #segment_to_wav(seg, "./generated/drumline_to_segment_test.wav")
    
    ## Should sound like a simple snare-bass-snare sequence of 3 drum hits.
    
    
    #### Part 4 ##################
    #-------------------------------
    #melody = [(40, 0, 500), (42, 500, 500), (40, 1000, 500), (42, 1500, 500)]
    #seg = add_drumline_to_song(40, 1, 40, 1, melody, bpm=120):
    #segment_to_wav(seg, "./generated/add_drumline_to_song_test.wav")
    
    ## What do you expect to hear? Does it sound right?
    
    
    #### OPTIONAL: Random Melody Generation ####
    #-------------------------------
    ## Now uncomment the following to generate a random melody, and use the functions you just wrote to play it! To see how to generate 
    ## these melodies, please read the functions in music_lib.py
    
    ## First, we generate a melody as a sequence of indices, that can be used with any 
    ## scale represented as a list. We will call this an 'abstract melody', as it can be
    ## generalised to any scale. We will constrain it to 2 octaves (indexes 0 to 16)
    
    # min_index = 0
    # max_index = 16
    # num_beats = 16
    # abstract_melody = rand_abstract_melody(min_index, max_index, num_beats)
    
    # # Now we will pass in a scale and convert the scale indices to actual pitch integers
    # # that our melody_to_segment function can understand
    
    # C_maj = build_major_scale(48, num_octaves=2)
    # melody = abstract_to_playable_melody(abstract_melody, C_maj)
    # print(melody)
    
    # # Finally, we will use our function to create an audiosegment and save it to a wav file!
    # segment = melody_to_segment(melody)
    # segment_to_wav(segment, "./generated/Random_Melody_C_maj.wav")
    
    
    # # We can also save the exact same melody, but in a different scale!
    # D_min = build_major_scale(50, num_octaves=2)
    # melody = abstract_to_playable_melody(abstract_melody, D_min)
    # print(melody)
    # segment = melody_to_segment(melody)
    # segment_to_wav(segment, "./generated/Random_Melody_D_min.wav")
    pass


