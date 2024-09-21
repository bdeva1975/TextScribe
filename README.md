# TextScribe: Building a Basic Generative AI Prototype

**TextScribe** demonstrates how to build a basic generative AI text generation application using very little code. The core focus is on leveraging OpenAI's GPT model for general content creation and basic question-answering. This simple architecture is particularly useful for tasks where factual accuracy is not critical and where common internet knowledge can suffice.

## Features
- **Generative AI Prototype**: Create and deploy a basic text generation app with minimal code.
- **Use Cases**:
  - General content creation (e.g., blogs, stories).
  - Basic Q&A for frequently asked, well-known facts.
- **Streamlit Integration**: A simple web-based interface to interact with the generative model.

## Table of Contents
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Use Cases](#use-cases)
- [Files Overview](#files-overview)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/TextScribe.git
   cd TextScribe
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then install the required packages using:
   ```bash
   pip install openai streamlit python-dotenv
   ```

3. **Setup OpenAI API key**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your-openai-api-key
   ```

## How It Works

- The **OpenAI GPT-3.5-turbo model** powers the text generation, responding to user input.
- The Streamlit interface accepts text input from the user and displays the generated response.
- The basic **text generation pattern** is ideal for content that doesn't require a high level of factuality but is good for creativity or answering commonly asked questions.

## Use Cases

1. **General Content Creation**: Generate ideas for articles, blogs, or stories without requiring fact-checking.
2. **Basic Question & Answer**: Provide answers to simple, well-known questions, especially those frequently found on the internet (e.g., historical dates, general knowledge).

## Files Overview

### `text_lib.py`
This file contains the function responsible for interacting with OpenAI's API to generate text responses based on user input.

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def get_text_response(input_content):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    # Generate response from the OpenAI API
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input_content}
        ],
        max_tokens=2000,
        temperature=0,
        top_p=0.9,
        stop=None
    )

    # Extract and return the response text
    return chat_completion.choices[0].message.content
```

### `text_app.py`
This file handles the Streamlit web application. It allows the user to input text, calls the `get_text_response()` function, and displays the generated content.

```python
import streamlit as st
import text_lib as glib

# Set page configuration
st.set_page_config(page_title="Text to Text")
st.title("Text to Text")

# Input text box
input_text = st.text_area("Input text", label_visibility="collapsed")
go_button = st.button("Go", type="primary")

# When the 'Go' button is clicked
if go_button:
    with st.spinner("Working..."):
        # Call the model and get the generated text
        response_content = glib.get_text_response(input_content=input_text)
        st.write(response_content)
```

## Running the Application

1. Run the Streamlit application with the following command:
   ```bash
   streamlit run text_app.py
   ```

2. Open your web browser and go to the address provided in the terminal (typically `http://localhost:8501`).

3. Input any text into the app, click the **Go** button, and view the generated response.

## Contributing

Feel free to fork this repository and open pull requests if you'd like to improve or add new features to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**TextScribe** offers a simple, yet powerful, demonstration of how to integrate OpenAI’s generative models into real-world applications using very little code.
