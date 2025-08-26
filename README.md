# Smart Email Rewriter

An AI-powered email rewriting API using OpenAI, DeepSeek, or Perplexity models.

### 🔧 Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Create a `.env` file and add your API keys:

```
OPENAI_API_KEY=your_openai_key
DEEPSEEK_API_KEY=your_deepseek_key
PERPLEXITY_API_KEY=your_perplexity_key
```

3. Run the server:

```
uvicorn app:app --reload --port 10000
```

### 🧠 API Endpoint

POST `/rewrite`

**Body:**

```json
{
  "prompt": "Make this more professional",
  "email": "hi john, please fix that bug asap.",
  "provider": "openai"
}
```

**Response:**

```json
{
  "rewritten_email": "Dear John, could you please prioritize resolving that issue at your earliest convenience?"
}
```

---

### ✅ Supported Providers

- OpenAI (`gpt-4`, `gpt-3.5`)
- DeepSeek (`deepseek-chat`)
- Perplexity (`mistral-7b-instruct`)

---

✅ Deploy to [Render](https://render.com) with `render.yaml` and plug it into Aistrix.