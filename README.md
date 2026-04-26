# Universal Voice AI (Groq Streaming Edition)

Windowsの標準音声入力 (Win+H) が使えない環境でも動作する、爆速AI搭載型音声入力ユーティリティ。

## 特徴
- **Ultra Low Latency**: Groq Whisper APIにより、話した内容が即座に画面に表示されます。
- **Live Preview Overlay**: 録音中のテキストはAIウィンドウ内にのみ表示。エディタ側の入力と競合しません。
- **AI Polishing**: 録音終了時、Llama-3.3が言い淀みを除去し、完璧な文章に整えてから1回だけペーストします。
- **Global Hotkey**: `F8` キーでいつでもどこでも録音のオン／オフが可能。

## セットアップ

### 1. 依存ライブラリのインストール
```bash
pip install -r requirements.txt
```

### 2. Groq APIキーの取得
[Groq Cloud](https://console.groq.com/) でAPIキーを取得してください。

### 3. 実行
```bash
python main.py
```
起動後、画面右下のウィンドウを**右クリック**して設定を開き、APIキーを保存してください。

## 使い方
1. `F8` キーを押すと録音が始まります。
2. AIウィンドウ内にリアルタイムで文字がプレビューされます。この間、エディタ側で手動入力を続けても問題ありません。
3. 再度 `F8` を押すと、AIが文章を整え、カーソル位置に「清書」されたテキストが一瞬で入力されます。
4. ウィンドウはドラッグで好きな位置に移動できます。
