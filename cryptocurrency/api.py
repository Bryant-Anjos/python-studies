from ecdsa import SigningKey, NIST384p
from flask import Flask

from Block import *
from Transaction import *
from wallet import *

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bem vindo a nossa criptomoeda'

@app.route('/generateKey')
def generateKey():
    arq = open('key.txt', 'w')
    sk = createSigningKey()
    arq.writelines(str(sk.to_string()))
    arq.close()
    return 'Key gerada e salva com sucesso'

@app.route('/coinbase')
def coinbase():
    return str(COINBASE)

@app.route('/validatingTransactionId', methods=['POST'])
def validanting(id, transaction):
    id = request.form['id']
    transaction = request.form['transaction']
    if id is type(int) and transaction is type(Transaction):
        if validantingTransactionId(id, transaction):
            return 'Transação válida'
        else:
            return 'Transação inválida'
    else:
        return 'Erro'

@app.route('/generateTransaction', methods=['POST'])
def generateTransaction(address, addressFrom, amount, leftover):
    key = open('private.pem', 'r').read()
    res = createTransaction(address, addressFrom, amount, leftover, key)
    transactionPool.append(res)
    return 'Transação adicionada a pool'


if __name__ == '__main__':
    app.run()