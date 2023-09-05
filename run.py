from app import app

# run this command to generate a self-signed ssl certificate
# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

if __name__ == '__main__':
    # app.run(host="0.0.0.0", ssl_context=('cert.pem', 'key.pem'))
    app.run(host="0.0.0.0")