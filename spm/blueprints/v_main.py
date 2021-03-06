from flask import Blueprint, request, abort, jsonify, session, render_template
from settings import TEMPLATES_FOLDER, STATIC_FOLDER
blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER,
    static_folder=STATIC_FOLDER)

from riakkit import NotFoundError

from spm.backend import users

from spm.blueprints.helpers import login_required

meta = {
    "url_prefix" : "",
}

# TODO: csrf this whole thing!

@blueprint.route("/")
def home():
  return render_template("home.html")

@blueprint.route("/login/", methods=["POST"])
def login():
  if "assertion" not in request.form:
    return abort(400)

  verification_data = users.do_login(request.form["assertion"])
  if verification_data:
    if verification_data["status"] == "okay":
      session["email"] = verification_data["email"]
      session["key"] = verification_data["key"]
    return jsonify(verification_data)

  return abort(500)

@blueprint.route("/logout/")
def logout():
  session.pop("email", None)
  session.pop("ukey", None)
  return jsonify(status="okay")

@blueprint.route("/profile/changename", methods=["POST"])
@login_required
def change_name():
  if "name" not in request.form:
    return abort(400)
  users.change_name(session["ukey"], request.form["name"])
  return jsonify(status="ok")

@blueprint.route("/profile/<key>")
@login_required
def view_profile(key):
  try:
    u = users.get_user_profile(key)
    u["status"] = "ok"
    return jsonify(u)
  except NotFoundError:
    return abort(404)
