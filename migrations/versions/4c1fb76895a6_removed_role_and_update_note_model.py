"""Removed Role, and update Note Model

Revision ID: 4c1fb76895a6
Revises: 488e3dae5a17
Create Date: 2015-12-09 03:36:07.840972

"""

# revision identifiers, used by Alembic.
revision = '4c1fb76895a6'
down_revision = '488e3dae5a17'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_table('roles')
    #op.add_column('notes', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.add_column('notes', sa.Column('updated_date', sa.DateTime(), nullable=True))
    #op.create_index(op.f('ix_notes_created_date'), 'notes', ['created_date'], unique=False)
    op.create_index(op.f('ix_notes_updated_date'), 'notes', ['updated_date'], unique=False)
    #op.drop_index('ix_notes_timestamp', table_name='notes')
    #op.drop_column('notes', 'timestamp')
    op.drop_column('users', 'role_id')

    op.alter_column('notes', 'timestamp', new_column_name='created_date')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('notes', sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    #op.create_index('ix_notes_timestamp', 'notes', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_notes_updated_date'), table_name='notes')
    #op.drop_index(op.f('ix_notes_created_date'), table_name='notes')
    op.drop_column('notes', 'updated_date')
    #op.drop_column('notes', 'created_date')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'roles_pkey'),
    sa.UniqueConstraint('name', name=u'roles_name_key')),
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True)),
    op.create_foreign_key(u'users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    ### end Alembic commands ###
