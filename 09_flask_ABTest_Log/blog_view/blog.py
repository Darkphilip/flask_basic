import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask, Blueprint, json, request,render_template, make_response, jsonify, redirect, url_for, session
from flask_login import UserMixin, login_user, current_user, logout_user
from blog_control.user_mgmt import User
from blog_control.session_mgmt import BlogSession
import datetime


blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods = ['GET', 'POST'])
def set_email():
  if request.method == 'GET':
    print('set_email:', request.args.get('user_email'))
    return redirect(url_for('blog.test_blog'))
  else:
    # print('set_email:', request.headers)
    # content type이 application/json인 경우
    # print('set_email:', request.get_json())
    # print('set_email:', request.form['user_email'])
    user = User.create(request.form['user_email'], request.form['blog_id'])
    login_user(user, remember=True, duration=datetime.timedelta(days=365))

    return redirect(url_for('blog.blog_fullstack1'))

  # return redirect('/blog/test_blog')
  # return make_response(jsonify(success = True), 200)

@blog_abtest.route('/logout')
def logout():
  User.delete(current_user.id)
  logout_user()
  return redirect(url_for('blog.blog_fullstack1'))

@blog_abtest.route('/blog_fullstack1')
def blog_fullstack1():
  if current_user.is_authenticated:
    webpage_name = BlogSession.get_blog_page(current_user.blog_id)
    BlogSession.save_session_info(
      session['client_id'], current_user.user_email, webpage_name)
    return render_template(webpage_name, user_email=current_user.user_email)
  else:
    webpage_name = BlogSession.get_blog_page()
    BlogSession.save_session_info(
      session['client_id'], 'anonymous', webpage_name)
    return render_template(webpage_name)

