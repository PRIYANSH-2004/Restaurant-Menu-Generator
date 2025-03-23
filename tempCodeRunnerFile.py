from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from secret_key import GEMINI_KEY
import os

key = os.environ['GEMINI_KEY']
print(key)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=key,
    temperature=0.6,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food in India. Suggest a fancy name for this. list only one name"
    )


    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,
                        output_key='resturant_name')
    print(name_chain)
    prompt_template_items = PromptTemplate(
        input_variables=['resturant_name'],
        template="Suggest some menu items for {resturant_name}. Return it as comma separated form."
    )
    food_items_chain = LLMChain(
        llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain2 = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'], 
    output_variables = ['restaurant_name', 'menu_items']
    )
    response2 = chain2({"cuisine" , cuisine})

    return response2


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))