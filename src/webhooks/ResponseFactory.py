from flask import jsonify


class ResponseFactory:
    def create(self):
        headers = {    "Content-Type": "application/octet-stream",    "Content-Disposition": "attachment; filename=foobar.json"}
        return jsonify("success"), 200, headers