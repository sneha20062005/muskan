from google import genai


class AIService:        #class
    def __init__(self):   #constructor
        self.client = genai.Client()

    def generate_reply(self, prompt):
        response = self.client.models.generate_content(
            model = "gemini-2.5-flash",contents=prompt
        )
        return response_text  
    

