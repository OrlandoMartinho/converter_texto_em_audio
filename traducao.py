from googletrans import Translator, LANGUAGES
import main
from gtts import gTTS
import os

def traduzir_frase(frase, idioma):
    
    existencia= [False,False]
    
        
    if idioma in main.controller.codigos_idiomas():
            
         existencia[0]=True
            
        
    if idioma in main.controller.idiomas_correspondentes():
            
            existencia[1]=True
            
    if existencia[1]==True :
        
       i=0    
       while i<len(main.controller.idiomas_correspondentes()):
           
           if idioma == main.controller.idiomas_correspondentes()[i]:
               
               idioma=main.controller.codigos_idiomas()[i].lower()
               
           i=i+1

    if True in existencia:
        
        translator = Translator()

        try:
            traducao = translator.translate(frase, src='auto', dest=idioma)
            return traducao.text
        except Exception as e:
            return f"Erro ao traduzir: {e}"
    else:
        
        return "Idioma inválido"



def texto_para_audio(texto, idioma):
    
    
    existencia= [False,False]
    
        
    if idioma in main.controller.codigos_idiomas():
            
         existencia[0]=True
            
        
    if idioma in main.controller.idiomas_correspondentes():
            
            existencia[1]=True
            
    if existencia[1]==True :
        
       i=0    
       while i<len(main.controller.idiomas_correspondentes()):
           
           if idioma == main.controller.idiomas_correspondentes()[i]:
               
               idioma=main.controller.codigos_idiomas()[i].lower()
               
           i=i+1

    if True in existencia:
        
        texto2 =str(traduzir_frase(texto, idioma))
         

        try:
          tts = gTTS(text=texto2, lang=idioma, slow=False)
          tts.save(main.controller.temp_dir()+"output.mp3")
          return idioma
        except Exception as e:
            return f"Erro ao traduzir: {e}"
    else:
        return "Idioma inválido"
    
    
    
   

