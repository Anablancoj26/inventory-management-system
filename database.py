from pydantic import BaseModel
from typing import List, Optional

# Modelos de Datos (Simulando esquema relacional)
class Product(BaseModel):
    id: int
    name: str
    category: str
    stock: int
    price: float

class User(BaseModel):
    username: str
    role: str  # 'admin' o 'operator'

# Base de datos simulada en memoria
inventory_db: List[Product] = [
    Product(id=1, name="Laptop Empresarial", category="Tecnología", stock=15, price=1200.0),
    Product(id=2, name="Escritorio Ergonómico", category="Muebles", stock=8, price=350.0),
    Product(id=3, name="Monitor 27 pulgadas", category="Tecnología", stock=22, price=250.0)
]
