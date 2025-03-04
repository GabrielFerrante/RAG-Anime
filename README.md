# Anime RAG with MyAnimeList API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Um sistema de **Retrieval-Augmented Generation (RAG)** especializado em informações sobre animes, utilizando dados da [MyAnimeList API](https://myanimelist.net/apiconfig/references/api/v2). Ideal para construir Q&A systems, chatbots ou aplicações de recomendação de animes.

## ✨ Funcionalidades

- **Recuperação em tempo real** de dados de animes (títulos, sinopse, episódios, gêneros, etc.)
- Sistema de perguntas e respostas baseado em NLP
- Armazenamento vetorial de informações para recuperação eficiente
- Integração simplificada com a API oficial do MyAnimeList
- Modelo de linguagem ajustável para diferentes casos de uso

🧠 Como Funciona
Extração de Dados: Consulta a MyAnimeList API v2 para obter metadados estruturados

Processamento: Transforma dados em documentos textuais otimizados para NLP

Armazenamento Vetorial: Usa FAISS para criar embeddings de alta dimensão

Geração: Combina retrieval com modelos de linguagem (ex: GPT-2, LLaMA) para respostas contextuais

📚 Documentação
Consulte os principais métodos disponíveis:

fetch_anime_data(anime_id: int)
Recupera dados brutos de um anime específico

query(question: str, top_k: int = 3)
Processa perguntas naturais e retorna respostas contextualizadas

add_custom_source(data: dict)
Permite adicionar fontes de dados adicionais ao sistema

🤝 Contribuição
Contribuições são bem-vindas! Siga estes passos:

Abra uma issue descrevendo sua proposta

Faça fork do repositório

Crie um branch com sua feature (git checkout -b feature/incrivel)

Commit suas mudanças (git commit -am 'Add incrivel feature')

Push para o branch (git push origin feature/incrivel)

Abra um Pull Request