from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

# import sys
# sys.path.append("D:/UWaterloo/academics/programs/langchain/ice_breaker")
from .tools import detect_blur_fft

def detect_blur_of_img(img_path: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo"
    )
    template = '''Given an image with path {image_path} I want you to know if the image is blurry or sharp.
    Your answer should be one of the following sentences describing the image:
    "The image appears to be blurry" or "The image appears to be sharp."'''

    prompt_template = PromptTemplate(
        template=template, input_variables=["image_path"]
    )

    tools_for_agent = [
        Tool(
            name="Detect if the image is blurry or sharp",
            func=detect_blur_fft,
            description="useful for when you need to know if the image is burry or sharp"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke({"input": prompt_template.format_prompt(image_path=img_path)})

    description = result["output"]
    return description

if __name__ == '__main__':
    des = detect_blur_of_img('axolotl_1_blur.jpg')
    print(des)