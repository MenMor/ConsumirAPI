from flask import Flask, jsonify

app = Flask(__name__)

# Datos sobre centros de reciclaje
recycling_centers = [
    {'id': 1, 'name': 'Centro Reciclaje Norte', 'location': 'Calle 123, Ciudad A'},
    {'id': 2, 'name': 'Centro Reciclaje Sur', 'location': 'Calle 456, Ciudad B'},
    {'id': 3, 'name': 'Eco Centro Este', 'location': 'Avenida 789, Ciudad C'},
    {'id': 4, 'name': 'Reciclaje Oeste', 'location': 'Camino 101, Ciudad D'},
    {'id': 5, 'name': 'Green Point Centro', 'location': 'Plaza 202, Ciudad E'},
    {'id': 6, 'name': 'EcoPunto SurEste', 'location': 'Ruta 303, Ciudad F'},
    {'id': 7, 'name': 'Eco Recicla Norte', 'location': 'Bulevar 404, Ciudad G'},
    {'id': 8, 'name': 'Recicladora Urbana', 'location': 'Callejón 505, Ciudad H'},
    {'id': 9, 'name': 'Punto Verde', 'location': 'Avenida 606, Ciudad I'},
    {'id': 10, 'name': 'Recicla Ya Centro', 'location': 'Camino 707, Ciudad J'},
    {'id': 11, 'name': 'Recolecta Eco', 'location': 'Sector 808, Ciudad K'},
    {'id': 12, 'name': 'Centro Limpio Este', 'location': 'Via 909, Ciudad L'},
    {'id': 13, 'name': 'EcoFacil', 'location': 'Paseo 1010, Ciudad M'},
    {'id': 14, 'name': 'Green City Recycle', 'location': 'Ronda 1111, Ciudad N'},
    {'id': 15, 'name': 'EcoServicios Centro', 'location': 'Circuito 1212, Ciudad O'},
    {'id': 16, 'name': 'Reciclaje Activo', 'location': 'Trayecto 1313, Ciudad P'},
    {'id': 17, 'name': 'Punto Recicla', 'location': 'Sector 1414, Ciudad Q'},
    {'id': 18, 'name': 'Centro Verde', 'location': 'Bulevar 1515, Ciudad R'},
    {'id': 19, 'name': 'Eco Zona Urbana', 'location': 'Avenida 1616, Ciudad S'},
    {'id': 20, 'name': 'ReciclaConNosotros', 'location': 'Camino 1717, Ciudad T'}
]


@app.route('/recycling_centers', methods=['GET'])
def get_recycling_centers():
    """Endpoint que devuelve una lista de centros de reciclaje."""
    return jsonify(recycling_centers)

@app.route('/recycling_center/<int:center_id>', methods=['GET'])
def get_recycling_center(center_id):
    """Endpoint que devuelve información sobre un centro de reciclaje específico."""
    center = next((center for center in recycling_centers if center['id'] == center_id), None)
    if center:
        return jsonify(center)
    else:
        return jsonify({'error': 'Centro de reciclaje no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True) 
