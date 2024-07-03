"""empty message

Revision ID: 150bd7d2a416
Revises: 38b2543e6ec9
Create Date: 2024-07-03 12:12:23.894817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '150bd7d2a416'
down_revision: Union[str, None] = '38b2543e6ec9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('enfant_video', 'taille')
    # op.create_primary_key(
    #     'pk_enfant_video',
    #     'enfant_video',
    #     ['enfant_id', 'video_id']
    # )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('enfant_video', sa.Column('taille', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
