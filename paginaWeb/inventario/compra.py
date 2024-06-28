class Carrito:
    def __init__(self ,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def agregar(self, camara):
        if camara.idCamara not in self.carrito.keys():
            self.carrito[camara.idCamara] = {
                'idCamara': camara.idCamara,
                'nombreCamara': camara.nombreCamara,
                'precio': str(camara.precio),
                'cantidad': 1,
                'imagen': camara.imagen.url
            }
        else:
            for key, value in self.carrito.items():
                if key == camara.idCamara:
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = camara.precio
                    value["total"]= value["total"]
                    break
        self.guardar()

    def guardar(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
    
    def eliminar(self, camara):
        id = camara.idCamara
        if id in self.carrito:
            del self.carrito[id]
            self.guardar()

    def restar(self, camara):
        for key, value in self.carrito.items():
            if key == camara.idCamara:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- camara.precio
                if value["cantidad"] < 1:
                    self.eliminar(camara)
                break
        self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
