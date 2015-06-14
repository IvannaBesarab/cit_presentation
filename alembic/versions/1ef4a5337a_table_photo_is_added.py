"""table Photo is added

Revision ID: 1ef4a5337a
Revises: 3cfce646762
Create Date: 2015-05-30 19:54:35.502475

"""

# revision identifiers, used by Alembic.
revision = '1ef4a5337a'
down_revision = '3cfce646762'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('issue_id', sa.Integer(), nullable=True),
                    sa.Column('file_path', sa.String(length=200), nullable=True),
                    sa.ForeignKeyConstraint(['issue_id'], ['issue.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###