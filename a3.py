from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io

def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech_v1.SpeechClient.from_service_account_json('PrestiSolutions-fb3de2002b43.json')

    # local_file_path = 'resources/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = "en-IN"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 16000

    # When enabled, the first result returned by the API will include a list
    # of words and the start and end time offsets (timestamps) for those words.
    enable_word_time_offsets = True

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC

    #Profanity Check
    prof_check = True
    config = {
        "profanity_filter": prof_check,
        "enable_word_time_offsets": enable_word_time_offsets,
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "use_enhanced": True,

    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
        for word in alternative.words:
            print(u"Word: {}".format(word.word))
            print(
                u"Start time: {} seconds {} nanos".format(
                    word.start_time.seconds, word.start_time.nanos
                )
            )
            print(
                u"End time: {} seconds {} nanos".format(
                    word.end_time.seconds, word.end_time.nanos
                )
            )


sample_recognize('xyz.flac')
