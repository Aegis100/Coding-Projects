from pydub import AudioSegment
import random
import math
import numpy as np

"""
    With contributions from Eran Egozy.
"""

# ==============================================
# Part 1: Musical Overview 
#         Familiarize yourself with the functions and data structures in this file,
#         but do not change the contents of this file.
#
#         Compare the note_name_to_midi_pitch and midi_pitch_to_note_name 
#         dictionaries below, the online piano, and example_note_pitch_mapping.png. 
#         You should be able to understand the relationships between them. 
#
#         You do not need to memorize the dictionaries for this assignment.
#
#         Finally, confirm you can play some WAV files in the samples/ directory.
#
#         (No coding)
# ==============================================

# see sample WAV files in samples/ directory. 
# the virtual piano the pset uses has 72 different piano keys (notes/pitches)
MIN_PIANO_PITCH = 24 
MAX_PIANO_PITCH = 96  

# You should not modify this dictionary! 
# for more information, see: https://people.virginia.edu/~pdr4h/pitch-freq.html
# This converts from note name (string) to pitch integer
note_name_to_midi_pitch = {
    # octave 1   
    "C1" : 24,  # notice: B# == C 
    "C#1" : 25,
    "Db1" : 25, # notice: Db == C#
    "D1" : 26,
    "D#1" : 27,
    "Eb1" : 27, # notice: Eb == D#
    "E1" : 28,  # notice: Fb == E   
    "F1" : 29,  # notice: E# == F
    "F#1" : 30, 
    "Gb1" : 30, # notice: Gb == F#
    "G1" : 31,
    "G#1" : 32,  
    "Ab1" : 32, # notice: Ab == G#
    "A1" : 33,  # notice: wraparound back to A after G#
    "A#1" : 34,
    "Bb1" : 34, # notice: Bb == A#
    "B1" : 35,  # notice: Cb == B                       
    # octave 2 (there exists the same structure for each octave)   
    "C2" : 36,
    "C#2" : 37,
    "Db2" : 37,
    "D2" : 38,
    "D#2" : 39,
    "Eb2" : 39,
    "E2" : 40,        
    "F2" : 41, 
    "F#2" : 42, 
    "Gb2" : 42,
    "G2" : 43,
    "G#2" : 44,
    "Ab2" : 44,  
    "A2" : 45, 
    "A#2" : 46,
    "Bb2" : 46,
    "B2" : 47,
    # octave 3 
    "C3" : 48,
    "C#3" : 49,
    "Db3" : 49,
    "D3" : 50,
    "D#3" : 51,
    "Eb3" : 51,
    "E3" : 52,     
    "F3" : 53, 
    "F#3" : 54, 
    "Gb3" : 54,
    "G3" : 55,
    "G#3" : 56,
    "Ab3" : 56,  
    "A3" : 57, 
    "A#3" : 58,
    "Bb3" : 58,
    "B3" : 59,
    # octave 4 
    "C4" : 60,
    "C#4" : 61,
    "Db4" : 61,
    "D4" : 62,
    "D#4" : 63,
    "Eb4" : 63,
    "E4" : 64,     
    "F4" : 65, 
    "F#4" : 66, 
    "Gb4" : 66,
    "G4" : 67,
    "G#4" : 68,
    "Ab4" : 68,  
    "A4" : 69, 
    "A#4" : 70,
    "Bb4" : 70,
    "B4" : 71,
    # octave 5 
    "C5" : 72,
    "C#5" : 73,
    "Db5" : 73,
    "D5" : 74,
    "D#5" : 75,
    "Eb5" : 75,
    "E5" : 76,    
    "F5" : 77, 
    "F#5" : 78, 
    "Gb5" : 78,
    "G5" : 79,
    "G#5" : 80,
    "Ab5" : 80,  
    "A5" : 81, 
    "A#5" : 82,
    "Bb5" : 82,
    "B5" : 83,
    # octave 6
    "C6" : 84,
    "C#6" : 85,
    "Db6" : 85,
    "D6" : 86,
    "D#6" : 87,
    "Eb6" : 87,
    "E6" : 88,  
    "F6" : 89, 
    "F#6" : 90, 
    "Gb6" : 90,
    "G6" : 91,
    "G#6" : 92,
    "Ab6" : 92,  
    "A6" : 93, 
    "A#6" : 94,
    "Bb6" : 94,
    "B6" : 95,
    # octave 7
    "C7" : 96
    # ...
    
    # can repeat up to pitch 127
    # think about where 127 might come from, and why...?
    # hint: binary is base 2
}

