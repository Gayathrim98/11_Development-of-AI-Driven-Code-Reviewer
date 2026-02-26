# import os
# from google import genai

# API_KEY = os.getenv("GEMINI_API_KEY")

# if not API_KEY:
#     raise ValueError("GEMINI_API_KEY not found in environment variables")

# client = genai.Client(api_key=API_KEY)


# def get_gemini_review(code, analysis):
#     prompt = f"""
# You are an expert Python code reviewer.

# Code:
# {code}

# Static analysis result:
# {analysis}

# Give:
# - Issues
# - Improvements
# - Best practices
# """

#     response = client.models.generate_content(
#     model="models/gemini-2.5-pro",
#     contents=prompt
# )


#     return response.text
