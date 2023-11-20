from controller import controller
from flask import Flask, request,jsonify
from flask_cors import CORS
import traducao


servidor = Flask(__name__)

CORS(servidor)
 
   
@servidor.route('/converter_texto_para_audio', methods=['POST'])

def converter_mensagem():
    
    dados = request.json
    frase =str(dados.get('frase'))
    idioma =str(dados.get('idioma'))    
    
    return  jsonify({
          "resultado":traducao.texto_para_audio(frase,idioma.lower())
        }), 200    
  
  

if __name__ == '__main__':
    servidor.run(debug=True)
    