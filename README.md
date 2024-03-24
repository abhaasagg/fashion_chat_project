# KEEP UP WITH FASHION

With our fast moving life it becomes more and more important to get some help with keeping up with the trends.
This project is an application where users input their city, and it provides clothing recommendations based on the current weather. Utilizing a weather API, it fetches weather data for the user's location, analyzes it using ChatGPT, and suggests suitable attire for the prevailing conditions, enhancing users' fashion choices. The result is  further optimised by using latest fashion articles and magazines which can be put in the dropbox for reference.

## Demo

See how the tool works:

![search tool demo](assets/search-tool.gif)

## How to run the tool

### Run with Docker

1. Create `.env` file in the root directory of the project, copy and paste the below config. Replace the `OPENAI_API_TOKEN` configuration value with your key `{OPENAI_API_KEY}` and replace `DROPBOX_LOCAL_FOLDER_PATH` with a path where Dropbox folder is located `{REPLACE_WITH_DROPBOX_FOLDER_PATH}`. For example, if the current project folder is `DROPBOX-SEARCH-TOOL`, you navigate to the Dropbox path in the home directory: `../Dropbox/documents`. Other properties are optional to change and be default.

```bash
OPENAI_API_TOKEN={OPENAI_API_KEY}
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
DROPBOX_LOCAL_FOLDER_PATH={REPLACE_WITH_DROPBOX_RELATIVE_PATH}
```
2. Add supplementary fashion articles and magazine pdfs in your dropbox folder.
3. From the project root folder, open your terminal and run `docker compose up`.
4. Navigate to `localhost:8501` on your browser when docker installion is successful.
5. Enter your city and get the latest and most aprropriate fashion recommendations.
