// Learn more about clients at https://docs.boundaryml.com/docs/snippets/clients/overview
client<llm> OpenRouter {
  provider "openai-generic"
  options {
    base_url "https://openrouter.ai/api/v1"
    api_key env.OPENROUTER_API_KEY
    model deepseek/deepseek-chat-v3-0324
    temperature 0.0
    headers {
      "X-Title" "Zapier project"
    }
  }
}
