from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    return {
        "mensagem": "Dados recebidos no backend",
        "tamanho_texto": len(dados.texto),
        "opcao_escolhida": dados.opcao
    }