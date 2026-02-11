import uvicorn
from confluent_kafka import Producer
from fastapi import FastAPI, responses

from congif import kafka_producer_config, settings
from modols import UserModel
from producer import send_user

producer = Producer(kafka_producer_config.model_dump(by_alias=True))
app = FastAPI()


@app.post("/register/", status_code=201)
def register(data: UserModel):
    try:
        value = data.model_dump_json().encode("utf-8")
        send_user(producer, value)
        return {"status": "accepted",
                "message": "user published to kafka"}
    except Exception as e:
        responses.JSONResponse(
            status_code=400,
            content={"status": "error", "message": str(e)}
        )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=settings.debug,
    )
