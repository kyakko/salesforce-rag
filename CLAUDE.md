# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
ユーザーへの返答には必ず日本語を利用してください。

## Project Overview

This is a hybrid project combining:
- **Salesforce DX project** with Lightning Web Components (LWC) for the frontend chat interface
- **FastAPI backend** (`rag-fastapi/`) providing a RAG (Retrieval-Augmented Generation) chatbot service using OpenAI and ChromaDB

## Common Development Commands

### Salesforce Development
```bash
# Connect to srvcdevpro org
sf org login web --alias srvcdevpro

# Set srvcdevpro as default org
sf config set target-org srvcdevpro

# Deploy to srvcdevpro org
sf project deploy start --target-org srvcdevpro

# Create scratch org (if needed)
sf org create scratch -f config/project-scratch-def.json

# Push source to scratch org
sf project deploy start --source-dir force-app/main/default

# Pull source from scratch org
sf project retrieve start --source-dir force-app/main/default

# Open srvcdevpro org
sf org open --target-org srvcdevpro
```

### Testing and Code Quality
```bash
# Run all tests
npm test

# Run tests with coverage
npm run test:unit:coverage

# Run tests in watch mode
npm run test:unit:watch

# Run linter
npm run lint

# Format code
npm run prettier

# Verify formatting
npm run prettier:verify
```

### FastAPI Development
```bash
# Install Python dependencies
cd rag-fastapi
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload

# Production server (for Render deployment)
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

## Architecture Overview

### Frontend (Salesforce LWC)
- **chatLauncher**: Floating Intercom-style launcher button (bottom-right)
- **chatWindow**: Main conversation interface with message list and input
- **chatMessage**: Individual message rendering component
- **chatService.js**: Service for API communication and chat history management

### Backend (FastAPI)
- **main.py**: FastAPI application entry point
- **rag.py**: Vector search and OpenAI response generation
- **loader.py**: Text loading, splitting, and embedding creation
- **data/source.txt**: Knowledge base source file

### Key Integration Points
- Chat API endpoint: `POST /chat` - accepts `{ "query": "...", "history": [] }`
- Frontend uses direct `fetch()` calls to FastAPI backend
- Future: Save chat transcripts to Salesforce case records

## Environment Setup

### Required Environment Variables
- `OPENAI_API_KEY`: OpenAI API key for the RAG service (stored in `rag-fastapi/.env`)

### File Structure
```
├── force-app/main/default/    # Salesforce source code
├── rag-fastapi/              # Python FastAPI backend
├── config/                   # Scratch org configuration
├── docs/                     # Project documentation
└── scripts/                  # Apex and SOQL scripts
```

## Development Workflow

1. **Salesforce changes**: Use standard SFDX commands for deployment and retrieval
2. **API changes**: Test locally with `uvicorn --reload`, then deploy to Render
3. **Integration testing**: Run both services locally and test the full chat flow
4. **Code quality**: Always run linting and formatting before commits (enforced by husky pre-commit hooks)

## Testing and Verification Procedures

### Local Development Testing
```bash
# 1. Start FastAPI server locally
cd rag-fastapi
uvicorn app.main:app --reload --port 8000

# 2. Test API endpoint directly
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello", "history": []}'

# 3. Deploy LWC to Salesforce
sf project deploy start --target-org srvcdevpro

# 4. Open Salesforce org and test chat components
sf org open --target-org srvcdevpro
```

### Render Deployment Testing
```bash
# 1. Check Render deployment status
# Visit Render dashboard to verify deployment

# 2. Test production API endpoint
curl -X POST "https://your-render-app.onrender.com/chat" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello", "history": []}'

# 3. Update LWC API endpoint configuration
# Update chatService.js with production URL
```

### Full Integration Testing
1. **Deploy FastAPI to Render**: Ensure API is accessible at production URL
2. **Update LWC configuration**: Modify chatService.js with Render URL
3. **Deploy LWC to Salesforce**: Push updated components to srvcdevpro
4. **Test chat flow**: Open Salesforce and verify end-to-end functionality
5. **Monitor logs**: Check both Render and Salesforce debug logs for issues

## Notes

- API version: 64.0
- Node.js testing with Jest configured for LWC
- Prettier and ESLint configured for code formatting and linting
- Husky pre-commit hooks ensure code quality

---

# 日本語版

このファイルは、このリポジトリで作業する際にClaude Code (claude.ai/code)にガイダンスを提供します。

## プロジェクト概要

このプロジェクトは以下を組み合わせたハイブリッドプロジェクトです：
- **Salesforce DXプロジェクト** - フロントエンドチャットインターフェース用のLightning Web Components (LWC)
- **FastAPIバックエンド** (`rag-fastapi/`) - OpenAIとChromaDBを使用したRAG（検索拡張生成）チャットボットサービス

## 一般的な開発コマンド

### Salesforce開発
```bash
# srvcdevpro組織に接続
sf org login web --alias srvcdevpro

