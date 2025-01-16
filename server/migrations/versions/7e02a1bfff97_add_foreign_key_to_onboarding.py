"""add foreign key to onboarding

Revision ID: 7e02a1bfff97
Revises: 2c02aac91b10
Create Date: 2025-01-16 12:23:56.069196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e02a1bfff97'
down_revision = '2c02aac91b10'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f('fk_onboardings_employee_id_employees'),
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(
            batch_op.f('fk_onboardings_employee_id_employees'),
            type_='foreignkey'
        )
        batch_op.drop_column('employee_id')
