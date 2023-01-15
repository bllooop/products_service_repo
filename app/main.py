from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, models, schemas
from .database import engine
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry import trace
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.sdk.trace import TracerProvider

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/v1/products")
def create(details: schemas.CreateProduct, db: Session = Depends(get_db)):
    to_create = models.Product(
        name = details.name,
        price = details.price,
        shopid = details.shopid
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id":to_create.id
    }

@app.get("/v1/products")
async def read_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/v1/products/{id}")
async def read_product_by_id(id: int, db: Session = Depends(get_db)):
    result = crud.get_products_by_id(db, id = id)
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@app.get("/__health")
async def check_service():
    return


resource = Resource(attributes={
    SERVICE_NAME: "products-service"
})

jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

FastAPIInstrumentor.instrument_app(app)

trace.set_tracer_provider(TracerProvider())
SQLAlchemyInstrumentor().instrument(
    engine=engine,
    service="products-service",
)


@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)


