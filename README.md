# Basic ChatGPT API Prompt Engineering Example

This is a basic example of how to use the ChatGPT API to complete a simple self-directed project.

In this example, we use the ChatGPT API to ask the user for a single prompt and then generate a long short story or novella based on the prompt. This example can generate outputs up to 20 short chapters long.

## Usage

This project uses Python and Poetry. To run this project, you'll need the following:
## Basic ChatGPT API Prompt Engineering Example

This is a basic example of how to use the ChatGPT API to complete a simple self-directed project.

In this example, we use the ChatGPT API to ask the user for a single prompt and then generate a long short story or novella based on the prompt. This example can generate outputs up to 20 short chapters long.

## Usage

This project uses Python and Poetry. To run this project, you'll need the following:

- Python 3.9 or later
- Poetry, a Python dependency management tool

### Setting Up the Environment

1. First, clone this repository to your local machine.

    ```sh
    git clone https://github.com/nurse-the-code/basic-chatgpt-api-prompt-engineering.git
    cd basic-chatgpt-api-prompt-engineering
    ```

2. Next, install Poetry if you don't have it already. You can install it by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

3. Once Poetry is installed, navigate to the project directory and run the following command to install the project's dependencies:

    ```sh
    poetry install
    ```

4. Ensure that you have set up the virtual environment that Poetry created as your project interpreter if you are using an IDE like PyCharm. This will enable the IDE to recognize the packages and versions installed by Poetry.

### Running the Script

1. Once you have installed the dependencies, you can run the script using Poetry:

    ```sh
    poetry run python main.py
    ```

    This command tells Poetry to run the `main.py` script using the Python interpreter and dependencies in the virtual environment.

2. The script will ask you to enter a prompt. Type in a creative prompt and press Enter. The script will then communicate with the ChatGPT API to generate a long short story or novella based on the prompt.

3. After the generation is complete, the script will save the story in a text file and also print it to the console.

### Configurations

This project uses the OpenAI ChatGPT API. You need to set your OpenAI API key and Organization ID as environment variables to authenticate with the API. You can set the environment variables as follows:

```sh
export OPENAI_ORG_ID="your-organization-id-here"
export OPENAI_API_KEY="your-api-key-here"
```

Replace `your-organization-id-here` with your actual Organization ID and `your-api-key-here` with your actual API key. These values are used in the `main.py` script as follows:

```python
openai.organization = os.environ.get("OPENAI_ORG_ID")
openai.api_key = os.environ.get("OPENAI_API_KEY")
```

## Contributing

Contributions to this project are welcome! Feel free to submit issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
