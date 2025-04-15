# Captioner-Aug: Towards the Robustness of Image Sets Captioning

This project is an extension of [VisDiff](https://github.com/Understanding-Visual-Datasets/VisDiff), introducing *Captioner-Aug* in replace of the original captioner in VisDiff to capture image quality information in an affordable way. 

As shown below *Captioner-Aug* augments the original captioner using external image processing tools such as FFT-based blur detectors. A [ReAct](https://github.com/ysymyth/ReAct)-style selects one of the user-defined tools based on a prompt, leveraging the reasoning abilities of large language models (LLMs). We implement the agent via [Langchain](https://www.langchain.com/).

![image](captioner-aug.PNG)

## Reproduction
Please first reproduce [VisDiff](https://github.com/Understanding-Visual-Datasets/VisDiff) and follow their instructions to install necessary packages. Then replace ```proposer.py``` in `\components` with our modified version. 

The implementation of our ReAct agent is in `\augmented_captioner`. Please place this folder under the root directory of VisDiff.

