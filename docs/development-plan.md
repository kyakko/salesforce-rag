# RAG API + Salesforce Integration Development Plan

This document outlines the development policy for the Retrieval-Augmented Generation (RAG) chatbot that integrates a FastAPI service with a Salesforce Lightning Web Components (LWC) user interface.

## Repository Overview

The repository currently contains a minimal Salesforce DX (SFDX) project. The API portion will be added under a separate directory named `rag-fastapi/`.

```
├── force-app/          # Salesforce source (LWC, Aura, etc.)
├── config/             # Scratch org configuration
├── rag-fastapi/        # FastAPI project (to be created)
└── docs/               # Project documentation
```

## API Development Guidelines

* **Language & Framework**: Python 3.10+ using FastAPI.
* **Vector Database**: ChromaDB with local persistence.
* **LLM**: OpenAI API (gpt-4o). Store the API key in `.env` using the variable `OPENAI_API_KEY`.
* **Endpoints**:
  * `POST /chat` – accepts `{ "query": "...", "history": [] }` and returns an answer with source chunks.
* **Modules**:
  * `loader.py` – loads `data/source.txt`, splits the text, and builds embeddings.
  * `rag.py` – performs vector search and calls OpenAI to generate the response.
  * `main.py` – FastAPI entry point.
* **Render Deployment**:
  * Build command: `pip install -r requirements.txt`
  * Start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
  * Environment variable: `OPENAI_API_KEY`
  * Optional volume for `/chromadb` if persistence is needed.

## Salesforce LWC Development Guidelines

* **Components**:
  * `chatLauncher` – floating Intercom-style launcher at the bottom-right.
  * `chatWindow` – main conversation window containing message list and input field.
  * `chatMessage` – renders individual messages.
  * `chatService.js` – handles fetch requests to the FastAPI `/chat` endpoint and manages local history.
* **UX Notes**:
  * Include a loading indicator while awaiting API responses.
  * Prefer direct `fetch()` calls to the API; use an Apex proxy only if required by CORS or authentication.
* **Integration Points**:
  * Optionally save chat transcripts to Salesforce case records in future iterations.

## Project Setup

1. **Salesforce**
   * Use the existing `sfdx-project.json` for scratch org creation.
   * Retrieve and deploy LWC components via standard SFDX commands (`force:source:push`, `force:source:pull`).
2. **API**
   * Create the `rag-fastapi/` directory following the structure described above.
   * Provide a `.env.template` with `OPENAI_API_KEY=your-key`.
   * Install dependencies listed in `requirements.txt`.
3. **Local Development**
   * Run the FastAPI server locally with `uvicorn` to test the chatbot independently of Salesforce.
   * Use the LWC components in a scratch org or sandbox and configure the API endpoint URL in `chatService.js`.

## Future Enhancements

* Extend `loader.py` to automatically chunk PDFs or CSVs.
* Utilize the `history` array for multi-turn conversations.
* Tie conversations to Salesforce case records for traceability.


---

# 日本語版

以下は、上記のドキュメントの日本語訳を追加したものです。

## RAG APIとSalesforce連携の開発方針

FastAPIで構築するRAGチャットボットを、Salesforce Lightning Web Components (LWC) と連携させるための開発方針を紹介します。

## リポジトリ概要

現在、リポジトリには最小限のSalesforce DX (SFDX) プロジェクトが存在しており、API部分は `rag-fastapi/` ディレクトリに追加します。

```
├── force-app/          # Salesforceソース (LWC、Aura等)
├── config/             # Scratch org設定
├── rag-fastapi/        # FastAPIプロジェクト（新規作成）
└── docs/               # ドキュメント
```

## API開発ガイドライン

* **使用言語・フレームワーク**: Python 3.10以上、FastAPI
* **ベクトルDB**: ChromaDB（永続化対応）
* **LLM**: OpenAI API (gpt-4o)。`.env`に`OPENAI_API_KEY`を格納
* **エンドポイント**:
  * `POST /chat` – `{ "query": "...", "history": [] }` を受け取り、回答とソースチャンクを返す
* **モジュール**:
  * `loader.py` – `data/source.txt` を読み込み、テキスト分割とEmbedding作成
  * `rag.py` – ベクトル検索を行い、OpenAIに問い合わせて応答を生成
  * `main.py` – FastAPIのエントリポイント
* **Renderでのデプロイ**:
  * Build command: `pip install -r requirements.txt`
  * Start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
  * 環境変数: `OPENAI_API_KEY`
  * 必要に応じ `/chromadb` のボリュームで永続化

## Salesforce LWC開発ガイドライン

* **コンポーネント**:
  * `chatLauncher` –  右下に定義されたIntercom風のランチャー
  * `chatWindow` – メッセージ一覧と入力欄を含むメインウィンドウ
  * `chatMessage` – 各メッセージを表示
  * `chatService.js` – FastAPIの`/chat`エンドポイントへのfetchと履歴管理
* **UX メモ**:
  * API回答待機中はローディングを表示
  * 直接 `fetch()` を使用し、CORSや認証で必要な場合のみApexプロキシを利用
* **連携ポイント**:
  * 将来的にはチャットログをSalesforceケースレコードに保存

## プロジェクトセットアップ

1. **Salesforce**
   * 既存の `sfdx-project.json` を使ってscratch orgを生成
   * SFDXの標準コマンド (`force:source:push`, `force:source:pull`) でLWCコンポーネントをデプロイ・取得
2. **API**
   * `rag-fastapi/` ディレクトリを前述の構成で作成
   * `.env.template` に `OPENAI_API_KEY=your-key` を記述
   * `requirements.txt` に記述された依存パッケージをインストール
3. **ローカル開発**
   * `uvicorn`でFastAPIサーバーを起動し、Salesforceと独立してチャットボットをテスト
   * scratch orgやsandboxでLWCコンポーネントを利用し、`chatService.js`でAPIエンドポイントURLを設定

## 今後の拡張

* `loader.py`を拡張し、PDFやCSVを自動的にチャンク化
* `history`配列を活用したマルチターン会話
* チャット履歴をSalesforceケースレコードに繋げる

