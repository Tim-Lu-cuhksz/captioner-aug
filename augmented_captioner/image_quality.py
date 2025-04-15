from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from .detect_blur import detect_blur_of_img as blur_detect_agent

def get_aug_caption(aug_prompt: str, img_path):
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo"
    )

    template = ''' We have provided the following techniques to detect patterns in an image:
    1. Blur: a method to detect if the image is blurry or sharp.
    2. Gaussian Noise: a method to detect if Gaussian noise persists in the image.
    3. Brightness: a method to detect if the image is bright or not.
    4. Contrast: a method to detect if the image has high contrast or not.

    You are provided a prompt that specifes a problem that could be potentially be solved via the above techiques.
    The prompt is {prompt}.

    Now output a technique that best matches the problem. 
    Your output should be one of the following: "Blur", "Gaussian Noise", "Brightness", "Contrast", or "None" if none of the method matches.
    '''

    prompt_template = PromptTemplate(
        input_variables=["prompt"], template=template,
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = prompt_template | llm

    res = chain.invoke({'prompt':aug_prompt})
    print("We use:", res.content)
    
    if res.content == 'Blur':
        aug_caption = blur_detect_agent(img_path)
    else:
        raise NotImplementedError

    return aug_caption


if __name__ == '__main__':
    msg = 'describe if the image is blurry or not'
    # msg = 'describe if the image is red or not'
    path = "./data/examples/set_a/000001.jpg"
    # path = "axolotl_1.jpg"
    aug_caption = get_aug_caption(msg, path)
    print("Augmented caption:", aug_caption)
