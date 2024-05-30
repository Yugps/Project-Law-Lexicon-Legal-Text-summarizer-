# Project Law Lexicon Legal Text summarizer
## Overview
This project implements a legal judgment summarizer using the Longformer encoder-decoder model. The goal is to generate concise summaries of legal abstracts, making it easier for legal professionals and researchers to quickly understand the key points of a case.

## Features
- **Longformer Model**: The core of this project is the Longformer, a transformer-based model designed to handle long sequences efficiently. It allows us to process legal texts with thousands of tokens while maintaining performance.
- **Summarization**: Given a legal abstract as input, the model generates a summary that captures the essential information. The summary can be used for quick reference or as an introduction to the full document.
- **End-to-End API**: I have provided an end-to-end API using Flask. Users can send legal abstracts to the API, which returns the corresponding summaries.
- **Downloading the model**: Link to download the model is here https://drive.google.com/file/d/1xi8nmiC-wYrPyU_9fzegOpIAzouQpoIp/view?usp=sharing
## Feel Free to customize the model and templates for your personal use 

## Important Info about Longformer Encoder Decoder Model
* Longformer: The Longformer is a transformer-based model designed to process long sequences efficiently. Traditional transformer models suffer from quadratic scaling of self-attention with sequence length, making them impractical for very long documents.
* The Longformer introduces an attention mechanism that scales linearly with sequence length, allowing it to handle documents with thousands of tokens or more1. It combines local windowed attention with task-motivated global attention. The Longformer has been successfully used for character-level language modeling and outperforms RoBERTa on long document tasks.
* Longformer Encoder-Decoder (LED):  It supports sequence-to-sequence (seq2seq) tasks with long input. With gradient checkpointing, mixed precision (fp16), and a sufficiently large GPU (e.g., 48GB), the input length can be up to 16K tokens2. This is particularly useful for tasks like document summarization or translation where the input text can be lengthy.
* Decoder Handling of Arbitrary Length Input: At training time, the decoder uses a triangular mask to prevent self-attention from “looking” at positions that are yet to be decoded. As a result, the decoder can handle shorter sequences than those it was trained with, and any padding is masked out during inference3. This flexibility allows the decoder to adapt to varying input lengths.

## Acknowledgments
The Longformer model was developed by AllenAI. We thank them for their contributions to the NLP community
