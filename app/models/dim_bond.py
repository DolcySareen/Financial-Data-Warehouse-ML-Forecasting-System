from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

class DimBond(db.Model):
    __tablename__ = "dim_bond"

    sk_bond_id = Column(Integer, primary_key=True, autoincrement=True)
    treasury_name = Column(String, nullable=True)

    @staticmethod
    def load_dim_bond(session: Session, bond_data: dict) -> int:
        existing = session.query(DimBond).filter_by(treasury_name=bond_data["treasury_name"]).one_or_none()

        if existing:
            # Return the ID of the existing record without making any changes
            return existing.sk_bond_id

        # Insert a new record
        new_bond = DimBond(
            treasury_name=bond_data.get("treasury_name")
        )
        session.add(new_bond)
        session.commit()
        return new_bond.sk_bond_id
    
    @staticmethod
    def get_bond_id(session: Session, treasury_name: str) -> int:
        bond = session.query(DimBond).filter_by(treasury_name=treasury_name).one_or_none()
        return bond.sk_bond_id if bond else None
