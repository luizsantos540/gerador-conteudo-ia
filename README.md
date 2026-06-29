# Gerador de Conteúdo Inteligente com IA

Uma aplicação Full Stack que utiliza a API do Google Gemini para processar textos e gerar conteúdos customizados, atendendo tanto o ambiente corporativo quanto o educacional e acadêmico.

## 🚀 Funcionalidades

- **Escopo Educacional:**
  - **Trabalho Escolar:** Estrutura textos nos blocos formais de Introdução, Desenvolvimento e Conclusão.
  - **Resumo de Livro:** Cria resumos críticos detalhados no estilo de fichamento analítico.
  - **Estrutura de Redação:** Analisa textos e propõe uma estrutura dissertativa-argumentativa no padrão Enem/Vestibular.

- **Escopo Geral e Profissional:**
  - **Resumo Simples:** Sínteses diretas, claras e objetivas.
  - **Pontos Chave:** Extração dos conceitos principais em formato de tópicos (bullet points).
  - **Post para LinkedIn:** Transforma artigos em publicações engajadoras com uso de emojis e hashtags.

## 🛠️ Tecnologias Utilizadas

- **Front-end:** HTML5, CSS3 (Variáveis nativas e Flexbox) e JavaScript Assíncrono (Fetch API).
- **Back-end:** Python, FastAPI (Framework Web), Pydantic (Validação de dados) e Uvicorn (Servidor ASGI).
- **Inteligência Artificial:** SDK `google-genai` oficial utilizando o modelo `gemini-2.5-flash`.

## 🔧 Como Executar o Projeto

### Prerrequisitos
- Python 3.10 ou superior instalado.
- Uma chave de API do Google Gemini.

### 1. Configuração do Back-end
Navegue até a pasta do servidor, instale as dependências e configure a variável de ambiente:

```bash
# Entrar na pasta
cd backend

# Ativar seu ambiente virtual (exemplo Windows)
.\venv\Scripts\activate

# Instalar pacotes
pip install -r requirements.txt

# Configurar a Chave da API no PowerShell
$env:GEMINI_API_KEY="Sua_Chave_Api"

# Iniciar o servidor
uvicorn app:app --reload
O servidor estará rodando em http://127.0.0.1:8000.

2. Configuração do Front-end
O Front-end foi construído de forma nativa e estática:

Navegue até a pasta frontend/.

Dê dois cliques no arquivo index.html para abri-lo diretamente no seu navegador.

Cole o texto desejado, selecione a opção e clique em Gerar Conteúdo.