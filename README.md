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

## Future Directions

This project serves as a foundation and there are numerous ways in which it can be extended and improved. Here are some possible directions for future development:

### Convert to a Flask App with Material UI Frontend

The current script-based approach is great for simplicity but can be extended to a more user-friendly web application. By converting the backend to a Flask app and using Material UI for a modern, responsive frontend, the interaction with the ChatGPT API can be made seamless for the users.

### Improved Auto-Directed Prompting for Consistency Checks

Though the current implementation generates a story based on a prompt, it can be improved by integrating additional auto-directed prompting. This would involve checking for inconsistencies in the story and making efforts to improve the overall quality and coherence of the content generated.

### Robust Error Handling

As with any application, especially one that interacts with an external API, robust error handling is key. Future developments could include more extensive error checking and handling to ensure that users have a smooth experience even when things go wrong.

### Data Persistence

As the novel is being created, it might be useful to persist the data to a database. This not only provides a way to save progress but also opens up possibilities for analytics and further interactions with the created content.

### Integration with Social Media Platforms

One interesting extension could be to allow users to publish snippets or entire chapters to social media platforms. This could help in gathering feedback and building an audience for the generated content.

### Customize Story Elements

Allow users to have more control over different story elements such as characters, setting, or plot twists. This could be achieved by presenting the users with customizable options and preferences that guide the generation process.

### Implementation of Feedback Loop

Implement a feedback loop where users can rate or give feedback on the generated content. This information can then be used to make the story generation more aligned with the preferences and expectations of the user.


## Contributing

Contributions to this project are welcome! Feel free to submit issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
