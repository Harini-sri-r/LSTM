document.addEventListener('DOMContentLoaded', () => {
  const generateBtn = document.getElementById('generateBtn')
  const promptEl = document.getElementById('prompt')
  const lengthEl = document.getElementById('length')
  const generatedTextEl = document.getElementById('generatedText')
  const errorEl = document.getElementById('error')

  async function generateText() {
    errorEl.hidden = true
    generatedTextEl.textContent = 'Generating...'

    const payload = {
      prompt: promptEl.value.trim(),
      length: Number(lengthEl.value || 20)
    }

    try {
      const response = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })

      if (!response.ok) {
        const data = await response.json()
        throw new Error(data.error || 'Generation failed')
      }

      const data = await response.json()
      generatedTextEl.textContent = data.generated_text
    } catch (err) {
      errorEl.hidden = false
      errorEl.textContent = err.message
      generatedTextEl.textContent = ''
    }
  }

  generateBtn.addEventListener('click', generateText)
})
