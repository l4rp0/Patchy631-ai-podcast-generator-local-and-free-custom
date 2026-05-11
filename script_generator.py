import os
from groq import Groq

class ScriptGenerator:
    def __init__(self):
        # This will now look for the GROQ_API_KEY we set in the app sidebar
        self.api_key = os.environ.get('GROQ_API_KEY')
        self.client = Groq(api_key=self.api_key)
    
    def generate(self, content: str) -> str:
        """Generate podcast script from content using Groq (Llama 3.3)."""
        prompt = self._create_prompt(content)
        
        try:
            # We use llama-3.3-70b-versatile because it's fast and smart
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a professional podcast script writer who specializes in engaging, natural dialogue."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2048
            )
            
            script = completion.choices[0].message.content
            return script
            
        except Exception as e:
            raise Exception(f"Groq Script generation failed: {str(e)}")
    
    def _create_prompt(self, content: str) -> str:
        return f"""Convert the following content into an engaging podcast script between two hosts.

Format the script as a natural conversation with:
- Host 1 (Male): A curious and enthusiastic interviewer
- Host 2 (Female): A knowledgeable expert on the topic

Requirements:
- Break down complex topics into digestible segments
- Use conversational language
- Include natural transitions and reactions
- Keep it engaging, informative and concise. 
- Format each line EXACTLY as "Host 1:" or "Host 2:" followed by their dialogue

Content to convert:
{content}

Generate the podcast script now:"""