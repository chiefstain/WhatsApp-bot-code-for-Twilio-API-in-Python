# Import required libraries
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route to handle incoming messages from Twilio
@app.route('/whatsapp', methods=['POST'])
def handle_incoming_messages():
    # Parse the incoming message
    incoming_message = request.values.get('Body', '').lower()
    
    # Determine how to respond based on the content of the message
    if incoming_message == 'hello':
        response_text = 'Hi there!'
    elif incoming_message == 'how are you?':
        response_text = 'I am doing well, thank you. How about you?'
    else:
        response_text = 'Sorry, I don\'t understand that command.'
    
    # Construct a Twilio MessagingResponse object with the response text
    twilio_response = MessagingResponse()
    twilio_response.message(response_text)
    
    # Return the Twilio response as a string
    return str(twilio_response)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
