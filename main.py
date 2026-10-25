from fastapi import FastAPI, HTTPException, Depends
from typing import List
from database import Product, User, inventory_db

app = FastAPI(title="Inventory Management API", version="1.0.0")

# Simulación de autenticación por roles
def verify_admin_role(current_user: User):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Acceso denegado: Se requiere rol de Administrador")
    return current_user

@app.get("/")
def root():
    return {"message": "Bienvenido al Sistema de Gestión de Inventarios con Control de Roles"}

@app.get("/api/products", response_model=List[Product])
def get_products():
    """Obtener la lista completa de productos en inventario (Accesible para todos los roles)"""
    return inventory_db

@app.post("/api/products", response_model=Product)
def add_product(product: Product, role: str = "operator"):
    """Agregar un nuevo producto al inventario (Requiere rol admin simulado por parámetro)"""
    if role != "admin":
        raise HTTPException(status_code=403, detail="Solo los administradores pueden registrar nuevos productos.")
    
    # Verificar si ya existe el ID
    for p in inventory_db:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="El ID del producto ya existe.")
            
    inventory_db.append(product)
    return product

@app.put("/api/products/{product_id}", response_model=Product)
def update_stock(product_id: int, new_stock: int):
    """Actualizar el stock de un producto existente"""
    for p in inventory_db:
        if p.id == product_id:
            p.stock = new_stock
            return p
    raise HTTPException(status_code=404, detail="Producto no encontrado.")
