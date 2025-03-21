# Further Project

A Streamlit app for ACME Senior Living's conversational AI assistant.

## Setup and Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   conda create -n further python=3.10
   conda activate further
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.sample` to `.env` and fill in your API keys.

## Running in Debug Mode

To run the Streamlit app in debug mode:

1. Open VS Code
2. Open the "Run and Debug" sidebar (Ctrl+Shift+D or Cmd+Shift+D)
3. Select "Streamlit: App" from the dropdown menu
4. Click the green play button or press F5

The app will start with debugging enabled, allowing you to:
- Set breakpoints in your code
- Inspect variables during runtime
- Step through your code
- Use the Debug Console

## Regular Run

To run the app without debugging:

```bash
streamlit run app.py
```