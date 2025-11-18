from flask import Flask, request
from whisper_decode import decode
from grok_inference import infer
from zk_proof import prove
from ssh_executor import execute
from blockchain_fork import fork

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    audio = request.data
    text = decode(audio)
    result = infer(text)
    proof = prove(result)
    execute(text, proof)
    fork(text, result, proof)
    return {"status":"logged","proof":proof.hex()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
