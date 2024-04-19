"""
Copyright (C) Iktos - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
"""

import logging
from typing import List, Union

from fastapi import FastAPI, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from src.controllers.sa_score_controller import sa_score_controller

app = FastAPI()

ForwardAddressHttpHeader = "X-Forward-To"
RequestIdHttpHeader = "X-Request-ID"
CorrelationIdHttpHeader = "X-Correlation-Id"


class Input(BaseModel):
    smiles: List[str]


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    console_formatter = uvicorn.logging.ColourizedFormatter(
        "{asctime} {levelprefix} : {message}", style="{", use_colors=True
    )
    logger.handlers[0].setFormatter(console_formatter)


@app.post("/score")
def sa_score_smiles(
    input_json: Input,
    x_request_id: Union[str, None] = Header(default=None),
    x_correlation_id: Union[str, None] = Header(default=None),
) -> JSONResponse:
    smiles_list = input_json.smiles
    return JSONResponse(
        content=jsonable_encoder(sa_score_controller(smiles_list)),
        headers=set_headers(x_request_id, x_correlation_id),
    )


@app.get("/health")
def get_info() -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(""))


def set_headers(
    x_request_id: Union[str, None] = Header(default=None),
    x_correlation_id: Union[str, None] = Header(default=None),
):
    hdr = {}
    if x_request_id is not None:
        hdr[RequestIdHttpHeader] = x_request_id

    if x_correlation_id is not None:
        hdr[CorrelationIdHttpHeader] = x_correlation_id

    return hdr
