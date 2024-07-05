import logging
import os

import openai
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import ChatPromptTemplate

from models import OpenPosition
from candidate import Candidate, TipScore
from pdf_converter import PdfConverter


class Resume:
    PROMPT = """
    Act as an HR expert providing services to the organization and its employees. Your tasks include supporting HR processes such as recruitment and onboarding, and providing advice to employees and managers. Your primary goal is to evaluate candidates based on their suitability for a given position.

    Scoring Instructions:
    - The score should range from 0 to 10.
    - A score of 0 indicates the candidate does not meet the basic requirements (e.g., incorrect degree or insufficient experience).
    - A score of 7 indicates the candidate meets all basic requirements.
    - Scores above 7 are for candidates who meet all basic requirements and also have desirable qualifications or experience. The maximum score of 10 is reserved for candidates who perfectly match both the required and preferred criteria.

    You should provide json format for the following questions:

    name: str - the name of the candidate
    linkdin_url: str - the linkdin url of the candidate (optional)
    email: str - the email of the candidate
    phone: str - the phone of the candidate
    city: str - the city of the candidate
    github: str - the github of the candidate (optional)
    score: int - the score of the candidate (0-10) how much he is suitable for the position, if the candidate is not suitable for the position, or don't have enough experience, as asked, or the same degree or the amount of years of experience, the score should be 0.
                if the candidate is suitable for the position, the score should be between 1-10. and 10 means, the candidate is very suitable for the position, did the candidate have all the requirements, and the experience needed, with the degree and the amount of years of experience.
    tips: str - tips for the candidate how to improve his resume, What's to need to be done to get a higher score, 
                or maybe which positions he is more suitable for.
    
    Format the output as JSON with the following keys:
    name
    linkdin_url
    email
    phone
    city
    github
    score
    tips
    
    Position:
    {position}
    
    Candidate Resume:
    {resume}
    """

    def __init__(self, candidate: Candidate, verbose: bool = False):
        self.pdf_converter = PdfConverter(candidate.resume)
        self.candidate = candidate
        self.llm_model = "gpt-3.5-turbo-16k"
        self.logger = logging.getLogger(__name__)
        self._config_logging_level(level=logging.DEBUG if verbose else logging.INFO)
        self._init_openapi()
        self.style = "American English in a calm and respectful tone"

    def _init_openapi(self):
        load_dotenv(find_dotenv())
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def _config_logging_level(self, level=logging.DEBUG):
        format_logging = "%(asctime)s %(name)s.%(funcName)s +%(lineno)s: %(message)s"
        handlers = [logging.StreamHandler()]
        logging.basicConfig(handlers=handlers, datefmt="%H:%M:%S", level=level, format=format_logging)

    def _get_completion(self, prompt: str, model: str):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(model=model, messages=messages, temperature=0, )
        return response.choices[0].message["content"]

    def _get_response_schema(self) -> list[ResponseSchema]:
        gift_schema = ResponseSchema(name="name", type="str", required=True,
                                     description="the name of the candidate")
        linkdin_url_schema = ResponseSchema(name="linkdin_url", type="str", required=False,
                                            description="the linkdin url of the candidate")
        email_schema = ResponseSchema(name="email", type="str", required=True,
                                      description="the email of the candidate")
        phone_schema = ResponseSchema(name="phone", type="str", required=True,
                                      description="the phone of the candidate")
        city_schema = ResponseSchema(name="city", type="str", required=True,
                                     description="the city of the candidate")
        github_schema = ResponseSchema(name="github", type="str", required=False,
                                       description="the github of the candidate")
        score_schema = ResponseSchema(name="score", type="int", required=True,
                                      description="the score of the candidate (0-10) "
                                                  "how much he is suitable for the position")
        tips_schema = ResponseSchema(name="tips", type="str", required=False,
                                     description="tips for the candidate how to improve his resume, "
                                                 "What's to need to be done to get a higher score, "
                                                 "or maybe which positions he is more suitable for.")
        response_schemas = [
            gift_schema,
            linkdin_url_schema,
            email_schema,
            phone_schema,
            city_schema,
            github_schema,
            score_schema,
            tips_schema,
        ]
        return response_schemas

    def summary(self) -> str:
        prompt = f"""
        Summary the candidate data base on his resume:
        what is the candidate's name?
        How many years of experience does the candidate have?
        where the candidate lives?
        what is the candidate's email?
        relevant experience to what kind of positions the candidate can apply?
        Write it in a style of {self.style}
        
        candidate information:
        
        {self.pdf_converter.convert_to_text()}
        """
        return self._get_completion(prompt, self.llm_model)

    def compute(self, position: OpenPosition) -> Candidate:
        text_resume = self.pdf_converter.convert_to_text()
        response_schema = self._get_response_schema()
        output_parser = StructuredOutputParser.from_response_schemas(response_schema)
        format_instructions = output_parser.get_format_instructions()

        prompt_template = ChatPromptTemplate.from_template(template=Resume.PROMPT)
        messages = prompt_template.format_messages(position=str(position), resume=text_resume)

        chat = ChatOpenAI(temperature=0.0, model=self.llm_model)
        response = chat(messages)
        output_dict = output_parser.parse(response.content)

        self.logger.debug(response)
        self.logger.debug(format_instructions)
        self.logger.debug(output_dict)

        tip_score = TipScore(tips=output_dict["tips"], score=output_dict["score"])

        self.candidate.name = output_dict["name"]
        self.candidate.linkdin_url = output_dict.get("linkdin_url")
        self.candidate.email = output_dict["email"].lower()
        self.candidate.phone = output_dict["phone"]
        self.candidate.city = output_dict["city"]
        self.candidate.github = output_dict.get("github")
        position_id = f"{position.id} - {position.title} - {position.company}"
        self.candidate.positions_scores[position_id] = tip_score

        return self.candidate
