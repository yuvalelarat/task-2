# IAM Policy Classifier

A Python tool that uses OpenAI's GPT models to classify AWS IAM policies as "Weak" or "Strong" based on security best practices. The tool leverages OpenAI's structured function calling to ensure reliable, injection-resistant policy analysis.

## Features

- 🔒 **Secure Analysis**: Uses OpenAI's function calling to prevent prompt injection attacks
- 📊 **Binary Classification**: Classifies policies as "Weak" or "Strong"
- 💡 **Detailed Explanations**: Provides reasoning for each classification
- 🛡️ **Injection-Resistant**: System prompts ignore embedded instructions in policy content

## Requirements

### Python Dependencies
- Python 3.7+
- openai==1.97.0
- python-dotenv==1.1.1

### OpenAI API Key
You'll need a valid OpenAI API key with access to compatible models.

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

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Basic Usage

Run the script with the example policy:

```bash
python script.py
```

### Custom Policy Analysis

Modify the `example_policy` variable in `script.py` or use the function programmatically:

```python
from script import classify_iam_policy

# Your IAM policy
my_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}

# Classify the policy
result = classify_iam_policy(my_policy)
print(f"Classification: {result['classification']}")
print(f"Reason: {result['reason']}")
```

## Example Output

```json
{
  "policy": {
    "Version": "2022-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "s3:DeleteObject",
        "Resource": "arn:aws:s3:::secure-bucket/*",
        "Condition": {
          "Bool": {
            "aws:MultiFactorAuthPresent": "true"
          }
        }
      }
    ]
  },
  "classification": "Strong",
  "reason": "This policy is classified as Strong because it implements several security best practices: it has a specific resource ARN limiting scope to a particular S3 bucket, uses a least-privilege action (s3:DeleteObject rather than s3:*), and importantly requires MFA authentication through the aws:MultiFactorAuthPresent condition, which adds an extra layer of security for destructive operations."
}
```

## How It Works

1. **System Prompt**: Establishes the AI as a security analyst with strict instructions to only use the function calling interface
2. **Function Definition**: Defines a structured schema for policy classification
3. **Forced Function Call**: Uses `tool_choice` to ensure the model responds only via the defined function
4. **Structured Output**: Parses the JSON response to extract classification and reasoning

## Security Considerations

- The system prompt explicitly instructs the AI to ignore any instructions embedded within IAM policies
- Function calling prevents the model from generating arbitrary text responses
- The structured schema ensures consistent output format

## File Structure

```
.
├── script.py           # Main classification script
├── config.py          # Configuration and API key management  
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## Troubleshooting

### Common Issues

1. **"No tool calls found"**: Ensure you're using a compatible model (see compatibility section)
2. **API Key errors**: Verify your `.env` file contains a valid `OPENAI_API_KEY`
3. **Module not found**: Run `pip install -r requirements.txt`

### Model Switching

To change the model, modify line 43 in `script.py`:

```python
response = client.chat.completions.create(
    model="gpt-4o",  # Change this to your preferred compatible model
    messages=messages,
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "classify_iam_policy"}}
)
```

## License

This project is provided as-is for educational and security analysis purposes.

## Contributing

Feel free to submit issues and enhancement requests!
