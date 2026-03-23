# AI Coding Agent

A command-line AI agent powered by Google Gemini that can read, write, and execute files in a sandboxed working directory.

## Features

- List directory contents
- Read file contents
- Write and overwrite files
- Execute Python files with optional arguments

## Project Structure

```
aiagent/
├── calculator/          # Working directory for the agent
│   ├── main.py
│   ├── tests.py
│   ├── lorem.txt
│   └── pkg/
│       ├── calculator.py
│       └── render.py
├── functions/           # Agent tool functions
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── call_function.py     # Function dispatcher and tool declarations
├── prompts.py           # System prompt
├── config.py            # Configuration (e.g. MAX_CHARS)
└── main.py              # Entry point
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

```bash
uv run main.py "<your prompt>"
```

With verbose output:
```bash
uv run main.py "<your prompt>" --verbose
```

## Examples

```bash
uv run main.py "what files are in the root?"
uv run main.py "read the contents of main.py"
uv run main.py "run tests.py"
uv run main.py "write 'hello world' to hello.txt"
```

## Security

All file and execution operations are sandboxed to the `calculator/` working directory. The agent cannot access or modify files outside of it.