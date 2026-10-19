from tiendaAmont import PKModel, column, db 
class Categoria(PKModel):
    __tablename__ = "categorias"
    nombre = column(db.String(100), nullable=False, unique=True)
    descripcion = column(db.String(255), nullable=False)
    
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"