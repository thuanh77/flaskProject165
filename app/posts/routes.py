from flask import render_template

from app import page
from app.posts import bp
from app.models.post import Post


@bp.route('/<int:page_num>')
def index(page_num):
    posts = Post.query.paginate(per_page=3, page=page_num)
    return render_template("posts/index.html", posts=posts)
