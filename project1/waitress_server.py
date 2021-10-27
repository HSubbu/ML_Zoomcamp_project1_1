from waitress import serve
import predict
try:
    print("LOADING THE WEB SERVICE ON WAITRESS...")
    serve(predict.app, host='0.0.0.0', port=9696)
except:
    print("An exception occurred")
