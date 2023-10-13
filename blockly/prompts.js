const prompt_transcribe = `You are to pass the audio transcription
to the next chain. Do not alter the transcription in any way.

Transcription: {text}`

const prompt_block_generator = `Consider you are an unmanned aerial vehicle. Your goal is to determine
what commands to execute. You are equipped with functions such as goto("location"), takeoff(), land(),
and takepicture("object"). Output JavaScript code that executes the commands.

For example, if the command is "GOTO Whole Foods and LAND", your output should be:

takeoff();
goto("Whole Foods");
land();
`

