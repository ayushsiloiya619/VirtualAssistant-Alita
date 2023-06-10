<h1>Personal Assistant</h1>

<p>This Python script creates a personal assistant program using the <code>pyttsx3</code>, <code>speech_recognition</code>, <code>datetime</code>, <code>wikipedia</code>, <code>webbrowser</code>, <code>requests</code>, <code>pywhatkit</code>, and <code>pyjokes</code> libraries. The program allows the user to interact with the assistant through voice commands and perform various tasks.</p>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.x</li>
  <li>pyttsx3 library</li>
  <li>speech_recognition library</li>
  <li>wikipedia library</li>
  <li>webbrowser library</li>
  <li>requests library</li>
  <li>pywhatkit library</li>
  <li>pyjokes library</li>
</ul>

<h2>Installation</h2>
<ol>
  <li>Make sure you have Python 3.x installed on your system.</li>
  <li>Install the required libraries by running the following command:</li>
</ol>

<pre><code>pip install pyttsx3 speechrecognition wikipedia requests pywhatkit pyjokes
</code></pre>

<h2>Usage</h2>

<p>1. Import the necessary libraries:</p>

<pre><code>import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests
import pywhatkit
import pyjokes
</code></pre>

<p>2. Initialize the pyttsx3 engine and set the voice:</p>

<pre><code>engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
</code></pre>

<p>3. Define the <code>speak</code> function to speak the given text:</p>

<pre><code>function speak(audio) {
    engine.say(audio);
    engine.runAndWait();
}
</code></pre>

<p>4. Define the <code>wishMe</code> function to greet the user based on the current time:</p>

<pre><code>function wishMe() {
    var hour = new Date().getHours();
    // Greet the user based on the current time
    // ...
}
</code></pre>

<p>5. Define the <code>takeCommand</code> function to listen to the user's voice command and convert it to text:</p>

<pre><code>function takeCommand() {
    var r = sr.Recognizer();
    // Use the microphone as the audio source
    // ...
}
</code></pre>

<p>6. Implement the main logic of the personal assistant:</p>

<pre><code>if (__name__ == "__main__") {
    // Greet the user
    wishMe();

    while (true) {
        // Listen to the user's command
        var query = takeCommand().toLowerCase();
        
        // Process the user's command and perform the corresponding task
        // ...
    }
}
</code></pre>

<p>7. Customize the program by adding more task-specific commands and functionalities based on your requirements. For example:</p>

<ul>
  <li>Searching on Wikipedia</li>
  <li>Opening YouTube, Google, or any other website</li>
  <li>Getting the current time</li>
  <li>Playing a song on YouTube</li>
  <li>Telling jokes</li>
  <li>Providing weather information</li>
  <li>Responding to user's gratitude or compliments</li>
  <li>Displaying personal information</li>
  <li>and more...</li>
</ul>

<p>8. Run the script and start interacting with your personal assistant!</p><br>
<b><p>Latest Release</p></b>
<p>ChatGPT: </P>
                engine="davinci-codex",
                prompt=prompt,
                temperature=0.5,
                max_tokens=200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
</p><br>
<h2>Note</h2>
<ul>
  <li>Make sure you have an active internet connection for tasks such as searching on Wikipedia, playing songs on YouTube, and getting weather information.</li>
  <li>Modify the program to include your own API keys or customize it to fit your needs.</li>
</ul>

<p>Enjoy using your personal assistant!</p>
