"""add foreign key to Review

Revision ID: 2c02aac91b10
Revises: b5b9c747fa04
Create Date: 2025-01-16 11:20:58.298120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c02aac91b10'
down_revision = 'b5b9c747fa04'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        if not column_exists('reviews', 'employee_id'):
            batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_reviews_employee_id_employees',
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')


def column_exists(table_name, column_name):
    """Check if a column exists in a table."""
    from sqlalchemy import inspect
    bind = op.get_bind()
    inspector = inspect(bind)
    columns = [col['name'] for col in inspector.get_columns(table_name)]
    return column_name in columns
