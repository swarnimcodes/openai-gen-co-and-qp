from openai import OpenAI

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from typing import Dict, Any
import json


client = OpenAI()
router = APIRouter()
MODEL = "gpt-3.5-turbo-0125"


@router.post("/v1/gen_course_outcomes")
async def gen_course_outcomes(data: Dict[str, Any] = Body(...)):
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """
                        You are a detailed course outcome generator. 
                        Generate exactly the number of course outcomes (n) as you are being asked of. No more, no less.
                        You will be provided syllabus/handout of a course and you need to generate `n` appropriate JSON formatted course outcomes in meticulous detail as to what the students should be able to do after completing the course.
                        Attach a list of applicable Blooms Taxonomy tags applicable per course outcome.
                        Attach course outcome number.
                        Give a short title to the course outcome as well.
                        Generate exactly `n` course outcomes. No more, no less.

                        Generate the outcomes with lightning speed as speed is paramount.

                        Output JSON keys per course outcome: outcome_number, title, description, blooms_taxonomy_tags
                    
                    """,
                },
                {"role": "user", "content": f"{data}"},
            ],
            response_format={"type": "json_object"},
            temperature=0.5,
        )
        ai_response = json.loads(completion.choices[0].message.content)
        print(type(completion.choices[0].message.content))
        return JSONResponse(status_code=200, content=ai_response)
    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"error": f"{err}"},
        )
