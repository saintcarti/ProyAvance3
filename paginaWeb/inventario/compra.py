class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def agregar(self, camara):
        if str(camara.idCamara) not in self.carrito:
            self.carrito[str(camara.idCamara)] = {
                'idCamara': camara.idCamara,
                'nombreCamara': camara.nombreCamara,
                'precio': str(camara.precio),
                'cantidad': 1,
                'imagen': camara.imagen.url,
                'total': str(camara.precio)
            }
        else:
            for key, value in self.carrito.items():
                if key == str(camara.idCamara):
                    value["cantidad"] += 1
                    value["total"] = str(int(value["total"]) + camara.precio)
                    break
        self.guardar()

    def guardar(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, camara):
        id = str(camara.idCamara)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar()

    def restar(self, camara):
        for key, value in self.carrito.items():
            if key == str(camara.idCamara):
                if value["cantidad"] > 1:
                    value["cantidad"] -= 1
                    value["total"] = str(int(value["total"]) - camara.precio)
                else:
                    self.eliminar(camara)
                break
        self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
