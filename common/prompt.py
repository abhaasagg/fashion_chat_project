import pathway as pw
from common.openaiapi_helper import openai_chat_completion
from common.weather import get_weather


def prompt(index, embedded_query, user_query):
    weather_str = get_weather(user_query)

    @pw.udf
    def build_prompt(local_indexed_data, query):
        docs_str = "\n".join(local_indexed_data)
        prompt = f"Given the following data about clothes to wear in particular weather: \n {docs_str} \n.{query} \n. Tell me what clothes to wear."
        return prompt

    query_context = embedded_query + index.get_nearest_items(
        embedded_query.vector, k=3, collapse_rows=True
    ).select(local_indexed_data_list=pw.this.chunk).promise_universe_is_equal_to(
        embedded_query
    )

    prompt = query_context.select(
        prompt=build_prompt(pw.this.local_indexed_data_list, weather_str)
    )

    return prompt.select(
        query_id=pw.this.id,
        result=openai_chat_completion(pw.this.prompt),
    )
