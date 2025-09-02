from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import torch
import asyncio

MODEL_NAME = "farizkuy/ner_fine_tuned_gdsc_tutoring_fariz"

# Load model and tokenizer once at import
model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
device = 0 if torch.cuda.is_available() else -1
ner_pipeline = pipeline(
    "ner",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple",
    device=device
)

async def predict_ner(text: str):
    loop = asyncio.get_event_loop()
    results = await loop.run_in_executor(None, ner_pipeline, text)
    # Normalize results to clearer format
    entities = []
    for ent in results:
        entities.append({
            "text": ent.get("word") or ent.get("entity"),
            "label": ent.get("entity_group") or ent.get("entity"),
            "start": ent.get("start"),
            "end": ent.get("end"),
            "score": round(ent.get("score", 0), 4)
        })
    return {"text": text, "entities": entities}
