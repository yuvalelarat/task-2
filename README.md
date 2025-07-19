## Prerequisites

- Python 3.7+
- OpenAI API key
- pip (Python package installer)

## Installation

1. **Clone or download the project**:
   ```bash
   git clone <repository-url>
   cd task-2
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Model Compatibility

⚠️ **Important**: This code is tightly coupled to the function calling behavior and will **only work** with models that support OpenAI's structured function calling.

### ✅ Compatible Models

- **gpt-4-1106-preview**
- **gpt-4-0125-preview**
- **gpt-4**
- **gpt-4o** (the latest and fastest GPT-4 model as of mid-2024)
- **gpt-3.5-turbo-1106** and later versions
- **gpt-3.5-turbo**
- and some other models, you can check on OpenAI's website to see which model can use functions and/or tools

These models support:
- `tools` with type "function"
- `tool_choice` for forcing a tool call
- Return of structured `tool_calls` in the response

With incompatible models, you may encounter:
- No tool call returned at all
- Freeform string completions instead of structured JSON
- Errors if `tool_choice` is enforced but the model can't comply

## Usage

### Running the Application

Execute the main application:
```bash
python app.py
```

### Input Options

The application provides two ways to input IAM policies:

1. **Paste JSON directly**: 
   - Select option 1
   - Paste your IAM policy JSON
   - Press Enter on an empty line to finish

2. **Select from files**:
   - Select option 2
   - Choose from available JSON files in the current directory

## API Reference

### classify_iam_policy(policy_json: dict) -> dict

Classifies an IAM policy using OpenAI's GPT-4 model.

**Parameters:**
- `policy_json` (dict): The IAM policy JSON object to classify

**Returns:**
- `dict`: Classification result containing:
  - `policy`: The original policy JSON
  - `classification`: "Weak" or "Strong"
  - `reason`: Detailed explanation of the classification

## Dependencies

- `openai==1.97.0`: OpenAI Python client library
- `python-dotenv==1.1.1`: Environment variable management