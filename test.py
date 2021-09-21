from icecream import ic
import abletonparsing
import librosa

def test():
    bpm = 130.
    dir = ""
    filename = "ASD_TEST_1.wav"
    audio_path = dir+filename
    clip_path = audio_path + '.asd'
    audio_data, sr = librosa.load(audio_path, sr=None, mono=False)
    num_samples = audio_data.shape[1]
    clip = abletonparsing.Clip(clip_path, sr, num_samples)
    print_all(clip)
    ic(clip)
    print(clip.start_marker)
    # 5.742306885616792e+72
    print(clip.loop_start)
# .loop_on - ( bool , READ/WRITE ) - Loop toggle is on
# .start_marker - ( float , READ/WRITE ) - Start marker in beats relative to 1.1.1
# .end_marker - ( float , READ/WRITE ) - End marker in beats relative to 1.1.1
# .loop_start - ( float , READ/WRITE ) - Loop start in beats relative to 1.1.1
# .loop_end - ( float , READ/WRITE ) - Loop end in beats relative to 1.1.1
# .hidden_loop_start - ( float , READ/WRITE ) - Hidden loop start in beats relative to 1.1.1
# .hidden_loop_end - ( float , READ/WRITE ) - Hidden loop end in beats relative to 1.1.1
# .warp_markers - ( list[WarpMarker] , READ/WRITE ) - List of warp markers
# .warp_on - ( bool , READ/WRITE ) - Warping is on
# .sr - ( float , READ/WRITE ) - Sample rate of audio data
def print_all(clip: abletonparsing.Clip):
    ic(clip.loop_on)
    ic(clip.start_marker)
    ic(clip.end_marker)
    ic(clip.loop_end)
    ic(clip.hidden_loop_start)
    ic(clip.hidden_loop_end)
    ic(clip.warp_markers)
    ic(clip.warp_on)
    ic(clip.sr)
    # audio_path2 = 'test2.wav'
    # clip_path2 = audio_path2 + '.asd'
    # audio_data2, sr2 = librosa.load(audio_path2, sr=None, mono=False)
    # num_samples2 = audio_data2.shape[1]
    # clip2 = abletonparsing.Clip(clip_path2, sr2, num_samples2)
    # print(clip2.start_marker)
    # # 5.742306885616792e+72
    # print(clip2.loop_start)

test()