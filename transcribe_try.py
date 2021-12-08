gcs_uri ='gs://ags_2021/2286220210823171141710.wav'
from google.cloud import speech
x = open("transcribe_2" , "w")

client = speech.SpeechClient()

audio = speech.RecognitionAudio(uri=gcs_uri)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code="en-US",
)

operation = client.long_running_recognize(config=config, audio=audio)

print("Waiting for operation to complete...")
response = operation.result(timeout=1000)

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    x.write(u"Transcript: {}\n".format(result.alternatives[0].transcript))
x.close()