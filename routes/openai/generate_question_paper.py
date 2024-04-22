from openai import OpenAI

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from typing import Dict, Any
import json


client = OpenAI()
router = APIRouter()
MODEL = "gpt-3.5-turbo-0125"


@router.post("/v1/generate_subjective_questions")
async def generate_subjective_questions(data: Dict[str, Any] = Body(...)):
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a professional question generator for a world class university.
                    You are to generate subjective questions for a given `course_name`.
                    The questions should test various aspects of a students understanding of the course.

                    Input JSON Schema:
                        - course_name: string
                        - textbook_name: string
                        - isbn: ISBN of the book
                        - topic: module or chapter from the book that students need to be tested on
                        - difficulty: ['easy', 'medium', 'difficult']
                        - number_of_questions: number of questions to generate

                    
                    The questions should test deep conceptual understanding of the subject.
                    Generate multi faceted questions only.
                    Each question may have more than one questions.
                    For each question you may chain multiple concepts by asking a question
                    that links to the next part and so on. So each question may have sub parts.
                    Verify that the questions you generate are sane.
                    Do not be lazy.
                    Read the context patiently.

                    Output should be in JSON format.
                    Output JSON Schema:
                        - question: String
                        - difficulty = ['easy', 'medium', 'difficult']
                        - question_type = "subjective"
                    """,
                },
                {"role": "user", "content": f"{data}"},
            ],
            response_format={"type": "json_object"},
            temperature=0.75,
        )
        ai_response: str | None = completion.choices[0].message.content
        if ai_response is not None:
            ai_response_json = json.loads(ai_response)
            return JSONResponse(status_code=200, content=ai_response_json)
        else:
            return JSONResponse(
                status_code=500,
                content={"error": "Could not get a response from OpenAI."},
            )

    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"error": f"{err}"},
        )


@router.post("/v1/generate_mcq")
async def generate_mcq(data: Dict[str, Any] = Body(...)):
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """
                        You are a professional MCQ generator for a world class university.
                        Your job is to generate multifaceted questions based on the following input JSON schema:
                            - course_name: name of the course
                            - textbook_name: name of the textbook used for the course
                            - textbook_authors: authors of the said textbook
                            - isbn: isbn of the said textbook
                            - topic: module or chapter from the book that students need to be tested on
                            - difficulty: ['easy', 'medium', 'difficult']
                            - number_of_questions: number of questions to generate
                        Being lazy is not allowed.
                        Output should be in JSON format.                    
                        Output JSON schema: 
                            - question: str
                            - options: Dict[str,str] = {"A": "", "B": "", "C": "", "D": ""}
                            - question_type: str = "Multiple Choice"
                            - difficulty: str
                            - correct_answer: str
                    """,
                },
                {"role": "user", "content": f"{data}"},
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
        )
        ai_response: str | None = completion.choices[0].message.content
        if ai_response is not None:
            ai_response_json = json.loads(ai_response)
            return JSONResponse(status_code=200, content=ai_response_json)
        else:
            return JSONResponse(
                status_code=500,
                content={"error": "Could not get a response from OpenAI."},
            )
    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"error": f"{err}"},
        )


@router.post("/v1/gen_question_paper")
async def gen_question_paper(data: Dict[str, Any] = Body(...)):
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """
                        You are a professional question generator based on course outcomes fed to you. 
                        Generate the number of subjective questions and number of objective as asked of you.
                        Generate detailed and professional questions that will be used in an actual question paper for students of a course.
                        Generate questions of mixed difficulty ranging from easy to difficult.
                        Output should be in JSON format.                    
                        Output JSON schema: 
                            - question: str
                            - question_type: str
                            - difficulty: str
                            - correct_answer: str
                    """,
                },
                {"role": "user", "content": f"{data}"},
            ],
            response_format={"type": "json_object"},
            temperature=0.5,
        )
        ai_response: str | None = completion.choices[0].message.content
        if ai_response is not None:
            ai_response_json = json.loads(ai_response)
            return JSONResponse(status_code=200, content=ai_response_json)
        else:
            return JSONResponse(
                status_code=500,
                content={"error": "Could not get a response from OpenAI."},
            )
    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"error": f"{err}"},
        )
