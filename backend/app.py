from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
import os

class RequisicaoTexto(BaseModel):
    texto: str
    opcao: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def verificar_status():
    return {"status": "Servidor rodando com sucesso"}

@app.post("/processar")
def processar_conteudo(dados: RequisicaoTexto):
    chave_api = os.getenv("GEMINI_API_KEY")
    
    if not chave_api:
        raise HTTPException(status_code=500, detail="Chave API nao configurada no servidor")
        
    try:
        cliente = genai.Client(api_key=chave_api)
        
        prompt_sistema = "Voce e um assistente especialista em sintese de conteudo."
        
        if dados.opcao == "resumo":
            prompt_usuario = f"Faca um resumo profissional, claro e direto do seguinte texto:\n\n{dados.texto}"
        elif dados.opcao == "bullets":
            prompt_usuario = f"Extraia os pontos mais importantes do seguinte texto em formato de lista (bullet points):\n\n{dados.texto}"
        elif dados.opcao == "linkedin":
            prompt_usuario = f"Transforme o seguinte texto em um post engajador para o LinkedIn, usando emojis e hashtags:\n\n{dados.texto}"
        else:
            prompt_usuario = f"Processe o seguinte texto:\n\n{dados.texto}"

        resposta = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt_usuario,
            config={"system_instruction": prompt_sistema}
        )
        
        return {"resultado": resposta.text}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))