# You should not modify this dictionary!
# This is the inverse of the above dictionary to convert from pitch integer to note name (string)
midi_pitch_to_note_name = {
    # octave 1
    24 : "C1",
    25 : "C#1/Db1",
    26 : "D1",
    27 : "D#1/Eb1",
    28 : "E1",
    29 : "F1",
    30 : "F#1/G#1",
    31 : "G1",
    32 : "G#1/Ab1",
    33 : "A1",
    34 : "A#1/Bb1",
    35 : "B1",
    # octave 2
    36 : "C2",
    37 : "C#2/Db2",
    38 : "D2",
    39 : "D#2/Eb2",
    40 : "E2",
    41 : "F2",
    42 : "F#2/Gb2",
    43 : "G2",
    44 : "G#2/Ab2",
    45 : "A2",
    46 : "A#2/Bb2",
    47 : "B2",
    # octave 3
    48 : "C3",
    49 : "C#3/Db3",
    50 : "D3",
    51 : "D#3/Eb3",
    52 : "E3",
    53 : "F3",
    54 : "F#3/Gb3",
    55 : "G3",
    56 : "G#3/Ab3",
    57 : "A3",
    58 : "A#3/Bb3",
    59 : "B3",
    # octave 4
    60 : "C4",
    61 : "C#4/Db4",
    62 : "D4",
    63 : "D#4/Eb4",
    64 : "E4",
    65 : "F4",
    66 : "F#4/Gb4",
    67 : "G4",
    68 : "G#4/Ab4",
    69 : "A4",
    70 : "A#4/Bb4",
    71 : "B4",
    # octave 5
    72 : "C5",
    73 : "C#5/Db5",
    74 : "D5",
    75 : "D#5/Eb5",
    76 : "E5",
    77 : "F5",
    78 : "F#5/Gb5",
    79 : "G5",
    80 : "G#5/Ab5",
    81 : "A5",
    82 : "A#5/Bb5",
    83 : "B5",
    # octave 6
    84 : "C6",
    85 : "C#6/Db6",
    86 : "D6",
    87 : "D#6/Eb6",
    88 : "E6",
    89 : "F6",
    90 : "F#6/Gb6",
    91 : "G6",
    92 : "G#6/Ab6",
    93 : "A6",
    94 : "A#6/Bb6",
    95 : "B6",
    # octave 7
    96 : "C7"
}

# Duration string mappings to beat scaling factors (for length to play a note)
dur_str_to_beatscale = {
    "sixteenth-note" : 0.25,  # very fast
    "eighth-note"    : 0.5,   # faster
    "quarter-note"   : 1,     # on-beat
    "half-note"      : 2,     # slower
    "whole-note"     : 4      # very slow
}

# Please do not modify this list!
# Specifies percussion instrument sample names for the 
# instrument hits encoded in the y axis of encodings (numpy arrays are (y, x))
y_axis_perc_instr= [
    "cymbal_crash",
    "tom_small",
    "tom_medium",
    "tom_floor",
    "hihat",
    "snare",
    "kick"
]



# You do not need to modify this function!
def print_scale(label, scale, max_cols=80):
    """
    Prints a scale (list of pitch integers) and their corresponding 
    note name strings.
    
    Adjust max_cols to change print width formatting.
    
    Parameters
    ----------
    label: string
        an identifier to print to stdout (such as "C3 major" or "G#4 minor"),
        followed by the scale pitch integers pretty printed
    scale : list of integers 
        contains pitches that are available in the scale
    max_cols: list of integers
        max width of printing output per line, changes width of printed scales
        
    Returns
    -------
    nothing
    """
    print("\n")
    print("scale %s (pitch, note name)" % label)
    pos = 0
    for i in range(len(scale)):
        pitch = scale[i]
        tuple_str_len = 5 + 10 # below string (static length + dynamic length)
        pos += tuple_str_len
        if pos > max_cols:
            print("\n")
            pos = tuple_str_len
        print("(%3d, %-7s )" % (pitch, midi_pitch_to_note_name[pitch]), end='')
    print("\n")
    


# You only need to understand this function's parameters and interface.
# Please do not modify this function!
def segment_to_wav(s, wav_filepath):
    """
    Save a PyDub AudioSegment as a WAV file to the specified filepath in the filesystem.
    Will produce errors if the given path to the output does not exist, or 
    is not accessable.
    
    Parameters
    ----------
    s : PyDub AudioSegment
        A created AudioSegment that contains audible audio contents.
    wav_filename : string (filesystem path to output file)
        A string representing the filesystem path to the desired output file.

    Returns
    -------
    None.

    """
    print(f'generated: {wav_filepath}')
    s.export(wav_filepath, format='wav')
    
# You only need to understand this function's parameters and interface.
# Please do not modify this function!
def bpm_to_beat_len(bpm):
    """
    Convert BPM (Beats Per Minute) to a length of time in milliseconds representing one beat

    Parameters
    ----------
    bpm : integer
        The beats per minute to convert

    Returns
    -------
    float
        An amount of miliseconds that represent one beat.
    """
    return 1000 / (bpm / 60)




#######################################################
#OPTIONAL EXPERIMENTAL MUSIC TRACKS
#######################################################

