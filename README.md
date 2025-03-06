# Anime RAG with MyAnimeList API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Um sistema de **Retrieval-Augmented Generation (RAG)** especializado em informações sobre animes, utilizando dados da [Jikan (API Não Oficial do MyAnimeList) ](https://api.jikan.moe/v4/anime). 

## ✨ Funcionalidades

- **Recuperação em tempo real** de dados de animes (títulos, sinopse, episódios, gêneros, etc.)
- Sistema de perguntas e respostas baseado em NLP
- Armazenamento vetorial de informações para recuperação eficiente
- Integração simplificada com a API Jikan (Não oficial do MyAnimeList)
- Modelo de linguagem ajustável para diferentes casos de uso

## 🧠 Como Funciona

- Extração de Dados: Consulta a API de animes para obter metadados estruturados. É armazenado em formato JSON para fácil recuperação.
- Processamento: Transforma dados em documentos textuais otimizados para NLP
- Armazenamento Vetorial: Usa FAISS para criar embeddings de alta dimensão
- Geração: Combina retrieval com modelos de linguagem (ex: DeepSeek 7B) para respostas contextuais
