from flask import Flask, jsonify, abort
import tier_controller

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return jsonify({
        'success': True
    })

@app.route('/tiers/<int:id>')
def getTier(id):
    tier = tier_controller.get_tier(id)

    if not tier:
        abort(404)

    return jsonify({
        'id': id,
        'tier': tier
    })

@app.errorhandler(404)
def page_not_found(error):
   return jsonify({
       'message': '404 - Not Found'
   })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)