def rand_abstract_melody(min_rand_index, max_rand_index, num_beats, bpm=120):
    """
    Generate a random abstract melody by performing a simple "random walk,"
    over scale indexes specified by the incoming range, paired with position and
    random duration integers, to return a new list of scale index tuples. 
    Scale index tuples are each of type (scale index, position, duration).
    
    First, add a scale index tuple of (0, "quarter-note") to start the abstract 
    melody on the first note of the scale (the opening note). 
    This counts as 1 beat toward num_beats.
    
    Then select a uniformly random starting scale index between 
    [min_rand_index, max_rand_index] (inclusive) as the first random scale index,
    to start the random walk.
    Hint: see random.randint
    
    Then repeatedly choose the next scale index by adding a uniform 
    randomly selected delta from the acceptable_deltas list to the previous scale index. 
    This is a simple "random walk" algorithm.
    
    When applying the random delta to select the next scale index, 
    always bound the new pitch to within 
    [min_rand_index, and max_rand_index] (inclusive) to respect incoming range. 
    
    For all generated tuples with random scale indicies, choose note durations 
    of 1/2 beat ("eighth-note") with 50% chance and 1 beat ("quarter-note") with 50% chance. 
    Hint: see random.choice
    
    If adding a tuple to the generated abstract melody causes the total beats of the 
    generated abstract melody to exceeds num_beats, do not add the generated 
    scale index tuple that caused the melody to exceed num_beats, and stop the generation.
    Hint: a while loop may help
    
    If your generated beat total then ended with less than num_beats, append one more eighth-note
    scale index tuple (representing 0.5 beat) with an acceptable scale index delta 
    to reach exactly num_beats worth of randomly generated scale index tuples,
    including the first opening tuple (1 beat).
    
    Finally, add a final ending scale index tuple to resolve the melody.
    Always end the abstract melody with a final scale index tuple 
    of (7, pos, 4*beat_length) to resolve the melody more pleasantly.
    
    Reminder: do not count the ending scale index tuple duration (4 beats) in reaching
    num_beats; num_beats is the maximum amount of beats to reach by 
    generating the randomly selected durations for the random tuples,
    summed together and added to the first opening tuple (1 beat).
    
    Then return the abstract melody (list of scale index tuples).
    
    Parameters
    ----------
    min_rand_index : integer
        the lowest selectable scale index. Cannot be negative
    max_rand_index : intger
        the highest selectable scale index. Must be >= min_rand_index.
    num_beats : the max number of beats of random scale index tuples to produce
        the total length of the melody will be num_beats + 4 (the final note)

    Returns
    -------
    a random abstract melody (list of scale index tuples) of num_beats worth of beats, 
    plus a final resolving note of 4 beats.
    """
    abstract_melody = []
    beat_dur = bpm_to_beat_len(bpm)
    
    abstract_melody.append((0, 0, beat_dur)) # add first opening note
    total_beats = 1 # count the first opening note as a generated beat
    pos = beat_dur    
    
    acceptable_deltas = (-2, -1, 0, 1, 2) # can be altered per semester to change random walk
    
    # generate up to but not exceeding num_beats worth of scale index tuples
    rand_scale_index = random.randint(min_rand_index, max_rand_index) # pick first random index
    
    while True:
        # pick next random duration
        # distribution can be altered per semester by changing proportion of eighth notes and quarter notes
        rand_beat_amount = random.choice([0.5, 1])
        if total_beats + rand_beat_amount > num_beats: # check generated beat amount
            break
        dur = rand_beat_amount*beat_dur
        abstract_melody.append((rand_scale_index, pos, dur)) # add the random tuple
        pos += dur
        total_beats += rand_beat_amount # update generated beat amount
        # pick next random scale index
        rand_scale_index = rand_scale_index + random.choice(acceptable_deltas)
        # bound within incoming rand range
        if rand_scale_index < min_rand_index:
            rand_scale_index = min_rand_index
        if rand_scale_index > max_rand_index:
            rand_scale_index = max_rand_index
    
    # if generation did not reach exactly num_beats, add an eighth-note to reach exactly num_beats
    if total_beats < num_beats:
        abstract_melody.append((rand_scale_index, pos, 0.5*beat_dur))
        pos += 0.5*beat_dur
        total_beats += 0.5
    
    # add final resolving note    
    abstract_melody.append((7, pos, 4*beat_dur)) 

    return abstract_melody     

def abstract_to_playable_melody(abstract_melody, scale):
    """
    Convert an abstract melody of scale index tuples to a playable melody 
    of note tuples (pitch integer, position integer, duration integer).
    
    Each created note tuple has a pitch index selected from the incoming scale 
    by using the corresponding incoming scale indices in the abstract melody. 
    The incoming positions and durations are left unchanged, and are copied to each new note tuple. 
    
    Then the list of note tuples is returned as a playable melody.

    Parameters
    ----------
    abstract_melody : list of scale index tuples (scale index integer, position integer, duration integer)
        A more abstract melody that encodes locations in a scale to play, and their 
        respective note duration strings.
    scale : list of pitch integers
        A list of pitches that make a scale. 

    Returns
    -------
    playable_melody : list of note tuples (pitch integer, position integer, duration integer)
        A list representing an encoding of a playable melody.
    """
    playable_melody = []
    for i in range(len(abstract_melody)):
        playable_melody.append((scale[abstract_melody[i][0]], abstract_melody[i][1], abstract_melody[i][2]))
    return playable_melody

    