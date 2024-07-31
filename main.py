"""
from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/explore_nairobi', methods=['POST'])
def explore_nairobi():
    session_id = request.form.get('sessionId')
    is_active = request.form.get('isActive')
    digit_pressed = request.form.get('dtmfDigits')
    caller_number = request.form.get('callerNumber')
    response = '<?xml version="1.0" encoding="UTF-8"?>'
    response += '<Response>'
    if is_active == '1':
        if digit_pressed:
            response += handle_response(digit_pressed)
        else:
            text = "Hey there, are you ready to explore Nairobi County? Press 1 to take a look at tourist destinations, press 2 to experience Nairobi street food, and press 3 to experience our unique matatu culture."
            response += '<GetDigits timeout="08" finishOnKey="#">'
            response += f'<Say>{text}</Say>'
            response += '</GetDigits>'
    else:
        # Handle the end of the call details
        duration = request.form.get('durationInSeconds')
        currency_code = request.form.get('currencyCode')
        amount = request.form.get('amount')
        # Log call details if necessary
        # No need to return a response if the call is not active
        return ''
    response += '</Response>'
    # Return the response to Africa's Talking
    return Response(response, mimetype='text/xml')

def handle_response(digit_pressed):
    if digit_pressed == '1':
        text = "We recommend you take a look at these locations. You can view Nairobi from the top of KICC for 200 bob, learn our local history at the National Archives for only 50 bob, or perhaps you would like something with more adventure, visit Giraffe Centre off Lang'ata Road and pet a giraffe for only 1000 bob."
        return f'<Say>{text}</Say>'
    elif digit_pressed == '2':
        return '<Say>Nairobi street food, You can enjoy a vast selection on our streets, from as low as 50 shillings, you can enjoy mahamri, kaimati, mbaazi, chapati and much more. We recomend you try out narobi street kitchen on General Mathenge road or you can try Klabu 36 on mamlaka road for authentic nairobi foods.</Say>'
    elif digit_pressed == '3':
        return '<Say>Nairobi matatu culture is famous world over, with only 100 shillings grab a matatu to Rongai, Ngong, Kasarani and or Thika. Let the Music fill your soul, from urbantone to Gengetone nairobi music will serenade you .</Say>'
    else:
        return '<Say>You have pressed an invalid key.</Say>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
"""


from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/explore_nairobi', methods=['POST'])
def explore_nairobi():
    session_id = request.form.get('sessionId')
    is_active = request.form.get('isActive')
    digit_pressed = request.form.get('dtmfDigits')
    caller_number = request.form.get('callerNumber')
    response = '<?xml version="1.0" encoding="UTF-8"?>'
    response += '<Response>'
    if is_active == '1':
        if digit_pressed:
            response += handle_response(digit_pressed)
        else:
            text = "Mambo Vipi? Karibu Sana Nairobi, Hili jiji wakaribishwa kwa mikono miwili. Tafadhali Mimi kama mwana ramani wako nakuomba ufanye hivi. Bonyeza moja kuona pa kutalii Nai, Mbili ili ujue street food culture yetu na pia tatu ili kuelewa matwana culture yetu kupitia mat za Ronga."
            response += '<GetDigits timeout="08" finishOnKey="#">'
            response += f'<Say>{text}</Say>'
            response += '</GetDigits>'
    else:
        # Handle the end of the call details
        duration = request.form.get('durationInSeconds')
        currency_code = request.form.get('currencyCode')
        amount = request.form.get('amount')
        # Log call details if necessary
        # No need to return a response if the call is not active
        return ''
    response += '</Response>'
    # Return the response to Africa's Talking
    return Response(response, mimetype='text/xml')

def handle_response(digit_pressed):
    if digit_pressed == '1':
        text = "We recommend you take a look at these locations. You can view Nairobi from the top of KICC for 200 bob, learn our local history at the National Archives for only 50 bob, or perhaps you would like something with more adventure, visit Giraffe Centre off Lang'ata Road and pet a giraffe for only 1000 bob."
        return f'<Say>{text}</Say>'
    elif digit_pressed == '2':
        return '<Say>Nairobi street food, You can enjoy a vast selection on our streets, from as low as 50 shillings, you can enjoy mahamri, kaimati, mbaazi, chapati and much more. We recomend you try out narobi street kitchen on General Mathenge road or you can try Klabu 36 on mamlaka road for authentic nairobi foods.</Say>'
    elif digit_pressed == '3':
        return '<Say>Nairobi matatu culture is famous world over, with only 100 shillings grab a matatu to Rongai, Ngong, Kasarani and or Thika. Let the Music fill your soul, from urbantone to Gengetone nairobi music will serenade you .</Say>'
    else:
        return '<Say>You have pressed an invalid key.</Say>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)