from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == 'Erdi1837.':
            return request.args.get('hub.challenge')
        return 'Invalid token', 403
    return 'OK', 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
