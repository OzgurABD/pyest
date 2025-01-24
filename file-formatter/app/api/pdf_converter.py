import os
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from services.file_handler import handle_pdf_word_v1, handle_pdf_word_v2, handle_pdf_to_pptx

router = APIRouter()


@router.post("/convert_pdf_to_word/")
async def convert_pdf_to_word(file: UploadFile = File(...)):
    try:
        result = await handle_pdf_word_v2(file)

        return FileResponse(
            result["filePath"],
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=os.path.basename(result["fileName"])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/convert_pdf_to_pptx/")
async def convert_pdf_to_pptx(file: UploadFile = File(...)):
    try:
        pptx_path = await handle_pdf_to_pptx(file)

        return FileResponse(
            pptx_path,
            media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            filename=os.path.basename(pptx_path)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