# srvcdevproをデフォルト組織として設定
sf config set target-org srvcdevpro

# srvcdevpro組織にデプロイ
sf project deploy start --target-org srvcdevpro

# スクラッチ組織を作成（必要に応じて）
sf org create scratch -f config/project-scratch-def.json

# スクラッチ組織にソースをプッシュ
sf project deploy start --source-dir force-app/main/default

# スクラッチ組織からソースをプル
sf project retrieve start --source-dir force-app/main/default

# srvcdevpro組織を開く
sf org open --target-org srvcdevpro
```

### テストとコード品質
```bash
# 全てのテストを実行
npm test

# カバレッジ付きでテストを実行
npm run test:unit:coverage

# ウォッチモードでテストを実行
npm run test:unit:watch

# リンターを実行
npm run lint

# コードをフォーマット
npm run prettier

# フォーマットを確認
npm run prettier:verify
```

### FastAPI開発
```bash
# Python依存関係をインストール
cd rag-fastapi
pip install -r requirements.txt

# 開発サーバーを実行
uvicorn app.main:app --reload

# 本番サーバー（Renderデプロイ用）
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

## アーキテクチャ概要

### フロントエンド（Salesforce LWC）
- **chatLauncher**: フローティングIntercomスタイルのランチャーボタン（右下）
- **chatWindow**: メッセージリストと入力を含むメインの会話インターフェース
- **chatMessage**: 個別のメッセージ表示コンポーネント
- **chatService.js**: API通信とチャット履歴管理用のサービス

### バックエンド（FastAPI）
- **main.py**: FastAPIアプリケーションのエントリーポイント
- **rag.py**: ベクトル検索とOpenAI応答生成
- **loader.py**: テキストの読み込み、分割、埋め込み作成
- **data/source.txt**: 知識ベースのソースファイル

### 主要な統合ポイント
- チャットAPIエンドポイント: `POST /chat` - `{ "query": "...", "history": [] }`を受け付け
- フロントエンドはFastAPIバックエンドへの直接的な`fetch()`呼び出しを使用
- 将来: チャットトランスクリプトをSalesforceケースレコードに保存

## 環境設定

### 必要な環境変数
- `OPENAI_API_KEY`: RAGサービス用のOpenAI APIキー（`rag-fastapi/.env`に格納）

### ファイル構造
```
├── force-app/main/default/    # Salesforceソースコード
├── rag-fastapi/              # Python FastAPIバックエンド
├── config/                   # スクラッチ組織設定
├── docs/                     # プロジェクトドキュメント
└── scripts/                  # ApexとSOQLスクリプト
```

## 開発ワークフロー

1. **Salesforce変更**: デプロイと取得に標準的なSFDXコマンドを使用
2. **API変更**: `uvicorn --reload`でローカルテスト後、Renderにデプロイ
3. **統合テスト**: 両方のサービスをローカルで実行し、完全なチャットフローをテスト
4. **コード品質**: コミット前に必ずリンティングとフォーマットを実行（huskyプレコミットフックで強制）

## テストと検証手順

### ローカル開発テスト
```bash
# 1. FastAPIサーバーをローカルで起動
cd rag-fastapi
uvicorn app.main:app --reload --port 8000

# 2. APIエンドポイントを直接テスト
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello", "history": []}'

# 3. LWCをSalesforceにデプロイ
sf project deploy start --target-org srvcdevpro

# 4. Salesforce組織を開いてチャットコンポーネントをテスト
sf org open --target-org srvcdevpro
```

### Renderデプロイテスト
```bash
# 1. Renderのデプロイ状況を確認
# Renderダッシュボードでデプロイを確認

# 2. 本番APIエンドポイントをテスト
curl -X POST "https://your-render-app.onrender.com/chat" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello", "history": []}'

# 3. LWCのAPIエンドポイント設定を更新
# chatService.jsを本番URLで更新
```

### 完全統合テスト
1. **FastAPIをRenderにデプロイ**: APIが本番URLでアクセス可能であることを確認
2. **LWC設定を更新**: chatService.jsをRender URLで変更
3. **LWCをSalesforceにデプロイ**: 更新されたコンポーネントをsrvcdevproにプッシュ
4. **チャットフローをテスト**: Salesforceを開いてエンドツーエンドの機能を確認
5. **ログを監視**: RenderとSalesforceの両方のデバッグログで問題を確認

## 注意事項

- APIバージョン: 64.0
- LWC用にJestで設定されたNode.jsテスト
- コードフォーマットとリンティング用にPrettierとESLintを設定
- Huskyプレコミットフックがコード品質を保証
- プロジェクトのSalesforce組織: srvcdevpro
- FastAPIホスティング: Render