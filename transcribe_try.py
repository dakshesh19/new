gcs_uri ='gs://ags_2021/2286220210929142155867(2).wav'
from google.cloud import speech
x = open("trancribe_2" , "w")
client = speech.SpeechClient()
audio = speech.RecognitionAudio(uri=gcs_uri)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code="en-US",
    use_enhanced=True,
    model="phone_call",
)
operation = client.long_running_recognize(config=config, audio=audio)
print("Waiting for operation to complete...")
response = operation.result(timeout=1000)
for result in response.results:
    x.write(u"Transcript: {}\n".format(result.alternatives[0].transcript))
x.close()