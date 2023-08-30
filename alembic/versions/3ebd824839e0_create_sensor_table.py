"""create sensor table

Revision ID: 3ebd824839e0
Revises:
Create Date: 2023-08-30 20:17:36.201772

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy_utils import create_database, database_exists

from alembic import context, op

config = context.config
url = config.get_main_option("sqlalchemy.url")

# revision identifiers, used by Alembic.
revision: str = "3ebd824839e0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    engine = sa.create_engine(url)
    if not database_exists(engine.url):
        create_database(engine.url)

    op.create_table(
        "sensors",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("device_id", sa.Text, nullable=False),
        sa.Column("datetime_created", sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table("sensors")
