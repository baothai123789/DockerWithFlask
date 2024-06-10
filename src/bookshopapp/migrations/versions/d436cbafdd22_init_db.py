"""init db

Revision ID: d436cbafdd22
Revises: 
Create Date: 2024-06-10 11:18:42.728533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd436cbafdd22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_categories'))
    )
    op.create_table('languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_languages'))
    )
    op.create_table('nations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_nations'))
    )
    op.create_table('publishers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_publishers'))
    )
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=256), nullable=False),
    sa.Column('lastname', sa.String(length=256), nullable=False),
    sa.Column('nation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['nation_id'], ['nations.id'], name=op.f('fk_authors_nation_id_nations')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_authors'))
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bookid', sa.String(length=20), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('publish_year', sa.Integer(), nullable=True),
    sa.Column('language_id', sa.Integer(), nullable=True),
    sa.Column('publisher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['language_id'], ['languages.id'], name=op.f('fk_books_language_id_languages')),
    sa.ForeignKeyConstraint(['publisher_id'], ['publishers.id'], name=op.f('fk_books_publisher_id_publishers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books'))
    )
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_books_bookid'), ['bookid'], unique=True)

    op.create_table('books_authors',
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], name=op.f('fk_books_authors_author_id_authors')),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_books_authors_book_id_books'))
    )
    op.create_table('books_categories',
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_books_categories_book_id_books')),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name=op.f('fk_books_categories_category_id_categories'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books_categories')
    op.drop_table('books_authors')
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_books_bookid'))

    op.drop_table('books')
    op.drop_table('authors')
    op.drop_table('publishers')
    op.drop_table('nations')
    op.drop_table('languages')
    op.drop_table('categories')
    # ### end Alembic commands ###
