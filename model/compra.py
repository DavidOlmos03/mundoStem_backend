from sqlalchemy import Column, Integer, ForeignKey, ForeignKeyConstraint
from connection.connection import Base


class compra_model(Base):
    __tablename__ = 'compras'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('usuarios.id'))
    product_id = Column(Integer , ForeignKey('producto.id'))
    total_products = Column(Integer, nullable=True)

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['usuarios.id']),
        ForeignKeyConstraint(['product_id'], ['producto.id'])
    )
    #user = relationship("user_model",foreign_keys=[user_id])
    #product = relationship("product_model",foreign_keys=[product_id])
