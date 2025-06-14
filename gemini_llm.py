# !pip install google-ai-generativelanguage
import google.generativeai as genai

genai.configure(api_key="AIzaSyDEp7vlPj0Zwsd_5asY9BLDRF_TbkzI9Ic")

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

# Generate content
response = model.generate_content("Tell me a story about a brave knight.")
print(response.text)

